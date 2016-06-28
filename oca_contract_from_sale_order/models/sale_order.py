# -*- coding: utf-8 -*-
from openerp import models, api, fields, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    contract_from_sale = fields.Boolean(
        string='Generar contrato desde este presupuesto',
        help="Si usted marca esta casilla cuando el presupuesto pase a ser "
        "pedido de venta se generara automaticamente un contrato con estos datos")

    contract_type = fields.Selection(
        [('alquiler_material', 'Alquiler y Material'),
         ('hardware_software', 'Hardware y software')],
        string='Tipo de contrato',)


    def generate_new_contract(self):
        invoice_lines = []
        contract_obj = self.env['account.analytic.account']
        for line in self.order_line:
            if line.product_id.obligatory_serie_number:
                for unit in range(0, int(line.product_uom_qty)):
                    invoice_lines.append((0,0,{
                                'product_id': line.product_id.id,
                                'name': line.name,
                                'quantity': 1,
                                'uom_id': line.product_uom.id,
                                'price_unit': line.price_unit,
                                'discount': line.discount
                                }))
            else:
                invoice_lines.append((0,0,{
                            'product_id': line.product_id.id,
                            'name': line.name,
                            'quantity': line.product_uos_qty,
                            'uom_id': line.product_uom.id,
                            'price_unit': line.price_unit,
                            'discount': line.discount
                            }))

        contract_values = {
            'name': self.partner_id.name+"-"+self.name,
            'partner_id': self.partner_id.id,
            'contract_type': self.contract_type,
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
