import unittest
from customer import Customer
from cdrent import CD
from customerList import CustomerList

class TestCustomerList(unittest.TestCase):
    def test_customer_list_is_initially_empty(self):
        customerList = CustomerList()
        self.assertEqual({}, customerList.customers)
        self.assertEqual(len(customerList.customers), 0)

    def test_add_customer(self):
        customerList = CustomerList()
        customer1 = Customer(001, "Chen")
        customer2 = Customer(002, "Chen")

        customerList.add_customer(customer1)
        customerList.add_customer(customer2)
        self.assertEqual(len(customerList.customers), 2)

    def test_get_customer_info(self):
        customerList = CustomerList()
        customer1 = Customer(001, "Chen")
        customerList.get_customer_info(customer1)
        self.assertEqual(customerList.get_customer_info(001), customer1)

if __name__ == '__main__':
    unittest.main()
