##############################   RANGE    ########################################
#Range to List

my_list = list(range(10))
print(my_list)

even = list(range(0,10,2))
odd = list(range(1,10,2))
print(even)
print(odd)

##################################################################
decimals = range(5,15)
#index access of range
print(decimals.index(8)) #return index of value 8
print(decimals[8]) #return value at index 8

##################################################################
sevens = range(7,1000000,7)
x = int(input("Enter a number "))
if x in sevens:
    print("{} is divisible by 7".format(x))

##################################################################
#Print in reverse order with negative step on the range slice
#this generates list 0 to 20 and then go reverse from 20 by 2 steps
for i in range(0,20)[::-2]:
    print(i)

#this tries to generate list with 0 to 20 by step -2 start from 0.
#if we start counting -2 from 0 then we cannot reach 20 anyhow. so this will not generate any list
for i in range(0,20,-2):
    print(i)

#this will generate a list from 19 to 0 by going step 2 from 19 towards 0
for i in range(19,0,-2):
    print(i)

    
print( range(0,100,-2) == range(99,0,-2) ) # this is false
print( range(0,100)[::-2] == range(99,0,-2) ) #this is true


##################################################################
#String reversal
var = "I will be modified"
print(var[::-1])




##############################   TUPLE    ########################################

t = "a","b","c"
print(t) #this is a tuple

print("a","b","c") #this is not a tuple
print(("a","b","c")) #this is a tuple

print( t == (("a","b","c")) ) #this is true


#to change content of a tuple. Direct update is not allowed. Tuples are immutable
# if and only if a tuple contains list then range can be modified with append/remove functions
t = t[0], "xyz", t[2]
print(t)

#tuple unpacking
val1, val2, val3 = t
print(val1)
print(val2)
print(val3)

#tuple of tuple
tup = "A", 2, "XYZ", (1,"AA"), (("A",1),("B",2))
val1 , val2, val3, val4, val5 = tup
print(val4)
print(val5)
part1, part2 = val5
print(part1)


