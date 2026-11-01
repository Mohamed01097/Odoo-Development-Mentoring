from odoo import models, fields, api


class equipment_request(models.Model):
    _name = 'equipment.request'

    title = fields.Char()
    equipment = fields.Char()
    quantity = fields.Integer()
    justification = fields.Text()
    priority = fields.Selection([
        ('low', 'Low'),
    ])
    owner_id = fields.Many2one('res.users')
    company_id = fields.Many2one('res.company')
    manager_note = fields.Text(groups="equipment_request.Manger_group")

    _check_quantity = models.Constraint(
        'CHECK(quantity > 0)',
        'Quantity must be greater than 0!'
    )