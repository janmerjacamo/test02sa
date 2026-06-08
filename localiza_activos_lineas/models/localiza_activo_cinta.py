# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaActivoCinta(models.Model):
    _name = "localiza.activo.cinta"
    _description = "Cintas"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    has_message = fields.Boolean(string="Has Message")
    sms_delivery_error = fields.Boolean(string="SMS Delivery error")
    # ratings: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    active = fields.Boolean(string="Activo")
    name = fields.Char(string="Descripción")
    fecha = fields.Date(string="Fecha")
    fecha_de_entrega = fields.Date(string="FECHA DE ENTREGA")
    sequence = fields.Integer(string="Secuencia")
    etiquetas = fields.Many2many("localiza.activo.cinta.tag", string="Etiquetas")
    tecnico = fields.Many2one("localiza.tecnico", string="TECNICO", ondelete="set null")
    tipo_cinta = fields.Many2one("localiza.activo.tipo.cinta", string="TIPO CINTA", ondelete="set null")
