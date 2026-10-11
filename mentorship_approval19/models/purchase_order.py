from odoo import _, fields, models
from odoo.exceptions import AccessError, UserError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    approval_state = fields.Selection([
        ('not_requested', 'Not Requested'),
        ('waiting', 'Waiting Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='not_requested', required=True, readonly=True, copy=False, tracking=True)
    approved_by_id = fields.Many2one('res.users', readonly=True, copy=False)
    approved_date = fields.Datetime(readonly=True, copy=False)

    def _approval_reset(self):
        return {'approval_state': 'not_requested', 'approved_by_id': False, 'approved_date': False}

    def write(self, vals):
        if 'order_line' in vals and 'approval_state' not in vals:
            vals = dict(vals, **self._approval_reset())
        return super().write(vals)

    def _approval_check_manager(self):
        if not self.env.user.has_group('purchase.group_purchase_manager'):
            raise AccessError(_('Only Purchase Managers may approve or reject purchase orders.'))

    def action_request_approval(self):
        for order in self:
            if order.state not in ('draft', 'sent'):
                raise UserError(_('Only draft RFQs can request approval.'))
            if order.amount_total <= 15000:
                raise UserError(_('Approval is only required above 15,000.'))
            if order.approval_state == 'approved':
                raise UserError(_('This RFQ is already approved.'))
        self.write({'approval_state': 'waiting', 'approved_by_id': False, 'approved_date': False})
        return True

    def action_approve_mentorship(self):
        self._approval_check_manager()
        for order in self:
            if order.state not in ('draft', 'sent') or order.approval_state != 'waiting':
                raise UserError(_('Only pending RFQs can be approved.'))
        self.write({'approval_state': 'approved', 'approved_by_id': self.env.user.id,
                    'approved_date': fields.Datetime.now()})
        return True

    def action_reject_mentorship(self):
        self._approval_check_manager()
        for order in self:
            if order.state not in ('draft', 'sent') or order.approval_state != 'waiting':
                raise UserError(_('Only pending RFQs can be rejected.'))
        self.write({'approval_state': 'rejected', 'approved_by_id': False, 'approved_date': False})
        return True

    def button_confirm(self):
        for order in self:
            if order.amount_total > 15000 and order.approval_state != 'approved':
                raise UserError(_('This purchase order requires Purchase Manager approval before confirmation.'))
        return super().button_confirm()
