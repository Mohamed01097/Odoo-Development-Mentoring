{
    'name': "Sale Training Service",

    'summary': "Adds training quantity and review evaluation to sales orders",


    'category': 'Sales',
    'version': '0.1',


    'depends': [
        'sale_management',
    ],


    'data': [
        # 'security/security_groups.xml',
        'views/sale_order_inherit_views.xml'
    ],

    'application': True,
    'installable': True,
    "license": "LGPL-3",

}

