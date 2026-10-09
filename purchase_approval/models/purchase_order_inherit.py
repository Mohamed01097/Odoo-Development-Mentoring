from odoo import fields, models, api
from odoo.exceptions import ValidationError



class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'


    approval_state = fields.Selection([
        ('not requested', 'Not Requested'),
        ('waiting approval', 'Waiting Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default="not requested", string='Approval State', readonly=True)

    confirmed_user = fields.Many2one(
        'res.users', string='Confirmed User', readonly=True, tracking=True
    )
    confirm_date = fields.Datetime(
        string='Confirm Date', readonly=True, tracking=True
    )


    def allowed_state(self, new_state):

        allowed = {
            'waiting approval': 'not requested',
            'approved': 'waiting approval',
            'rejected': 'waiting approval',
        }

        for rec in self:
            if allowed.get(new_state) != rec.approval_state:
                raise ValidationError(
                    f"{new_state} is not allowed, from {rec.approval_state}"
                )


    def action_request_approval(self):
        for order in self:

            order.allowed_state('waiting approval')

            order.approval_state = 'waiting approval'


    def action_approve(self):
        for order in self:
            order.allowed_state('approved')

            order.approval_state = 'approved'


    def action_reject(self):
        for order in self:
            order.allowed_state('rejected')

            order.approval_state = 'rejected'


    def button_confirm(self):

        for order in self:

            if (
                    order.amount_total > 15000 and
                    order.approval_state != 'approved'

            ):
                raise ValidationError(
                    "To Confirm Order with Total more than 15K; "
                    "You need Approved from Manager."
                )

            order.confirmed_user = self.env.user.id
            order.confirm_date = fields.Datetime.now()


        return super().button_confirm()



    def write(self, vals):
        for rec in self:

            if (
                    'order_line' in vals
                and
                    rec.approval_state == 'approved'
            ):
                rec.approval_state = 'not requested'

        return super().write(vals)

