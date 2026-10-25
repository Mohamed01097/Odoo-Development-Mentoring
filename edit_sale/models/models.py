from odoo import models, fields, api
from odoo.exceptions import ValidationError


class edit_sale(models.Model):
    _inherit = 'sale.order'
    training_total_quantity = fields.Float(compute='_compute_training_total_quantity' ,readonly=True ,store=True)
    training_customer_phone = fields.Char(string='phone', related='partner_id.phone', readonly=True)
    training_review_limit = fields.Monetary(default='5000')
    training_needs_review = fields.Boolean(default=False ,readonly=True )

    @api.depends('order_line.product_uom_qty', 'order_line.display_type')
    def _compute_training_total_quantity(self):
        for record in self:
            record.training_total_quantity = sum(
                line.product_uom_qty
                for line in record.order_line
                if not line.display_type
            )




    @api.constrains('training_review_limit')
    def check_limits(self):
        for record in self:
            if record.training_review_limit < 0:
                raise ValidationError("Training review_limit cannot be less than 0")

    @api.onchange('training_review_limit')
    def check_limit(self):
        if self.training_review_limit < 0:
            return {
                'warning': {
                    'title': 'Stoppppp',
                    'message': 'limit cannot be negative',
                }
            }

    def action_training_evaluate_review(self):
        for record in self:
            comparison = record.currency_id.compare_amounts(record.amount_total, record.training_review_limit)


            if comparison > 0:
                record.training_needs_review = True
            else:
                record.training_needs_review = False


