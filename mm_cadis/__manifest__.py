# -*- coding: utf-8 -*-
{
    'name': "mm_cadis",

    'summary': """
       Modulo con customizaciones para
       Grupo CADIS""",

    'description': """
    Modulo con customizaciones para
       Grupo CADIS
    """,

    'author': "Mit-Mut",
    'website': "https://www.mit-mut.com",
    'license': 'OPL-1',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management','contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/inherit_sale_order_views.xml',
        'views/inherit_res_partner_views.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
