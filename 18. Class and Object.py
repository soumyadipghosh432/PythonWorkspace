class Laptop(object):

	powerSource = "electricity"

	def __init__(self, make, price):
		self.make = make
		self.price = price
		self.isHavingOs = False

	def assignOs(self):
		self.isHavingOs = True

	def getOs(self):
		print("Assigning OS to {}".format(self.make))
		if self.isHavingOs:
			print("{} is having OS pre-installed".format(self.make))
		else:
			print("{} is not having OS pre-installed".format(self.make))
			
			
dell = Laptop("Dell", "40000")
lenovo = Laptop("Lenovo", "38000")
hp = Laptop("HP", "39000")

print("Make : ", dell.make)
print("Initial Price : ", dell.price)

dell.price = 42000
print("Updated Price : ", dell.price)

print("Initial HP Power Source : ", hp.powerSource)
hp.powerSource = "solar/electricity"
print("Modified HP Power Source : ", hp.powerSource)

print("Catalouge ===> \n\t{} : \t\t{} \n\t{} : \t{} \n\t{} : \t\t{} ".format(dell.make, dell.price, lenovo.make, lenovo.price, hp.make, hp.price))

#  works exactly same as above
print("Catalouge ===> \n\t{0.make} : \t\t{0.price} \n\t{1.make} : \t{1.price} \n\t{2.make} : \t\t{2.price} ".format(dell, lenovo, hp))

# Calll functions of class from objects. Method - 1
dell.getOs()

if not dell.isHavingOs:
	dell.assignOs()

dell.getOs()

# Calll functions from class using object. Method - 2
lenovo.getOs()

if not lenovo.isHavingOs:
	Laptop.assignOs(lenovo)

lenovo.getOs()	


"""
In Python after instanciating a class, we can add attributes directly
to objects. However some value is required to be assigned for that.
These are called instance variables
"""

dell.rating = 4.5
print("Laptop rating for dell : " , dell.rating)

try:
	print("Laptop rating for Lenovo : " , lenovo.rating) # this will throw error
except:
	print("Lenovo do not have rating assigned")	


## Get all attributes of object as dictionary.
print(Laptop.__dict__) # this will show powerSource variable since it was defined in class namespace
print(dell.__dict__) # this will not show powerSource variable
print(lenovo.__dict__) # this will not show powerSource variable
print(hp.__dict__) # this will show show powerSource variable since the value is modified later in program scope
