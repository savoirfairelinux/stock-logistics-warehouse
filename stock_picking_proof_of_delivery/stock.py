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

from openerp.osv import fields, orm


class stock_picking_out(orm.Model):
    _name = 'stock.picking.out'
    _inherit = 'stock.picking.out'

    _columns = {
        'state': fields.selection(
            [('draft', 'Draft'),
             ('auto', 'Waiting Another Operation'),
             ('confirmed', 'Waiting Availability'),
             ('assigned', 'Ready to Deliver'),
             ('done', 'Awaiting PoD'),
             ('delivered', 'Delivered'),
             ('cancel', 'Cancelled'), ],
            'Status', readonly=True, select=True,
            help="""
            * Draft: not confirmed yet and will not be scheduled
            until confirmed\n
            * Waiting Another Operation: waiting for another move to proceed
            before it becomes automatically available
            (e.g. in Make-To-Order flows)\n
            * Waiting Availability: still waiting for the availability
            of products\n
            * Ready to Deliver: products reserved, simply waiting
            for confirmation.\n
            * Awaiting: Awaiting PoD
            * Delivered: has been processed, can't be modified or
            cancelled anymore\n
            * Cancelled: has been cancelled, can't be confirmed anymore"""),
    }

    def action_delivered(self, cr, uid, ids, context=None):
        """ Changes picking state to delivered.
        @return: True
        """
        self.write(cr, uid, ids, {'state': 'delivered'})
        return True
