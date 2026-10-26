from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    training_total_quantity = fields.Float(
        compute='_compute_training_total_quantity', store=True, index=True,
        string='Training Total Quantity', copy=False, tracking=True,
    )

    training_customer_phone = fields.Char(
        related='partner_id.phone',
        string='Customer Phone',
    )

    training_review_limit = fields.Monetary(
        default=5000.0, currency_field="currency_id",
        string='Training Review Limit', copy=False, tracking=True
    )

    training_needs_review = fields.Boolean(
        default=False, index=True, copy=False, tracking=True,
    )


    _sql_constraints = [
        (
            'non_negative_training_review_limit_check',
            'CHECK (training_review_limit >= 0)',
            'Training customer limit must be greater than or equal to 0.',
        ),

        (
            'non_negative_training_total_quantity_check',
            'CHECK (training_total_quantity >= 0)',
            'Training total quantity limit must be greater than or equal to 0.',
        ),
    ]


    @api.onchange('training_review_limit')
    def onchange_training_limit_(self):
        if self.training_review_limit < 0:
            return {
                    'warning': {
                        'title': "warning",
                        'type': 'notification',
                        'message': _("Review limit is negative")
                }
            }


    # From GPT : I do not understand the requirement
    @api.depends(
        "order_line.product_uom_qty",
        "order_line.display_type",
    )
    def _compute_training_total_quantity(self):
        for order in self:
            product_lines = order.order_line.filtered(
                lambda line: not line.display_type
            )

            order.training_total_quantity = sum(
                product_lines.mapped("product_uom_qty")
            )


    def action_training_evaluate_review(self):
        for order in self:
            order.training_needs_review = (
                order.amount_total < order.training_review_limit
            )
