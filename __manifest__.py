# -*- coding: utf-8 -*-
{
    'name': "Index Scrum Management",

    'summary': """
        Ajout champ 'Dedié à' dans Projet """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Index Consulting Madagascar",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        "views/assets.xml",
        'views/project.xml',
        "views/hr_attendance.xml",
    ],
    "qweb": [
        "static/src/xml/recap_task.xml",
    ],

}
