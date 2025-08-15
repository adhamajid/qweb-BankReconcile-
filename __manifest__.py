# -*- coding: utf-8 -*-
{
    'name': "Custom Bank Reconcile",

    'summary': "Modul Kustomisasi untuk Bank Reconcile",

    'description': """
        Modul Kustom untuk Bank Reconcile
    """,

    'author': "Majid",
    'website': "https://instagram.com/asyah_majid",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    'depends': ['base','mail','account_accountant','account','account_asset'],

    # always loaded
    'data': [      

    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'qweb-bankreconcile/static/src/components/**/*',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'icon': '/qweb-bankreconcile/static/description/majid_icon.jpg',
}

