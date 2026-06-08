# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaActivo(models.Model):
    _name = "localiza.activo"
    _description = "GESTION DE ACTIVOS"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    has_message = fields.Boolean(string="Has Message")
    sms_delivery_error = fields.Boolean(string="SMS Delivery error")
    # ratings: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    active = fields.Boolean(string="Activo")
    # lineas_nuevas: One2many original de Studio omitido para evitar errores; se recrea desde el modelo hijo con Many2one.
    name = fields.Char(string="Descripción")
    antena_gps = fields.Boolean(string="Antena GPS")
    ano = fields.Char(string="Año")
    apagado_de_motor = fields.Boolean(string="Apagado de Motor")
    avl = fields.Boolean(string="AVL")
    bateria_de_respaldo = fields.Boolean(string="Batería de Respaldo")
    bateria_extra = fields.Boolean(string="Batería Extra")
    new_casilla_de_verificacion = fields.Boolean(string="New Casilla de verificación")
    boton_de_panico = fields.Boolean(string="Botón de Pánico")
    boton_de_panico_2 = fields.Boolean(string="Botón de Pánico")
    chasis = fields.Char(string="Chasis")
    cliente_transportista = fields.Many2one("hr.employee", string="Cliente/Transportista:", ondelete="set null")
    color = fields.Char(string="Color")
    desconexion = fields.Boolean(string="Desconexión")
    fecha_hora = fields.Datetime(string="Fecha / Hora:")
    imagen = fields.Binary(string="Imagen")
    lugar_de_trabajo = fields.Char(string="Lugar de trabajo:")
    magnetico = fields.Boolean(string="Magnético")
    modelos = fields.Many2one("ir.model", string="Modelos", ondelete="set null")
    modelos_de_equipos = fields.Many2one("localiza.equipo.modelo", string="Modelos de Equipos", ondelete="set null")
    marcas_de_equipos = fields.Many2one("localiza.equipo.marca", string="Marcas de Equipos", ondelete="set null")
    microfono = fields.Boolean(string="Micrófono")
    multimedia_1 = fields.Binary(string="Multimedia 1")
    multimedia_2 = fields.Binary(string="Multimedia 2")
    no_se_coloca_apagado = fields.Boolean(string="No se coloca apagado")
    notas_de_instalacion = fields.Text(string="Notas de Instalación")
    notas_de_instalacion_2 = fields.Text(string="Notas de Instalación")
    notas_inspeccion_vehiculo = fields.Text(string="Notas Inspección Vehículo")
    placa = fields.Char(string="Placa")
    posicion_de_equipo = fields.Char(string="Posición de equipo")
    realay_24_voltios = fields.Boolean(string="Realay 24 Voltios")
    relay_12_voltios = fields.Boolean(string="Relay 12 Voltios")
    responsable = fields.Many2one("res.users", string="Responsable", ondelete="set null")
    sequence = fields.Integer(string="Secuencia")
    tamper = fields.Boolean(string="Tamper")
    tamper_2 = fields.Boolean(string="Tamper")
    tecnico = fields.Many2one("hr.employee", string="Técnico:", ondelete="set null")
    tipo = fields.Char(string="Tipo")
    responsable_2 = fields.Many2one("res.users", string="Responsable", ondelete="set null")
