import unittest
from customer import Customer
from cdrent import CD


class TestCustomer(unittest.TestCase):
    def test_customer_info(self):
        customer = Customer(007, "Chen")
        self.assertEqual(customer.customer_name, "Chen")

    def setUp(self):
        self.customer = Customer(007, "Chen")

    def test_add_method_raises_typeerror_if_id_is_string(self):
         self.assertRaises(TypeError, self.customer.check_id_if_int, 007,"Chen")
