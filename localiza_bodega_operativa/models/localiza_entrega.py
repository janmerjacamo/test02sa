# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class LocalizaEntrega(models.Model):
    _name = 'localiza.entrega'
    _description = 'Entrega operativa de bodega'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date desc, id desc'

    name = fields.Char(default='Nuevo', copy=False, readonly=True)
    date = fields.Date(string='Fecha', default=fields.Date.context_today, required=True, tracking=True)
    tipo = fields.Selection([
        ('uniforme', 'Uniforme'),
        ('insumo', 'Insumo'),
        ('gps', 'GPS / equipo seriado'),
        ('otro', 'Otro'),
    ], required=True, default='insumo', tracking=True)
    receptor = fields.Char(string='Receptor', tracking=True)
    employee_id = fields.Many2one('hr.employee', string='Empleado')
    partner_id = fields.Many2one('res.partner', string='Contacto / cliente')
    puesto_id = fields.Many2one('localiza.puesto', string='Puesto / destino', tracking=True)
    location_src_id = fields.Many2one('stock.location', string='Ubicación origen', required=True,
                                      default=lambda self: self.env.ref('stock.stock_location_stock', raise_if_not_found=False))
    location_dest_id = fields.Many2one('stock.location', string='Ubicación destino', compute='_compute_location_dest', store=True, readonly=False)
    picking_id = fields.Many2one('stock.picking', string='Transferencia Odoo', readonly=True, copy=False)
    notes = fields.Text(string='Observaciones')
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmada'),
        ('done', 'Entregada'),
        ('cancel', 'Cancelada'),
    ], default='draft', tracking=True)
    line_ids = fields.One2many('localiza.entrega.line', 'entrega_id', string='Líneas')
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company, required=True)

    @api.model_create_multi
    def create(self, vals_list):
        seq = self.env['ir.sequence']
        for vals in vals_list:
            if vals.get('name', 'Nuevo') == 'Nuevo':
                vals['name'] = seq.next_by_code('localiza.entrega') or 'Nuevo'
        return super().create(vals_list)

    @api.depends('puesto_id', 'partner_id')
    def _compute_location_dest(self):
        fallback = self.env.ref('localiza_bodega_operativa.stock_location_localiza_entregados', raise_if_not_found=False)
        for rec in self:
            rec.location_dest_id = rec.puesto_id.location_id.id if rec.puesto_id and rec.puesto_id.location_id else (fallback.id if fallback else False)

    def action_confirm(self):
        for rec in self:
            if not rec.line_ids:
                raise UserError(_('Agrega al menos una línea.'))
            rec.state = 'confirmed'

    def action_done(self):
        for rec in self:
            if rec.state == 'draft':
                rec.action_confirm()
            picking = rec._create_internal_picking()
            rec.picking_id = picking.id
            rec.state = 'done'
            for line in rec.line_ids.filtered(lambda l: l.gps_equipo_id):
                vals = {'state': 'asignado'}
                if rec.puesto_id:
                    vals['puesto_id'] = rec.puesto_id.id
                line.gps_equipo_id.write(vals)

    def action_cancel(self):
        for rec in self:
            if rec.picking_id and rec.picking_id.state not in ('done', 'cancel'):
                rec.picking_id.action_cancel()
            rec.state = 'cancel'

    def _create_internal_picking(self):
        self.ensure_one()
        if self.picking_id:
            return self.picking_id
        picking_type = self.env['stock.picking.type'].search([
            ('code', '=', 'internal'),
            ('warehouse_id.company_id', '=', self.company_id.id),
        ], limit=1)
        if not picking_type:
            picking_type = self.env['stock.picking.type'].search([('code', '=', 'internal')], limit=1)
        if not picking_type:
            raise UserError(_('No se encontró un tipo de operación interna de inventario.'))
        picking = self.env['stock.picking'].create({
            'picking_type_id': picking_type.id,
            'location_id': self.location_src_id.id,
            'location_dest_id': self.location_dest_id.id,
            'origin': self.name,
            'scheduled_date': fields.Datetime.now(),
        })
        for line in self.line_ids:
            move = self.env['stock.move'].create({
                'name': line.product_id.display_name,
                'product_id': line.product_id.id,
                'product_uom_qty': line.qty,
                'product_uom': line.product_id.uom_id.id,
                'picking_id': picking.id,
                'location_id': self.location_src_id.id,
                'location_dest_id': self.location_dest_id.id,
            })
            move._action_confirm()
            move._action_assign()
            line._set_done_quantity(move)
        picking.button_validate()
        return picking

    def action_view_picking(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Transferencia'),
            'res_model': 'stock.picking',
            'view_mode': 'form',
            'res_id': self.picking_id.id,
        }


class LocalizaEntregaLine(models.Model):
    _name = 'localiza.entrega.line'
    _description = 'Línea de entrega operativa'

    entrega_id = fields.Many2one('localiza.entrega', required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Producto', required=True)
    qty = fields.Float(string='Cantidad', default=1.0, required=True)
    lot_id = fields.Many2one('stock.lot', string='Serie / lote')
    gps_equipo_id = fields.Many2one('localiza.gps.equipo', string='Equipo GPS')
    talla = fields.Char(string='Talla')
    notes = fields.Char(string='Observación')

    @api.onchange('gps_equipo_id')
    def _onchange_gps_equipo_id(self):
        for line in self:
            if line.gps_equipo_id:
                line.product_id = line.gps_equipo_id.product_id.id
                line.lot_id = line.gps_equipo_id.lot_id.id
                line.qty = 1.0

    def _set_done_quantity(self, move):
        self.ensure_one()
        vals = {'quantity': self.qty}
        if self.lot_id:
            vals['lot_id'] = self.lot_id.id
        if move.move_line_ids:
            move.move_line_ids[0].write(vals)
        else:
            vals.update({
                'move_id': move.id,
                'picking_id': move.picking_id.id,
                'product_id': self.product_id.id,
                'product_uom_id': self.product_id.uom_id.id,
                'location_id': move.location_id.id,
                'location_dest_id': move.location_dest_id.id,
            })
            self.env['stock.move.line'].create(vals)
