# IPPBX Quotation Portal Templates

Adds a **Quotation Design** dropdown on the sale order form. Depending on what's
selected, the customer portal preview ("Preview" button / emailed link) renders
one of several industry-specific page designs instead of - or in addition to -
the stock Odoo layout.

## Before installing (important)

`portal_sale_order_switch.xml` inherits the core view `sale.sale_order_portal_template`
and expects it to still be the **stock Odoo 18 arch**. If it was hand-edited
directly (e.g. the earlier "non-profit.xml" was pasted into it through the
portal/view code editor), the xpath target (`row o_portal_sale_sidebar`) won't
match and this module will fail to install/upgrade.

Fix: Settings > Technical > Views > search "Sale Order Portal Template" (or the
XML ID `sale.sale_order_portal_template`) > **Reset to default arch**. Nothing
is lost - that same design is now the "Non Profit Proposal" selectable option
(`views/template_modern_digital_workplace.xml`), seeded as a `quotation.template`
record. It's fine to leave the hand-edited view as-is until you're ready to
install this module - just reset it right before installing, not before.

## What's in the box

- `quotation.template` model - the list of selectable designs, managed at
  Sales > Configuration > Quotation Templates. Add more later without touching
  code: create a QWeb template, then a record pointing `view_id` at it.
- `sale.order.quotation_template_id` - the field on the quotation form, defaults
  to whichever `quotation.template` record has `is_default_selection = True`.
  Note this is a *different* flag from `is_default`: `is_default` marks the one
  row that means "render the genuine stock Odoo layout" (used by the routing
  view's fallback branch); `is_default_selection` marks which row a brand-new
  quotation starts with. They can point at different rows.
- Dropdown values (in this order): **Default Odoo**, General Proposal, Law
  Proposal, Medical Proposal, Religious Proposal, Phone System, Non Profit
  Proposal.
- `views/template_general_proposal.xml`, `template_law.xml`, `template_medical.xml`,
  `template_religious.xml`, `template_phone_system.xml` - generated from the raw
  HTML proposals. Customer/proposal-number/salesperson/valid-until/total, and the
  Products table (name, quantity, unit price, amount, taxes, total), are all
  dynamic - bound to the real `sale_order` and `sale_order.order_line`, same
  pattern as Non Profit Proposal. Only the savings/benchmark-comparison callout
  (estimated annual savings vs. a "typical" monthly cost) stays a **static
  placeholder number**, since there's no field yet for the customer's actual
  current phone bill to compare against - clearly commented in each file.
- `views/template_modern_digital_workplace.xml` ("Non Profit Proposal" in the
  dropdown) - the non-profit.xml design, unchanged, including its dynamic
  order-line pricing table. Left as-is per request.
- `views/portal_sale_order_switch.xml` - the routing view. Picks the custom
  template via `t-call="#{sale_order.quotation_template_id.view_id.key}"` when
  one is set and not flagged as `is_default`; otherwise falls through to the
  exact stock Odoo markup (kept verbatim in the `t-else`).
- `post_init_hook` (in `__init__.py`) - runs once at install. Every pre-existing
  `sale.order` gets a brand-new, empty `quotation_template_id` field; left alone
  the routing view would fall back to stock Odoo for all of them, silently
  changing how already-sent quotations look (they currently all render as Non
  Profit Proposal, since that's what's hand-edited into the DB today). The hook
  backfills `quotation_template_id = Non Profit Proposal` on every order that
  doesn't have one yet, so nothing visually changes for quotations already sent
  or signed. Only new quotations created after install use `is_default_selection`.

## Known simplification from the source files

The boss's "Phone System" file (`Phone System · AI Calling · Business
Applications.html`) turned out to be byte-for-byte identical to
`Medical_Proposal_Template.html` (only a trailing whitespace difference).
It's included as its own selectable template (re-skinned with its own accent
color) so all 7 dropdown entries exist and work, but its content is currently
a duplicate of Medical Proposal - swap `views/template_phone_system.xml`'s
content for the real Phone System copy whenever the boss sends distinct text.

## Next steps (not done yet, by agreement)

1. Get distinct content for the "Phone System" template (see above) - currently
   a re-skinned duplicate of Medical Proposal.
2. Decide if a real field/comparison basis should replace the static
   savings-callout numbers in the 5 non-Non-Profit templates, or if that stays
   illustrative permanently.
3. Decide if/how the PDF report (Print / emailed attachment) should also follow
   `quotation_template_id` - out of scope for this pass (portal-only).
