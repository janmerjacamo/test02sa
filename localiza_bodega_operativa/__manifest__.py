# -*- coding: utf-8 -*-
{
    'name': 'Localiza Bodega Operativa',
    'version': '19.0.1.0.3',
    'category': 'Inventory/Inventory',
    'summary': 'Gestión operativa de bodega: uniformes, insumos, GPS, puestos y entregas',
    'description': '''
Localiza Bodega Operativa
=========================
App integrada con Inventario para controlar productos operativos, GPS seriados,
puestos, entregas y carga masiva desde Excel.
    ''',
    'author': 'XIM Technology / Localiza',
    'website': 'https://ximpower.com',
    'license': 'LGPL-3',
    'depends': ['stock', 'product', 'contacts', 'mail', 'hr'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequences.xml',
        'data/product_categories.xml',
        'data/stock_locations.xml',
        'views/product_template_views.xml',
        'views/localiza_puesto_views.xml',
        'views/localiza_gps_equipo_views.xml',
        'views/localiza_entrega_views.xml',
        'views/localiza_dashboard_views.xml',
        'wizard/localiza_import_wizard_views.xml',
        'views/menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'localiza_bodega_operativa/static/src/scss/localiza_backend.scss',
        ],
    },
    'application': True,
    'installable': True,
}
