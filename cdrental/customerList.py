class CustomerList(object):

	def __init__(self):
		self.customerList = {}

	def add_customer(self, customer):
		self.customerList[customer.customer_id] = customer.customer_name

    def get_customer_info(self, customer_id):
    	self.customerList.get(customer_id)
