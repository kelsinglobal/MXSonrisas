# -*- coding: utf-8 -*-


{
    'name': 'Easi Medical Personnel',
    'category': 'Human Resources/Employees',
    'sequence': 150,
    'summary': 'Manage medical personnel',
    'description': """
    Manage medical personnel
""",
    'depends': ['hr'],
    'data': [
        'views/medical_personnel_views.xml',
        'views/menu_views.xml',
        'data/medical_personnel_data.xml',
        'security/ir.model.access.csv',
    ],
    'application': True,
    'license': 'LGPL-3',
}
