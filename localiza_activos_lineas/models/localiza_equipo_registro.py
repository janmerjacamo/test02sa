# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaEquipoRegistro(models.Model):
    _name = "localiza.equipo.registro"
    _description = "Registros de Equipos"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    has_message = fields.Boolean(string="Has Message")
    sms_delivery_error = fields.Boolean(string="SMS Delivery error")
    # ratings: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    active = fields.Boolean(string="Activo")
    color = fields.Integer(string="Color")
    currency = fields.Many2one("res.currency", string="Currency", ondelete="set null")
    name = fields.Char(string="Descripción")
    moneda = fields.Many2one("res.currency", string="Moneda", ondelete="set null")
    fecha_de_compra = fields.Date(string="FECHA DE COMPRA")
    iva = fields.Float(string="IVA")
    estado_de_kanban = fields.Char(string="Estado de kanban", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    modelo = fields.Many2one("localiza.equipo.modelo", string="MODELO", ondelete="set null")
    marca = fields.Many2one("localiza.equipo.marca", string="MARCA", ondelete="set null")
    moneda_2 = fields.Many2one("res.currency", string="Moneda", ondelete="set null")
    no_factura = fields.Char(string="NO. FACTURA")
    no_serie = fields.Char(string="NO. SERIE")
    notas = fields.Html(string="Notas")
    alta_prioridad = fields.Boolean(string="Alta Prioridad")
    proveedor = fields.Many2one("res.partner", string="PROVEEDOR", ondelete="set null")
    sequence = fields.Integer(string="Secuencia")
    sim = fields.Char(string="SIM")
    etapa = fields.Many2one("localiza.equipo.registro.stage", string="Etapa", ondelete="set null")
    valor = fields.Float(string="Valor")
    imei_count = fields.Integer(string="IMEI count")
    registros_de_equipos_count = fields.Integer(string="Registros de Equipos count")
