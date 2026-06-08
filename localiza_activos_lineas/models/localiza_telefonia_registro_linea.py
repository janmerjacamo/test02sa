# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaTelefoniaRegistroLinea(models.Model):
    _name = "localiza.telefonia.registro.linea"
    _description = "Registros LINEAS"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    has_message = fields.Boolean(string="Has Message")
    sms_delivery_error = fields.Boolean(string="SMS Delivery error")
    # ratings: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    active = fields.Boolean(string="Activo")
    name = fields.Char(string="Número de Líneas")
    asignada_equipo = fields.Boolean(string="Asignada / Equipo")
    new_casilla_de_verificacion = fields.Boolean(string="New Casilla de verificación")
    esta_asignada_a_una_sim_plastica = fields.Boolean(string="Esta asignada a una SIM Plástica:")
    plan_de_datos = fields.Char(string="Plan de datos:")
    moneda = fields.Many2one("res.currency", string="Moneda", ondelete="set null")
    new_fecha_y_hora = fields.Datetime(string="New Fecha y hora ")
    esta = fields.Boolean(string="esta")
    esta_asignada_a_un_equipo = fields.Boolean(string="Esta asignada a un Equipo:")
    estado_en_equipos = fields.Char(string="ESTADO EN EQUIPOS:")
    fecha = fields.Datetime(string="Fecha:")
    fecha_de_registro_de_la_linea = fields.Datetime(string="Fecha de registro de la Línea")
    fin_de_contrato = fields.Datetime(string="FIN DE CONTRATO:")
    icc_actual = fields.Char(string="ICC Actual:")
    inicio_de_contrato = fields.Char(string="INICIO DE CONTRATO:")
    inicio_de_contrato_2 = fields.Datetime(string="INICIO DE CONTRATO:")
    lote_migrado = fields.Char(string="Lote / Migrado")
    asignados = fields.Many2one("localiza.asignado", string="Asignados", ondelete="set null")
    plan_de_datos_2 = fields.Many2one("localiza.telefonia.plan.datos", string="Plan de Datos", ondelete="set null")
    compania_telefonica = fields.Many2one("localiza.telefonia.compania", string="Compañía Telefónica", ondelete="set null")
    # lineas_nuevas: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    sequence = fields.Integer(string="Secuencia")
    responsable = fields.Many2one("res.users", string="Responsable", ondelete="set null")
    costo_q = fields.Float(string="Costo Q")
