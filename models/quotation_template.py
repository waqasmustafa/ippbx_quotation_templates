from odoo import fields, models


class QuotationTemplate(models.Model):
    _name = 'quotation.template'
    _description = 'Quotation Portal Template'
    _order = 'sequence, id'

    name = fields.Char(required=True, translate=True)
    code = fields.Char(
        required=True,
        help="Technical key for this design, e.g. 'general_proposal'. Only used internally.",
    )
    is_default = fields.Boolean(
        string='Odoo Default Layout',
        help="When checked, the quotation renders with the stock Odoo portal layout "
             "instead of a custom view, regardless of what is set in View.",
    )
    is_default_selection = fields.Boolean(
        string='Default For New Quotations',
        help="The template pre-filled on newly created quotations. Should be set "
             "on exactly one record; this is independent from 'Odoo Default Layout', "
             "which instead marks the row that means 'use the stock Odoo layout'.",
    )
    view_id = fields.Many2one(
        'ir.ui.view',
        string='Portal Content View',
        help="QWeb view rendered on the customer portal for quotations using this design. "
             "Not needed when 'Odoo Default Layout' is checked.",
    )
    active = fields.Boolean(default=True)
    sequence = fields.Integer(default=10)

    _sql_constraints = [
        ('code_uniq', 'unique(code)', 'The technical code of a quotation template must be unique.'),
    ]
