from odoo import fields, models, _
from odoo.exceptions import UserError


class ExpenseAdvanceRejectWizard(models.TransientModel):
    _name = 'expense.advance.reject.wizard'
    _description = 'Reject Expense Advance'

    advance_id = fields.Many2one('helpdesk.ticket', required=True, readonly=True)
    reason = fields.Text(required=True)

    def action_confirm_reject(self):
        self.ensure_one()
        advance = self.advance_id
        # advance.check_access('write')
        # advance._check_manager()
        if not (self.reason or '').strip():
            raise UserError(_('A rejection reason is required.'))
        advance.write({'rejection_reason': self.reason.strip()})
        advance.state = 'rejected'
        # advance._set_state('rejected')
        # advance._close_review_activities()
        advance.message_post(body=_('Advance rejected. Reason: %s') % self.reason.strip())
        return {'type': 'ir.actions.act_window_close'}
