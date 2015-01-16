


class YearMonth():

	def __init__(self, year_month):
		self.year_month = year_month
		self.store_customers = set()
		self.autorip_customers = set()
		self.cloudplayer_customers = set()
		self.lib_customers = set()
		self.prime_customers = set()

	def get_year_month(self):
		return self.year_month

	def add_customer(self, customer_type, cust_id, prime):
		if prime == '1':
			self.prime_customers.add(cust_id)
		if customer_type == 'store':
			self.store_customers.add(cust_id)
		elif customer_type == 'auto':
			self.autorip_customers.add(cust_id)
		elif customer_type == 'cp':
			self.cloudplayer_customers.add(cust_id)
		elif customer_type == 'lib':
			self.lib_customers.add(cust_id)

	def find_overlap(self):
		all_cust = len(self.store_customers | self.cloudplayer_customers | self.autorip_customers)
		store_cp = len(self.store_customers & self.cloudplayer_customers)
		store_auto = len(self.store_customers & self.autorip_customers)
		cp_auto = len(self.cloudplayer_customers & self.autorip_customers)
		store_cp_auto = len(self.store_customers & self.cloudplayer_customers & self.autorip_customers)
		store_only = len(self.store_customers - self.cloudplayer_customers - self.autorip_customers)
		cp_only = len(self.cloudplayer_customers - self.autorip_customers - self.store_customers)
		auto_only = len(self.autorip_customers - self.store_customers - self.cloudplayer_customers )
		auto_lib = len(self.autorip_customers & self.lib_customers)
		auto_nocp_with_lib = len(self.autorip_customers - self.cloudplayer_customers & self.lib_customers)
		auto_NOcp_NOlib_prime = len(((self.autorip_customers - self.cloudplayer_customers) - self.lib_customers) & self.prime_customers)
		prime_cust = len(self.prime_customers)
		cp_prime = len(self.cloudplayer_customers & self.prime_customers)
		store_prime = len(self.store_customers & self.prime_customers)
		auto_prime = len(self.autorip_customers & self.prime_customers)
		


		return self.year_month + ': ' + '\n' + '*total customers: '            + str(all_cust)              + '\n' \
											 + '*Store and CP customers: '     + str(store_cp)              + '\n'\
											 + '*Store and AutoRip customer: ' + str(store_auto)            + '\n'\
											 + '*CP and AutoRip customers: '   + str(cp_auto)               + '\n'\
											 + '*All engaged customers: '      + str(store_cp_auto)         + '\n'\
											 + '*Store only customers: '       + str(store_only)            + '\n'\
											 + '*CP only customers: '          + str(cp_only)               + '\n'\
											 + '*AutoRip only customers: '     + str(auto_only)             + '\n'\
											 + '*AutoRip no CP with a lib: '   + str(auto_nocp_with_lib)    + '\n'\
                                             + '*Prime customers: '            + str(prime_cust)            + '\n' \
                                             + '*auto_NOcp_NOlib_prime: '      + str(auto_NOcp_NOlib_prime) + '\n'\
                                             + '*cp prime: '                   + str(cp_prime)              + '\n' \
                                             + '*store prime: '                + str(store_prime)           + '\n' \
                                             + '*autorip prime: '              + str(auto_prime)



def process_line(line):
		
	line = line.strip().split('\t')
	ym, cust_id, cust_type, prime = line[0:4]
	if ym in year_month_dic:
		year_month_dic[ym].add_customer(cust_type, cust_id, prime)
	else:
		temp = YearMonth(ym)
		temp.add_customer(cust_type, cust_id, prime)
		year_month_dic[ym] = temp 

def get_monthly_overlap():

	files = ('store_3.tsv', 'cp_4.tsv', 'auto_3.tsv', 'lib_10.tsv')
	for file_name in files:
		for customer in open(file_name, 'r'):
			if 'year_month' in customer or '2014-4' not in customer:
				continue
			else:
				process_line(customer)
        for key in year_month_dic:
                
                print(year_month_dic[key].find_overlap())

# #test_list = [('2014-01', '1234', 'store'), ('2014-01', '2345', 'store'), ('2014-02', '1234', 'cp'), ('2014-01', '1234', 'cp')]
year_month_dic = {}
get_monthly_overlap()

	
	




