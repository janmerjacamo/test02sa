# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaActivoLine(models.Model):
    _name = "localiza.activo.line"
    _description = "gestion_de_activos_line"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    x_gestion_de_activos = fields.Many2one("localiza.activo", string="X Gestion De Activos", ondelete="set null")
    name = fields.Char(string="Descripción")
    sequence = fields.Integer(string="Secuencia")
    active = fields.Boolean(string="Activo", default=True)
