# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaTelefoniaSim(models.Model):
    _name = "localiza.telefonia.sim"
    _description = "SIM Registro"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    has_message = fields.Boolean(string="Has Message")
    sms_delivery_error = fields.Boolean(string="SMS Delivery error")
    # ratings: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    active = fields.Boolean(string="Activo")
    name = fields.Char(string="ICC:")
    actualizar_estados = fields.Boolean(string="ACTUALIZAR ESTADOS:")
    lote = fields.Char(string="Lote:")
    compania_telefonica = fields.Char(string="Compañía telefónica:", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    estado_de_la_sim = fields.Char(string="Estado de la SIM:", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    fecha_y_hora_de_migracion = fields.Datetime(string="Fecha y hora de Migración:")
    fecha_hora_de_registro = fields.Datetime(string="Fecha/Hora de Registro:")
    habilitado = fields.Boolean(string="HABILITADO")
    linea = fields.Many2one("localiza.telefonia.linea", string="LINEA:", ondelete="set null")
    linea_2 = fields.Many2one("localiza.telefonia.registro.linea", string="LINEA:", ondelete="set null")
    registros_lineas = fields.Many2one("localiza.telefonia.registro.linea", string="Registros LINEAS", ondelete="set null")
    gestion_de_lineas = fields.Many2one("localiza.telefonia.linea", string="GESTION DE LINEAS", ondelete="set null")
    companias = fields.Many2one("res.company", string="Compañías", ondelete="set null")
    observaciones = fields.Text(string="Observaciones:")
    sequence = fields.Integer(string="Secuencia")
    responsable = fields.Many2one("res.users", string="Responsable", ondelete="set null")
