# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaTelefoniaLinea(models.Model):
    _name = "localiza.telefonia.linea"
    _description = "GESTION DE LINEAS"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    has_message = fields.Boolean(string="Has Message")
    sms_delivery_error = fields.Boolean(string="SMS Delivery error")
    # ratings: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    active = fields.Boolean(string="Activo")
    currency = fields.Many2one("res.currency", string="Currency", ondelete="set null")
    name = fields.Char(string="Descripción")
    asignada_equipo = fields.Boolean(string="Asignada / Equipo")
    asignada_equipo_2 = fields.Boolean(string="Asignada / Equipo")
    new_texto = fields.Char(string="New Texto")
    costo_q = fields.Float(string="Costo Q")
    new_fecha_y_hora = fields.Datetime(string="New Fecha y hora ")
    new_fecha_y_hora_2 = fields.Datetime(string="New Fecha y hora ")
    esta_asignada_a_una_sim_plastica = fields.Boolean(string="Esta asignada a una SIM Plástica:")
    esta_asignada_a_una_sim_plastica_2 = fields.Boolean(string="Esta asignada a una SIM Plástica:")
    fin_de_contrato = fields.Datetime(string="FIN DE CONTRATO:")
    fin_de_contrato_2 = fields.Datetime(string="FIN DE CONTRATO:")
    inicio_de_contrato = fields.Datetime(string="INICIO DE CONTRATO:")
    numero_de_lineas = fields.Char(string="Número de Líneas")
    numero_de_lineas_2 = fields.Char(string="Número de Líneas")
    numero_de_lineas_3 = fields.Char(string="Número de Líneas")
    sequence = fields.Integer(string="Secuencia")
