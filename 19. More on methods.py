import datetime
import pytz


class Account:
	""" this is a class for bank account with deposit and withdraw functionality """

	@staticmethod
	def _getCurrentTime():
		""" =============================================================================
			the name starts with _. this is the convention in python to denote
			that this method is NOT intended to be used by any external functions.
			This function purely meant for internal use and change in this may cause
 			break in the functionality. This is named as NONPUBLIC as per pythonic 
 			way of coding since it will not enforce the attribute to be private
		============================================================================= """
		xt = datetime.datetime.utcnow()
		t = pytz.utc.localize(xt)
		return t

	def __init__(self, name, amount):
		self.name = name
		""" ===========================================================================
			the name for balance is started with __. this is the pythonic way of hiding
			attributes. This is called NAME MANGLING. This will somehow prevent the 
			change of the value for this attribute directly in the client code. 
			The effect of name mangling is the attribute name will be internally 
			change from __balance to _Account__balance. So, accessing the value 
			of __balance outside class definition by using <object>.__balance will not 
			make any changes in the actual variable.
			However, if outside class definition if it used as <obj>._Account__balance
			then it will allow the value to be changed. This is strongly discouraged.
		=========================================================================== """
		self.__balance = amount
		self.transactions = [("Deposit",Account._getCurrentTime(),amount)]
		print("Account created for : ", name, "with balance : ", amount)

	def show_balance(self):
		print("Current balance is : ", self.__balance)
	

	def deposit(self,amount):
		if amount > 0:
			self.__balance += amount
			self.transactions.append(("Deposit",Account._getCurrentTime(),amount))
		self.show_balance()


	def withdraw(self,amount):
		if 0 < amount <= self.__balance:
			self.__balance -= amount
			self.transactions.append(("Withdraw",Account._getCurrentTime(),amount))	
		else:
			print("Amount must be more than 0 and less than current balance")
				
		self.show_balance()

	def show_transctions(self):
		print("============== Account Transactions ================")
		for tr_type, date, amount in self.transactions:
			print("{:9}  {:12}  on {} (Local Time {})".format(tr_type, amount, date, date.astimezone()))
		self.show_balance()


if __name__ == '__main__':
	""" ============================================================
		this will only execute when the program is called directly.
		If the file is imported as module in different program then
		following lines will not be executed. 
	============================================================="""
	myAcc = Account("someName", 5000)
	myAcc.deposit(15000)
	myAcc.withdraw(2000)
	myAcc.withdraw(0)
	""" ===========================================================
		below is the effect of NAME MANGLING. Due to the name 
		mangled with the class name using the __, below code
		will not effect directly in the scope of the class.
		However this will create a local variable in the main 
		scope of flow for the program 
	=========================================================== """
	myAcc.__balance = 9090909090909
	myAcc.withdraw(65656565656)
	myAcc.show_transctions()
