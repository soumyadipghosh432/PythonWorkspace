ipAddress = "111.222.0.1"
print(ipAddress.count("."))
###############################

some_list = ["First Item","Second Item","Third Item"]

some_list.append("New Item")
some_list.append("New Item2")
some_list.remove("New Item")

for item in some_list:
    print(item)

###############################


evens = [2,4,6,8]
odds = [1,3,5,7,9]

numbers = evens + odds
print(numbers) #Concatenated list

#returns object in sorted order
print(sorted(numbers))

#this will not return a variable. Do the change in the object itself
numbers.sort()

print(numbers) #Sorted List

###############################


#below two lists are same, empty lists
list_1 = []
list_2 = list()

list_1=['A','B']
list_2 = list_1
print(list_2 is list_1) #returns true


###############################

list_1=['A','B']
list_2 = list(list_1)
print(list_2 is list_1) #returns false
print(list_2 == list_1) #returns true, since == checks on the content


#this will break the string into character array
print(list("This is a list"))


###############################

list1 = [2,6,4,8]
list2 = list1
list2.sort(reverse=True)
print(list1) #this will print the list as sorted as the list object is same for both variables


###############################

list_1 = [1,2,3,4]
list_2 = [5,6,7,8]

#concatenate two lists
list_3 = list_1 + list_2
print(list_3)

#create a list with two lists as members
list_4 = [list_1, list_2]
print(list_4)

for sets in list_4:
    print(sets) 
    for items in sets:
        print(items)


###############################

menu = []
menu.append(['egg','spam','ham'])
menu.append(['egg','bacon','coffee'])
menu.append(['burger','spam','orange'])

for meal in menu:
    if not "spam" in meal:
        print(meal)
        for items in meal:
            print(items)



###################################
#list to string
myList = ["a", "b", "c", "d"]
newString = ",".join(myList) #this will convert the list into comma seperated string
print(myList)


####################################
# Split a text into list of values
str = "This is a text"
print(str.split()) #this will be comma seperated - ['This', 'is', 'a', 'text']
print(str.split(",")) #this will be space seperated like original string but as a record in list - ['This is a text']
print(str)

