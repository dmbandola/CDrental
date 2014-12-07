import unittest
from cdrent import CD
from customerList import CustomerList
from cdstorage import CDStorage


class TestCheckOut(unittest.TestCase):
    def test_checkout_cd(self):
	cdstorage = CDStorage()
	customerList = CustomerList()

	cd = CD("CD1","XOXO","Available")
	cdstorage.add_cd(cd)
	customer = (001, "Chen")
	customerList.add_customer(customer)

	
	checkout = Checkout()
        checkout.record_cd(cd_id, cudtomer_id)
        self.assertEqual(cdstorage.get_cd_info(cd_id).rented, "Not Available")
