# -*- coding: utf-8 -*-
{
    'name': "Portal de Auto-Facturacion CFDI",

    'summary': """
        Portal de Cliente diseñado para generar facturas desde la Web.""",

    'description': """

Portal Auto-Facturacion CFDI
================================

Permite al Cliente poder generar su Factura mediante la Parte Web.

    """,

    'author': "IT Admin",
    'website': "www.itadmin.com.mx",
    'category': 'Facturacion Electronica',
    'version': '15.04',
    'depends': [
        'website_sale_stock',
        'website_crm',
        'sale',
        'cdfi_invoice',
        ],
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_common': [
            'website_self_cfdi_invoice/static/src/js/website.js',
        ],
    },

}
