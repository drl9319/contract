# -*- coding: utf-8 -*-
from openerp import models, api, fields, _


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    related_sale_order_id = fields.Many2one(
        comodel_name='sale.order',
        string='Pedido de venta')
