# -*- coding: utf-8 -*-
# (c) 2016 Serv. Daniel Rodriguez Lijo
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from openerp import models, fields


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    related_sale_order_id = fields.Many2one(
        comodel_name='sale.order',
        string='Related Sale Order')
