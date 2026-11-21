from odoo import models, fields, api
from odoo.exceptions import ValidationError

class edit_sales(models.Model):
     _inherit = 'sale.order'
     _description = 'edit_sales.edit_sales'

     customer_note = fields.Text(string='Customer Note')
     delivery_priority = fields.Selection(
         [
             ('normal', 'Normal'),
             ('urgent', 'Urgent'),
             ('very_urgent', 'Very Urgent')
         ]
     )
     custom_discount = fields.Float(string='Custom Discount')
     discount_amount = fields.Float(string='Discount Amount' ,compute='_compute_discount_amount')
     minimum_order_amount =fields.Float(default=1000.0)

     @api.depends('custom_discount','amount_untaxed')
     def _compute_discount_amount(self):
         for order in self:
             order.discount_amount = order.amount_untaxed * order.custom_discount/100

     @api.constrains('amount_untaxed')
     def _compute_amount_untaxed(self):
         for order in self:
             if order.amount_untaxed < order.minimum_order_amount:
                 raise ValidationError('Minimum order amount cannot be less than minimum order amount')


     def Ahmed_essam(self):
         pass