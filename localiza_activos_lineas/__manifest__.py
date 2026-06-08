# -*- coding: utf-8 -*-
{
    "name": "Localiza Activos, SIM y Líneas",
    "version": "19.0.1.0.0",
    "category": "Localiza",
    "summary": "Módulo limpio para reemplazar personalizaciones de Odoo Studio.",
    "author": "XIM Power / Localiza",
    "license": "LGPL-3",
    "depends": ['base', 'mail', 'product', 'stock', 'purchase', 'localiza_studio_core'],
    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/views.xml",
        "views/menus.xml",
    ],
    "installable": True,
    "application": True,
}
