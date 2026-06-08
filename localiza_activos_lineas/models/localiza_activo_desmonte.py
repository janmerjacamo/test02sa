# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaActivoDesmonte(models.Model):
    _name = "localiza.activo.desmonte"
    _description = "Desmontes"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    has_message = fields.Boolean(string="Has Message")
    sms_delivery_error = fields.Boolean(string="SMS Delivery error")
    # ratings: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    active = fields.Boolean(string="Activo")
    name = fields.Char(string="Descripción")
    apagado = fields.Char(string="APAGADO")
    boleta = fields.Char(string="BOLETA")
    cliente = fields.Char(string="CLIENTE")
    cliente_2 = fields.Char(string="CLIENTE")
    fecha = fields.Date(string="Fecha")
    fecha_e = fields.Date(string="FECHA E.")
    imei = fields.Many2one("localiza.equipo.registro", string="IMEI", ondelete="set null")
    modelo = fields.Many2one("localiza.equipo.modelo", string="MODELO", ondelete="set null")
    motivo = fields.Char(string="MOTIVO")
    placa = fields.Char(string="PLACA")
    resultado = fields.Char(string="RESULTADO", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    sequence = fields.Integer(string="Secuencia")
    sim_numero = fields.Char(string="SIM/NUMERO")
    tecnico = fields.Many2one("localiza.tecnico", string="TECNICO", ondelete="set null")
