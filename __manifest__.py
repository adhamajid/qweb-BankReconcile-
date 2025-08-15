# -*- coding: utf-8 -*-
{
    'name': "Modul Kustom MPA",

    'summary': "Modul Kustomisasi untuk MPA",

    'description': """
Modul Kustom untuk Mitra Prima Anugerah (MPA)
    """,

    'author': "Abajoo",
    'website': "https://abajoo.co.id/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','account_accountant','maintenance','stock','purchase_request','purchase','hr','request_part_list', 'auto_transfer_move','account','account_asset','abj_cash_advance'],
    # request_part_list, auto_transfer_move itu modul kustom dari Abajoo


    # always loaded
    'data': [
        'security/security.xml',
        'security/security_rules.xml',
        'security/ir.model.access.csv', 
        'security/menu_item.xml',
        'views/sequence_mr.xml',
        'views/sequence.xml',
        'views/sequence_asset_number.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/maintenance_request.xml',
        'views/request_part_list.xml',
        'views/stock_picking.xml',
        'views/purchase_order.xml',
        'views/equipment.xml',
        'views/partlist.xml',
        'views/purchase_request.xml',
        'views/equipment_location.xml',
        'views/assets.xml',
        'views/product_template.xml',
        'views/account_asset_group.xml',
        'views/defect_category.xml',
        'views/inprogress_status.xml',
        'views/stock_move_line.xml',
        'views/bank_view.xml',
        'views/payment_term.xml',
        'report/rpl.xml',
        'report/rpl_report_action.xml',
        'report/purchase_request_inherit.xml',
        'report/custom_delivery_slip.xml',
        'report/workorder.xml',
        'report/workorder_report_action.xml',
        'report/warranty_report_action.xml',
        'report/warranty.xml',
        'report/purchase_order_report.xml',
         

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'mpa_custom_modul/static/src/components/**/*',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'icon': '/mpa_custom_modul/static/description/mpa_icon.jpg',
}

