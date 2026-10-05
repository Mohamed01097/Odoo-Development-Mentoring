from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    test = fields.Boolean()

    def action_confirm(self):
        res = super().action_confirm()
        if not self.user_id:
            raise ValidationError("User not set")
        return res

    def get_sale_orders(self):
        orders = self.env['sale.order'].search([],limit=2)
        orders = self.env['sale.order'].browse(orders.ids)
        print(orders)
