{
    'name': "Purchase Order Budget Control",

    'summary': "Purchase Order Budget Control; "
               "to control company purchase orders before confirming them.",

        'description' : """
Purchase Order Budget Control
==================================
* To control company purchase orders before confirming them.
* Classify all purchase orders according to their total amount.
* Big purchase orders cannot be confirmed without purchase manager.


""",

    'depends': [
        'purchase'
    ],

    'data': [
        'security/security_groups.xml',
        'views/purchase_order_inherit_views.xml'

    ],

    'installable': True,

}

