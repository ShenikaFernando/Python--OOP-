class BankAccount:
	"""docstring for BankAccount"""
	def __init__(self, account_type, amount):
		self.account_type = account_type
		self.amount = amount

	def deposite(self, deposite_amount):
		self.amount += deposite_amount
		print("{} account holder desposits {}".format(self.account_type, deposite_amount))

	def withdraw(self, withdraw_amount):
		self.amount -= withdraw_amount
		print("{} account holder withdraw {} ".format(self.account_type, withdraw_amount))

	def __str__(self):
		return "{} account Amount {}".format(self.account_type, self.amount)

matt = BankAccount("Silver", 2000)
print(matt.account_type)
print(matt.amount)


#Matt deposits another 4000
matt.deposite(4000)
print(matt.amount)

matt.withdraw(475)
print(matt.amount)

print(matt)
		