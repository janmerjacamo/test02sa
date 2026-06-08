# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaEquipoMarca(models.Model):
    _name = "localiza.equipo.marca"
    _description = "marcas de equipos"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Descripción")
    active = fields.Boolean(string="Activo", default=True)
    sequence = fields.Integer(string="Secuencia", default=10)
