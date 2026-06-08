# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LocalizaExtProduct_template(models.Model):
    _inherit = "product.template"

    compania_telefonica = fields.Char(string="Compañía Telefónica:", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    fecha_y_hora_de_registro = fields.Datetime(string="Fecha y hora  de  Registro:")
    fecha_hora_de_registro = fields.Datetime(string="FECHA/HORA DE REGISTRO:")
    fecha_hora_de_registro_2 = fields.Datetime(string="FECHA/HORA DE REGISTRO:")
    fin_contrato = fields.Date(string="FIN / CONTRATO:")
    icc_actual = fields.Char(string="ICC-ACTUAL:")
    imei_de_equipo = fields.Char(string="IMEI de Equipo:")
    inicio_contrato = fields.Date(string="INICIO / CONTRATO:")
    linea = fields.Char(string="LINEA")
    lote_de_orden_compra = fields.Char(string="Lote de Orden / Compra:")
    lote_de_orden_compra_2 = fields.Char(string="Lote de Orden / Compra:")
    lote_de_orden_compra_3 = fields.Char(string="Lote de Orden / Compra:")
    marca = fields.Many2one("localiza.catalogo.marca", string="MARCA", ondelete="set null")
    marcas = fields.Char(string="MARCAS:", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    modelos = fields.Char(string="MODELOS: ", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    plan_de_datos = fields.Char(string="PLAN DE DATOS: ", help="Campo convertido desde selección de Studio; revisar opciones originales antes de producción.")
    ruta_historica_apps = fields.Char(string="Ruta histórica apps ")
