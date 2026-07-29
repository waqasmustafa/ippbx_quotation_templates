from . import models


def post_init_hook(env):
    """Preserve the current portal look for quotations that already existed
    before this module was installed.

    sale.sale_order_portal_template was previously hand-edited (directly in
    the database) to render the Non Profit Proposal design for every
    quotation. quotation_template_id is a brand-new field, so every
    pre-existing sale.order has it empty - left alone, the routing view
    would fall back to the stock Odoo layout for all of them, silently
    changing how already-sent quotations look. Point every order that
    doesn't have a design yet at Non Profit Proposal so nothing changes for
    what customers have already seen or signed. Only new quotations created
    from now on use quotation.template's "Default For New Quotations" row.
    """
    template = env.ref(
        'ippbx_quotation_templates.quotation_template_modern_digital_workplace',
        raise_if_not_found=False,
    )
    if not template:
        return
    orders = env['sale.order'].search([('quotation_template_id', '=', False)])
    if orders:
        orders.write({'quotation_template_id': template.id})
