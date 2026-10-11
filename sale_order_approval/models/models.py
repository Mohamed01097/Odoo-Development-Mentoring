from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrderApproval(models.Model):
    _inherit = "sale.order"

    approval_state = fields.Selection([
     ('not_requested', 'Not Requested'),
     ('waiting_approval', 'Waiting_Approval'),
     ('approved','Approved'),
     ('rejected','Rejected'),
     ],default='not_requested')

    def action_confirm(self):
      res=super().action_confirm()
      if sum(self.order_line.mapped('price_subtotal')) >= 10000:
          raise ValidationError("you must have approve")
      return res

    def requested_approval_button(self):
        pass

    def write(self, vals):

        if self.approval_state == 'approved':
            raise ValidationError("you can't update the order after approval")
        return super().write(vals)
