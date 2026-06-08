# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaActivoSenuelo(models.Model):
    _name = "localiza.activo.senuelo"
    _description = "Señuelos"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    has_message = fields.Boolean(string="Has Message")
    sms_delivery_error = fields.Boolean(string="SMS Delivery error")
    # ratings: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    active = fields.Boolean(string="Activo")
    avatar = fields.Binary(string="Avatar")
    name = fields.Char(string="Descripción")
    moneda = fields.Many2one("res.currency", string="Moneda", ondelete="set null")
    marca = fields.Many2one("localiza.equipo.marca", string="MARCA", ondelete="set null")
    modelo = fields.Many2one("localiza.equipo.modelo", string="MODELO", ondelete="set null")
    sequence = fields.Integer(string="Secuencia")
    valor = fields.Float(string="Valor")
