from odoo import models, fields, api,_
from odoo.exceptions import AccessError

class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'helpdesk_ticket.helpdesk_ticket'
    _inherit = ['mail.activity.mixin','mail.thread']

    name = fields.Char()
    employee_id = fields.Many2one('hr.employee', required=True, tracking=True)
    requester_id = fields.Many2one('res.users', default=lambda self: self.env.user, required=True, readonly=True, copy=False)
    manager_id = fields.Many2one('res.users', readonly=True, tracking=True)
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company, required=True, readonly=True)
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id', store=True)
    amount = fields.Monetary(required=True, tracking=True)
    reason = fields.Text(required=True)
    rejection_reason = fields.Text(readonly=True, copy=False)
    state = fields.Selection([
        ('draft', 'Draft'), ('submitted', 'Submitted'),
        ('approved', 'Approved'), ('rejected', 'Rejected'), ('paid', 'Paid'),
    ], default='draft', required=True, tracking=True, copy=False)

    @api.onchange('employee_id')
    def _onchange_employee(self):
        for rec in self:
            if rec.employee_id:
                rec.manager_id = rec.employee_id.parent_id.user_id or False

    def action_submit(self):
        for rec in self:
            rec.activity_schedule(
                'mail.mail_activity_data_todo',
                user_id=rec.manager_id.id,
                summary=f'Employee {rec.employee_id.name} has new request of {rec.reason}',
                note='New Request',
            )
            rec.state = "submitted"

    def action_approve(self):
        finance_group =  self.env.ref('helpdesk_ticket.group_advance_finance')
        user_id = False
        for user in finance_group.user_ids:
             user_id = user.id
        for rec in self:
            rec.activity_schedule(
                'mail.mail_activity_data_todo',
                user_id=user_id,
                summary=f'Employee {rec.employee_id.name} has new request of {rec.reason}',
                note='New Request',
            )
            rec.state = "approved"

    def action_open_reject_wizard(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window', 'name': _('Reject Advance'),
            'res_model': 'expense.advance.reject.wizard', 'view_mode': 'form',
            'target': 'new', 'context': {'default_advance_id': self.id},
        }

    def action_paid(self):
        for rec in self:
            rec.state = "paid"



class MailActivity(models.Model):
    _inherit = 'mail.activity'

    def unlink(self):
        if not self.env.user.has_group(
                'helpdesk_ticket.mail_activity_can_del'
        ):
            raise AccessError(
                _("You are not allowed to delete activities.")
            )

        return super().unlink()

class ResUsers(models.Model):
    _inherit = 'res.users'

    is_finance = fields.Boolean(default=False)