from odoo import _, fields, models
from odoo.exceptions import AccessError, UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    approval_state = fields.Selection([
        ('not_requested', 'Not Requested'),
        ('waiting', 'Waiting Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='not_requested', required=True, readonly=True, copy=False, tracking=True)
    approved_by_id = fields.Many2one('res.users', readonly=True, copy=False)
    approved_date = fields.Datetime(readonly=True, copy=False)


    def _notify_approvers(self):
        for record in self:
            group = self.env.ref('mentorship_approval19.group_mentorship_approval')
            for user in group.user_ids:
                record.activity_schedule(
                    'mail.mail_activity_data_todo',
                    user_id=user.id,
                    summary='Approval Required',
                    note=f'Approval is required for {record.display_name}.',
                )
    def _approval_reset(self):
        return {'approval_state': 'not_requested', 'approved_by_id': False, 'approved_date': False}

    def write(self, vals):
        # Invalidate approvals when any pricing input changes, including order lines.
        if 'order_line' in vals and 'approval_state' not in vals:
            vals = dict(vals, **self._approval_reset())
        return super().write(vals)

    def _approval_check_manager(self):
        if not self.env.user.has_group('mentorship_approval19.group_mentorship_approval'):
            raise AccessError(_('Only Sales Managers may approve or reject quotations.'))

    def action_request_approval(self):
        for order in self:
            if order.state not in ('draft', 'sent'):
                raise UserError(_('Only quotations can request approval.'))
            if order.amount_total <= 10000:
                raise UserError(_('Approval is only required above 10,000.'))
            if order.approval_state == 'approved':
                raise UserError(_('This quotation is already approved.'))
        self.write({'approval_state': 'waiting', 'approved_by_id': False, 'approved_date': False})
        self._notify_approvers()
        return True

    def action_approve_mentorship(self):
        self._approval_check_manager()
        for order in self:
            if order.state not in ('draft', 'sent') or order.approval_state != 'waiting':
                raise UserError(_('Only pending quotations can be approved.'))
        self.write({'approval_state': 'approved', 'approved_by_id': self.env.user.id,
                    'approved_date': fields.Datetime.now()})
        return True

    def action_reject_mentorship(self):
        self._approval_check_manager()
        for order in self:
            if order.state not in ('draft', 'sent') or order.approval_state != 'waiting':
                raise UserError(_('Only pending quotations can be rejected.'))
        self.write({'approval_state': 'rejected', 'approved_by_id': False, 'approved_date': False})
        return True

    def action_confirm(self):
        for order in self:
            if order.amount_total > 10000 and order.approval_state != 'approved':
                raise UserError(_('This quotation requires Sales Manager approval before confirmation.'))
        return super().action_confirm()
