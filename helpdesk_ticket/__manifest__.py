{
    'name': "Helpdesk Expense Ticket",

    'summary': "Helpdesk Expense Ticket",


    'author': "Islam Mahdy",


    'category': 'HR',
    'version': '0.1',

    'depends': [
        'base', 'hr', 'mail'
    ],

    'data': [

        'security/security.xml',
        'security/ir.model.access.csv',


        'views/expense_ticket_views.xml',

        # 'wizard/expense_advance_reject_views.xml',

    ],


}

