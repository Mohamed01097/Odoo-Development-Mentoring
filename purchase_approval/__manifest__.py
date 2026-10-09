{
    'name': "Purchase Approvel",

    'sequence': -10,

    'summary': "Purchase Approval Module to approve purchase orders with a big Values",

    'author': "Islam Mahdy",

    'category': 'Education',
    'version': '0.1',

    'depends': [
        'base', 'purchase'
    ],


    'data': [
        'views/purchase_order_inherit.xml',
    ],

    'application': True,
    'installable': True,

}

