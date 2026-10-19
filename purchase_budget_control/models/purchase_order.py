# -*- coding: utf-8 -*-
"""Mentor reference: Session 02 — Python & OOP inside Odoo."""

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    budget_level = fields.Selection(
        selection=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
        string='Budget Level',
        compute='_compute_budget_level',
        store=True,
        readonly=True,
    )
    requires_manager = fields.Boolean(
        string='Requires Manager',
        compute='_compute_budget_level',
        store=True,
        readonly=True,
    )

    @api.depends('amount_total')
    def _compute_budget_level(self):
        for order in self:
            amount = order.amount_total
            if amount < 5000:
                order.budget_level = 'low'
            elif amount <= 25000:
                order.budget_level = 'medium'
            else:
                order.budget_level = 'high'
            order.requires_manager = order.budget_level == 'high'

    def get_budget_summary(self):
        """Return one order's summary; caller must supply exactly one record."""
        self.ensure_one()
        return {
            'order_name': self.name,
            'vendor_name': self.partner_id.name,
            'total_amount': self.amount_total,
            'budget_level': self.budget_level,
            'requires_manager': self.requires_manager,
        }

    def button_confirm(self):
        # Validate every selected order BEFORE calling the standard workflow.
        # This makes the check work for UI buttons and server-side/API calls.
        is_manager = self.env.user.has_group('purchase.group_purchase_manager')
        for order in self:
            if not order.order_line:
                raise UserError(_("Cannot confirm an order without order lines."))
            if order.amount_total > 25000 and not is_manager:
                raise UserError(_("Only a manager can confirm orders above 25000."))
        return super().button_confirm()
