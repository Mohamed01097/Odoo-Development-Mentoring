from odoo import api, fields, models, _

class SaleOrderShell(models.Model):
    _inherit = 'sale.order'


    def action_about_env(self):
        env_vals = {
            'user_id': self.env.user.id,
            'user': self.env.user,
            'user_name': self.env.user.name,
            'company_id': self.env.company.id,
            'context': self.env.context,
        }
        print(env_vals)


    def action_about_orders_info(self):
        orders = self.search([])

        vals = {
            'model_name': orders._name,
            'orders_num': len(orders),
            'orders': orders,
            'orders_ids': orders.ids,

        }

        print(vals)
