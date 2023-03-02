from ifrs16 import Lease, Organisation

# instantiate organisations to be attributed under our lease
my_lessor = Organisation('Landlord Inc')
my_lessee = Organisation('Tenant Ltd')

# define list of transactions, which can be "decimal" strings for basic usage
my_transactions = ['1234.56', '987.65', '4321.09']

# instantiate `Lease` instance along with tenure type as string
my_lease = Lease(
    start_date='01/01/2023', end_date='01/01/2024', tenure='leasehold',
    lessor=my_lessor, lessee=my_lessee, transactions=my_transactions
)

# display lease instance and its various attributes
print(my_lease)

# access dates which are automatically cast to datetime objects
print(my_lease.start_date)
print(type(my_lease.start_date))

# verify that lease is considered short term
print(my_lease.is_short_term())

# access organisation attributes via `lessor` or `lessee` attribute
print(my_lease.lessor.name)

# access transactions which are automatically cast to decimal objects
print(my_lease.transactions)
print(type(my_lease.transactions[0]))
