# -*- coding: utf-8 -*-
{
    'name': "Easi manage appointment medical",
    'summary': """
        Manage appointment medical""",
    'description': """
       Manage appointment medical
    """,
    'author': "",
    'website': "",
    'category': '',
    'version': '1.0',
    'depends': ['easi_areas_attention', 'easi_medical_personnel'],
    'data': [
        'security/ir.model.access.csv',
        'views/calendar_views.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
