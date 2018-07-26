# print('Hello World !')
# print("Quoted string")
# print('double "quotes" are allowed')
# print("Single 'quotes' are also allowed")
# print(1 + 2)
# print(4*4)

############## ESCAPE CHARACTERS ##############
# splitString = "This string in broken\nhere and having a tab \there"
# print(splitString)
# escape1="This is required to print the \\"
# print(escape1)
# escape2 = """ Triple quoted strings takes escapes automatically like \  """
# print(escape2)

############# VARIABLES ###############
# greeting = "Good Morning !"
# name = "User"
# print(greeting + name)
# name = input("Enter you name : ")
# print(greeting + ' ' + name)
# a=12
# b=3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# str = 'ABCDEFGHIJK'
# print(str)
# print(str[0])
# print(str[2])
# print(str[-1])
# print(str[-2])
# print(str[0:5])
# print(str[:4])
# print(str[6:])
# print(str[-5:-2])
# print(str[1:7:2]) #Skip by 2 characters
# str='1, 2, 3, 4, 5, 6'
# print(str[0::3])
# print(str[1::3])
#
# print("hello " * 5)
#
# str = "weekend"
# print("end" in str) #substring
# print("monday" in str)

age = 24
print("My age is : " + str(age) + " years")

print("My age is : %d years" % age)
print("My age is : %d %s, %d %s" % (age, "years", 6, "months"))
print("My age is : {0} years".format(age))

print("%2d is squared to %4d and cubed to %4d" % (2, 2**2, 2**3))
print("%2d is squared to %4d and cubed to %4d" % (8, 8**2, 8**3))
print("%2d is squared to %4d and cubed to %4d" % (12, 12**2, 12**3))
print("{0:2} is squared to {1:4} and cubed to {2:4}".format(2, 2**2, 2**3))
print("{0:2} is squared to {1:4} and cubed to {2:4}".format(8, 8**2, 8**3))
print("{0:2} is squared to {1:4} and cubed to {2:4}".format(12, 12**2, 12**3))
#Left Alignment
print("{0:2} is squared to {1:<4} and cubed to {2:<4}".format(2, 2**2, 2**3))
print("{0:2} is squared to {1:<4} and cubed to {2:<4}".format(8, 8**2, 8**3))
print("{0:2} is squared to {1:<4} and cubed to {2:<4}".format(12, 12**2, 12**3))



print("Value of Pi is : %30f" % (22/7))
print("Value of Pi is : %30.15f" % (22/7))
print("Value of Pi is : %.15f" % (22/7))
print("Value of Pi is : {0:30.15}".format(22/7))







