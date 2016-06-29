# -*- coding: utf-8 -*-
# (c) 2016 Serv. Daniel Rodriguez Lijo
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import models, api, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    contract_from_sale = fields.Boolean(
        string='Make a new contract from this Quotation',
        help="If this field is check, when Quotation pass from draft to "
        "Sale order, a associated contract will de created")

    def generate_new_contract(self):
        invoice_lines = []
        contract_obj = self.env['account.analytic.account']
        for line in self.order_line:
            invoice_lines.append((0, 0, {
                'product_id': line.product_id.id,
                'name': line.name,
                'quantity': line.product_uos_qty,
                'uom_id': line.product_uom.id,
                'price_unit': line.price_unit,
                'discount': line.discount
            }))

        contract_values = {
            'name': self.partner_id.name + "-" + self.name,
            'partner_id': self.partner_id.id,
            'company_id': self.company_id.id,
            'recurring_invoices': True,
            'recurring_invoice_line_ids': invoice_lines,
            'related_sale_order_id': self.id,
            'type': 'contract'
        }
        contract_obj.create(contract_values)

    @api.multi
    def action_button_confirm(self):
        super(SaleOrder, self).action_button_confirm()
        if self.contract_from_sale:
            self.generate_new_contract()
        return True
