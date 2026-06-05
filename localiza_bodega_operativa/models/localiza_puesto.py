# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class LocalizaPuesto(models.Model):
    _name = 'localiza.puesto'
    _description = 'Puesto operativo Localiza'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'

    name = fields.Char(required=True, tracking=True)
    code = fields.Char(string='Código', copy=False, readonly=True, default='Nuevo')
    tipo = fields.Selection([
        ('capital', 'Capital'),
        ('departamental', 'Departamental'),
        ('bodega', 'Bodega / Base'),
        ('cliente', 'Cliente'),
    ], required=True, default='capital', tracking=True)
    partner_id = fields.Many2one('res.partner', string='Cliente / contacto')
    supervisor_id = fields.Many2one('hr.employee', string='Supervisor')
    address = fields.Char(string='Dirección')
    active = fields.Boolean(default=True, tracking=True)
    state = fields.Selection([
        ('alta', 'Alta'),
        ('baja', 'Baja'),
    ], default='alta', required=True, tracking=True)
    fecha_inicio = fields.Date(string='Fecha inicio')
    fecha_baja = fields.Date(string='Fecha baja')
    agentes = fields.Integer(string='Cantidad de agentes', default=1)
    location_id = fields.Many2one('stock.location', string='Ubicación de inventario', readonly=True, copy=False)
    notes = fields.Text(string='Observaciones')
    entrega_count = fields.Integer(compute='_compute_entrega_count')

    @api.model_create_multi
    def create(self, vals_list):
        seq = self.env['ir.sequence']
        for vals in vals_list:
            if vals.get('code', 'Nuevo') == 'Nuevo':
                vals['code'] = seq.next_by_code('localiza.puesto') or 'Nuevo'
        records = super().create(vals_list)
        records._ensure_stock_locations()
        return records

    def write(self, vals):
        res = super().write(vals)
        if 'name' in vals or 'tipo' in vals:
            self._ensure_stock_locations()
        return res

    def _ensure_stock_locations(self):
        parent = self.env.ref('localiza_bodega_operativa.stock_location_localiza_puestos', raise_if_not_found=False)
        if not parent:
            return
        for rec in self:
            if not rec.location_id:
                loc = self.env['stock.location'].create({
                    'name': '[%s] %s' % (rec.code or 'PTO', rec.name),
                    'usage': 'internal',
                    'location_id': parent.id,
                    'company_id': self.env.company.id,
                })
                rec.location_id = loc.id
            else:
                rec.location_id.name = '[%s] %s' % (rec.code or 'PTO', rec.name)

    def action_baja(self):
        for rec in self:
            rec.write({'state': 'baja', 'active': False, 'fecha_baja': fields.Date.context_today(rec)})

    def action_alta(self):
        for rec in self:
            rec.write({'state': 'alta', 'active': True, 'fecha_baja': False})

    def _compute_entrega_count(self):
        data = self.env['localiza.entrega'].read_group([('puesto_id', 'in', self.ids)], ['puesto_id'], ['puesto_id'])
        mapped = {d['puesto_id'][0]: d['puesto_id_count'] for d in data if d.get('puesto_id')}
        for rec in self:
            rec.entrega_count = mapped.get(rec.id, 0)

    def action_view_entregas(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Entregas'),
            'res_model': 'localiza.entrega',
            'view_mode': 'list,form',
            'domain': [('puesto_id', '=', self.id)],
            'context': {'default_puesto_id': self.id},
        }
