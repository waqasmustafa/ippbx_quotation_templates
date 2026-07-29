from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    quotation_template_id = fields.Many2one(
        'quotation.template',
        string='Quotation Design',
        default=lambda self: self.env['quotation.template'].search([('is_default_selection', '=', True)], limit=1),
        help="Controls which portal page design the customer sees when previewing "
             "or signing this quotation online.",
    )
