from odoo import models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def write(self, vals):
        orders = self.mapped('order_id') if set(vals) & {'product_id', 'product_uom_qty', 'price_unit', 'discount', 'tax_id'} else self.env['sale.order']
        result = super().write(vals)
        if orders:
            orders.write(orders._approval_reset())
        return result

    def create(self, vals_list):
        lines = super().create(vals_list)
        orders = lines.mapped('order_id')
        if orders:
            orders.write(orders._approval_reset())
        return lines

    def unlink(self):
        orders = self.mapped('order_id')
        result = super().unlink()
        if orders:
            orders.write(orders._approval_reset())
        return result


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    def write(self, vals):
        orders = self.mapped('order_id') if set(vals) & {'product_id', 'product_qty', 'price_unit', 'taxes_id', 'discount'} else self.env['purchase.order']
        result = super().write(vals)
        if orders:
            orders.write(orders._approval_reset())
        return result

    def create(self, vals_list):
        lines = super().create(vals_list)
        orders = lines.mapped('order_id')
        if orders:
            orders.write(orders._approval_reset())
        return lines

    def unlink(self):
        orders = self.mapped('order_id')
        result = super().unlink()
        if orders:
            orders.write(orders._approval_reset())
        return result
