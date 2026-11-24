# STeSI Consulting - Daniele Lucarelli
# License OPL-1 (https://www.odoo.com/documentation/user/18.0/legal/licenses/licenses.html).
from lxml import etree
from odoo.tests import tagged
from odoo.tests.common import TransactionCase

DATE_FIELDS = ('start_date', 'end_date', 'number_of_days')


@tagged('post_install', '-at_install')
class TestDatesVisible(TransactionCase):
    """The date fields of the order lines are never hidden, and stay required
    only when the product requires dates."""

    def _fields(self, model, view_xmlid, path):
        view = self.env.ref(view_xmlid)
        arch = etree.fromstring(self.env[model].get_view(view.id)['arch'])
        result = {}
        for name in DATE_FIELDS:
            nodes = arch.xpath(f"{path}/field[@name='{name}']")
            self.assertTrue(nodes, name)
            result[name] = nodes[0]
        return result

    def test_order_line_list_dates_visible(self):
        nodes = self._fields('sale.order', 'sale.view_order_form', "//field[@name='order_line']/list")
        for name, node in nodes.items():
            self.assertFalse(node.get('invisible'), name)
            self.assertEqual(node.get('required'), 'must_have_dates', name)

    def test_order_line_readonly_form_dates_visible(self):
        nodes = self._fields('sale.order.line', 'sale.sale_order_line_view_form_readonly', '/')
        for name, node in nodes.items():
            self.assertFalse(node.get('invisible'), name)
            self.assertEqual(node.get('required'), 'must_have_dates', name)
