# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaTelefoniaRegistroLineaDetalle(models.Model):
    _name = "localiza.telefonia.registro.linea.detalle"
    _description = "registros_line"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="ICC NUEVA:")
    x_registros = fields.Many2one("localiza.telefonia.registro.linea", string="X Registros", ondelete="set null")
    fecha_y_hora_de_migracion = fields.Datetime(string="Fecha y hora de Migración:")
    sequence = fields.Integer(string="Secuencia")
    active = fields.Boolean(string="Activo", default=True)
