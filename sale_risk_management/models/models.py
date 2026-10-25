from odoo import models, fields, api ,_
from odoo.exceptions import UserError

class sale_risk_management(models.Model):
    _inherit = "sale.order"
    risk_level = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),

    ],readonly=True,copy=False,compute="_compute_risk_level",store=True )

    requires_manager= fields.Boolean()



    @api.depends('amount_total')
    def _compute_risk_level(self):
     for order in self:
         if order.amount_total < 10000:
             order.risk_level = 'low'
         if order.amount_total < 50000 and order.amount_total > 10000:
             order.risk_level = 'medium'
         if order.amount_total > 50000:
             order.risk_level = 'high'



    @api.onchange('requires_manager')
    def show_require_manager(self):
        for rec in self:
           if rec.risk_level == 'high':
              if not self.env.user.has_group('sale_order_approval.sales_manager_group'):
                    raise UserError(_("Only Sales Managers can perform this action"))


    def action_confirm(self):
         for record in self:
            if not record.order_line:
                raise UserError(_("You must have an at least one order to perform this action."))
         return super().action_confirm()

    def get_risk_level(self):
        data=[{
            'name':order.name,

        }for order in self]
        return data

    def action_show_risk_data(self):
        for record in self:
            data = record.get_risk_level()
            # يمكنك طباعتها في تيرمينال السيرفر للتأكد
            print(data)
        return True