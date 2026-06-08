# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaTelefoniaPlanDatos(models.Model):
    _name = "localiza.telefonia.plan.datos"
    _description = "Plan de Datos"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    has_message = fields.Boolean(string="Has Message")
    sms_delivery_error = fields.Boolean(string="SMS Delivery error")
    # ratings: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    active = fields.Boolean(string="Activo")
    name = fields.Char(string="Nombre")
    moneda = fields.Many2one("res.currency", string="Moneda", ondelete="set null")
    sequence = fields.Integer(string="Secuencia")
    costo = fields.Float(string="Costo:")
