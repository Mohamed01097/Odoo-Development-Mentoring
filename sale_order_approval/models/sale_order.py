from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrderApproval(models.Model):
    _inherit = "sale.order"

    approval_state = fields.Selection([
        ('not_requested', 'Not Requested'),
        ('waiting_approval', 'Waiting_Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='not_requested', readonly=True, tracking=True, copy=False)

    approved_by_id = fields.Many2one(
        'res.users',
        string="Approved By",
        copy=False,
        readonly=True
    )

    approved_date = fields.Datetime(
        string="Date of Approval",
        readonly=True,
        copy=False
    )


    def action_confirm(self):
      
      for order in self:
          if order.amount_total > 10000 and order.approval_state != 'approved':
            raise ValidationError("you must have approve")
          order.write({
            'approval_state': 'not_requested',
          })

      return super().action_confirm()


    def requested_approval_button(self):
     for order in self:
        if order.amount_total <= 10000:
            raise ValidationError("approve is only for orders more than 10000")
        order.write({
            'approval_state': 'waiting_approval',
          })

    def approved_button(self):

        if not self.env.user.has_group('sale_order_approval.sales_manager_group'):
            raise ValidationError("You are not authorized to approve this order")
        for order in self:
         order.write({
            'approval_state': 'approved',
            'approved_by_id': self.env.user.id,
            'approved_date': fields.Datetime.now(),
                })


    def rejected_button(self):
       if not self.env.user.has_group('sale_order_approval.sales_manager_group'):
        raise ValidationError("You are not authorized to reject this order")
       for order in self:
        order.write({
            'approval_state': 'rejected',
            'approved_by_id': False,
            'approved_date': False,
           })

    def write(self, vals):
        res = super().write(vals)
        for order in self:
            # لو الأوردر كان واخد موافقة، واليوزر عدل في بنود المنتجات
            if order.approval_state == 'approved' and 'order_line' in vals:
                order.approval_state = 'not_requested'
                order.approved_by_id = False
                order.approved_date = False
        return res
