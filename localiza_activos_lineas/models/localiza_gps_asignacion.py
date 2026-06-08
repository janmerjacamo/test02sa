# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaGpsAsignacion(models.Model):
    _name = "localiza.gps.asignacion"
    _description = "Asignaciones GPS"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    has_message = fields.Boolean(string="Has Message")
    sms_delivery_error = fields.Boolean(string="SMS Delivery error")
    # ratings: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    active = fields.Boolean(string="Activo")
    name = fields.Char(string="ICC Nueva")
    compania_telefonica = fields.Char(string="Compañía telefónica", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    e = fields.Boolean(string="e")
    esta_asignada_a_un_equipo = fields.Boolean(string="Esta asignada a un Equipo:")
    habilitado = fields.Boolean(string="HABILITADO")
    estado_de_la_sim = fields.Char(string="Estado de la SIM:", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    fecha_y_hora_de_migracion = fields.Datetime(string="Fecha y hora de Migración:")
    fecha_hora_de_registro = fields.Datetime(string="Fecha/Hora de Registro:")
    linea_asignada = fields.Many2one("localiza.telefonia.linea", string="Línea Asignada", ondelete="set null")
    lote = fields.Char(string="Lote:")
    many2one_field_ghx2n = fields.Many2one("localiza.telefonia.registro.linea", string="X Studio Many2One Field Ghx2N", ondelete="set null")
    registros_lineas = fields.Many2one("localiza.telefonia.registro.linea", string="Registros LINEAS", ondelete="set null")
    notas = fields.Html(string="Notas")
    new_campo_relacionado = fields.Char(string="New Campo relacionado")
    sequence = fields.Integer(string="Secuencia")
