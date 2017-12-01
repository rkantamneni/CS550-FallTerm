import random
class Account:
	def __init__(self, amount, pin):
		self.balance = amount
		self.pin = pin
		self.account = random.randint(1000000000,9999999999)
		self.isOpen = True

	def close(self, pin):
		if self.pin == pin:
			isOpen = False
			money = self.balance 
			self.balance = 0
			return money
		else:
			self.pinerror()
			return None

	def deposit(self, amount, pin):
		if self.pin == pin:
			self.balance += amount
			self.slip("Deposit", amount)
		else:
			self.pinerror()

	def withdraw(self, amount, pin):
		if self.pin == pin:
			if self.balance > amount:
				self.balance -= amount
			else:
				print("insufficient funds")
			self.slip("Withdraw", amount)
		else:
			self.pinerror()

	def pinerror(self):
		print('wrong pin')

	def slip(self, action, amt):
		print("------------------------")
		print("Account number: ******" + str(self.account)[6:])
		print(action+": $"+str(amt))
		print("Balance: $"+ str(self.balance))
		print("------------------------\n\n\n")


ba = Account(500, 1111)
ba.withdraw(200, 1123) 
ba.withdraw(200, 1111) 
ba.withdraw(500, 1111) 
ba.deposit(500, 5432) 
ba.deposit(500, 1111)
print(ba.close(1111))