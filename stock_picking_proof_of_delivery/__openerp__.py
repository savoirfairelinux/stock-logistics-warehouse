# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2014 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Stock Picking Proof of Delivery',
    'version': '0.1',
    'author': 'Savoir-faire Linux',
    'maintainer': 'Savoir-faire Linux',
    'website': 'http://www.savoirfairelinux.com',
    'license': 'AGPL-3',
    'category': 'Warehouse Management',
    'summary': 'Add a new state "Awaiting PoD" in stock_picking',
    'description': """
Add a new state "Awaiting PoD" in stock_picking
===============================================

This module add a new state "Awaiting PoD" in stock_picking.

When delivering a Delivery Order, the state changes to "Awaiting PoD"
rather than "Delivered"; the user can then click the button "PoD received"
to change the state to done.

This module also add a new predefined filter in the search view "PoD not
received" for the Delivery Orders.

Contributors
------------
* El Hadji Dem (elhadji.dem@savoirfairelinux.com)
""",
    'depends': [
        'stock',
    ],
    'external_dependencies': {
        'python': [],
    },
    'data': [
        'stock_view.xml',
        'stock_workflow.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}
