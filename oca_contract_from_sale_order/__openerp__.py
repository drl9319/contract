# -*- coding: utf-8 -*-
{
    'name': "Contract from sale order",

    'summary': """stock""",

    'author': "Daniel Rodriguez, Odoo Community Association (OCA)",
    'website': "http://danielrodriguez.esy.es/blog/",
    # Category se usa com filtrro para la lista de modulos
    'category': 'Other',
    'version': '8.0.1.0.0',
    'license': 'AGPL-3',
    # Depends indica los modulos necesarios para el correcto trabajo de nuestro modulo
    'depends': [
        'sale',
        'analytic',
        'account_analytic_analysis',
    ],  # es una lista porque puede depender de mas de uno
    # Datos que siempre carga
    'data': [
        'views/sale_order.xml'
    ],
    "installable": True,
}
