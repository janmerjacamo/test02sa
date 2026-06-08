# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaActivoCintaTag(models.Model):
    _name = "localiza.activo.cinta.tag"
    _description = "Cintas Tags"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    color = fields.Integer(string="Color")
    name = fields.Char(string="Nombre")
    active = fields.Boolean(string="Activo", default=True)
    sequence = fields.Integer(string="Secuencia", default=10)
