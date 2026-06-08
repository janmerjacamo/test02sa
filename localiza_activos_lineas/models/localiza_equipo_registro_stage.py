# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaEquipoRegistroStage(models.Model):
    _name = "localiza.equipo.registro.stage"
    _description = "Registros de Equipos Stages"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nombre de la etapa")
    sequence = fields.Integer(string="Secuencia")
    active = fields.Boolean(string="Activo", default=True)
