# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    x_localiza_tipo_operativo = fields.Selection([
        ('uniforme', 'Uniforme'),
        ('bota', 'Bota'),
        ('insumo', 'Insumo operativo'),
        ('gps', 'GPS / equipo seriado'),
        ('vehiculo_insumo', 'Insumo vehicular'),
        ('otro', 'Otro'),
    ], string='Tipo operativo Localiza', index=True)
    x_localiza_criticidad = fields.Selection([
        ('normal', 'Normal'),
        ('bajo_control', 'Bajo control'),
        ('critico', 'Crítico'),
    ], string='Criticidad', default='normal')
    x_localiza_stock_minimo = fields.Float(string='Stock mínimo operativo', default=0.0)
    x_localiza_requiere_puesto = fields.Boolean(string='Requiere puesto/destino')
    x_localiza_notas_operativas = fields.Text(string='Notas operativas')
