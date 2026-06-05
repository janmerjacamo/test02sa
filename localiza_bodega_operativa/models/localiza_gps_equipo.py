# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class LocalizaGpsEquipo(models.Model):
    _name = 'localiza.gps.equipo'
    _description = 'Equipo GPS Localiza'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'

    name = fields.Char(string='IMEI / Identificador', required=True, index=True, tracking=True)
    product_id = fields.Many2one('product.product', string='Producto Odoo', required=True)
    lot_id = fields.Many2one('stock.lot', string='Serie / lote Odoo')
    modelo = fields.Char(string='Modelo', tracking=True)
    marca = fields.Char(string='Marca')
    fecha_compra = fields.Date(string='Fecha compra')
    proveedor_id = fields.Many2one('res.partner', string='Proveedor')
    factura = fields.Char(string='Factura')
    no_serie = fields.Char(string='No. serie proveedor')
    costo = fields.Float(string='Costo')
    iva = fields.Float(string='IVA')
    placa = fields.Char(string='Placa')
    cliente_id = fields.Many2one('res.partner', string='Cliente')
    puesto_id = fields.Many2one('localiza.puesto', string='Puesto / destino')
    state = fields.Selection([
        ('bodega', 'En bodega'),
        ('asignado', 'Asignado'),
        ('instalado', 'Instalado'),
        ('retirado', 'Retirado'),
        ('danado', 'Dañado'),
        ('perdido', 'Perdido'),
    ], default='bodega', tracking=True, index=True)
    notes = fields.Text(string='Observaciones')

    _sql_constraints = [
        ('imei_unique', 'unique(name)', 'El IMEI / identificador ya existe.'),
    ]

    @api.onchange('product_id')
    def _onchange_product_id(self):
        for rec in self:
            if rec.product_id and rec.product_id.tracking == 'none':
                rec.product_id.tracking = 'serial'

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        records._ensure_lots()
        return records

    def _ensure_lots(self):
        Lot = self.env['stock.lot']
        for rec in self:
            if rec.product_id and not rec.lot_id:
                lot = Lot.search([
                    ('name', '=', rec.name),
                    ('product_id', '=', rec.product_id.id),
                    ('company_id', 'in', [False, self.env.company.id]),
                ], limit=1)
                if not lot:
                    lot = Lot.create({
                        'name': rec.name,
                        'product_id': rec.product_id.id,
                        'company_id': self.env.company.id,
                    })
                rec.lot_id = lot.id

    def action_mark_installed(self):
        self.write({'state': 'instalado'})

    def action_mark_bodega(self):
        self.write({'state': 'bodega', 'puesto_id': False})
