from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

# Manger group that has the rights to confirm high budget purchase orders
MANAGER_GROUP = 'purchase_budget_control.group_purchase_budget_manager'

class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'


    budget_level = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ],
        string='Budget Level', copy=False,
        compute='_compute_budget_level', index=True
    )

    requires_manager = fields.Boolean(
        compute='_compute_budget_level'
    )



    # Compute Methods
    @api.depends('amount_total')
    def _compute_budget_level(self):
        """Compute budget level based on Total Amount of Purchase Order
            less than 5K => Low,
            Between  5K : 25 K  and less than 25K => Medium
            More than or equal to 25K => High
        """
        """High Budget Orders require manager confirmation"""
        for order in self:
            # Order Total Amount cannot be less than zero
            if order.amount_total < 0:
                raise ValidationError(_(
                    "Total Amount can not be negative."
                ))

            elif order.amount_total < 5000:
                order.budget_level = 'low'

            elif order.amount_total < 25000:
                order.budget_level = 'medium'

            else:
                order.budget_level = 'high'

            # High Budget Orders require manager confirmation
            order.requires_manager = (
                    order.budget_level == 'high'
            )

    def _check_is_manager(self):
        """Check the current user hasManger group that has the rights to confirm high budget purchase orders"""
        return self.env.user.has_group(MANAGER_GROUP)


    def get_budget_summary(self):
        """Method return budget summary as a list of dictionaries"""

        """Containing Info : Order Reference, Vendor, Total Amount,
        Budget Level, Is purchase order Requires Manager ?
        """

        budget_summary = [{
            'order_ref': order.name,
            'order_vendor': order.partner_id.name,
            'total_amount': order.amount_total,
            'budget_level': order.budget_level,
            'requires_manager': order.requires_manager,
        } for order in self]

        return budget_summary




    def button_confirm(self):
        for order in self:
            """You cannot confirm purchase order without order lines"""

            if not order.order_line:
                raise ValidationError(
                    _(
                        "You can not confirm order without"
                        "order lines"
                    )
                )

            """Check if order requires manager confirmation and if it requires manager
            confirmation check if the current user is manager t 
            """
            """Manager Only Can complete this process with the last conditions"""

            if order.requires_manager and not order._check_is_manager():

                raise ValidationError(_(
                    f"{self.env.user.name} Can not confirm this purchase order.\n"
                    "Only Purchase Credit Manager can confirm "
                    "the high budget purchase orders."
                ))

        return super().button_confirm()
