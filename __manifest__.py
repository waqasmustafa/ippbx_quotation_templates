{
    'name': 'IPPBX Quotation Portal Templates',
    'version': '18.0.1.0.0',
    'summary': 'Pick a portal design (General, Law, Medical, Non Profit, Phone System, Religious) per quotation',
    'description': """
Adds a "Quotation Design" field on the sale order so each quotation can render
a different portal (customer preview) page - one of several industry designs,
or the stock Odoo layout by default.

Templates are managed under Sales > Configuration > Quotation Templates
(quotation.template model), so new designs can be added without code changes.
""",
    'author': 'Waqas Mustafa',
    'category': 'Sales',
    'depends': ['sale', 'portal'],
    'data': [
        'security/ir.model.access.csv',
        'views/quotation_template_views.xml',
        'views/sale_order_views.xml',
        'views/template_general_proposal.xml',
        'views/template_law.xml',
        'views/template_medical.xml',
        'views/template_religious.xml',
        'views/template_phone_system.xml',
        'views/template_modern_digital_workplace.xml',
        'views/template_it_general.xml',
        'views/template_it_law.xml',
        'views/template_it_medical.xml',
        'views/template_it_religious.xml',
        'data/quotation_template_data.xml',
        'views/portal_sale_order_switch.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
    'post_init_hook': 'post_init_hook',
}
