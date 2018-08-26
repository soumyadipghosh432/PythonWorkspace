# Declare blank list
blankList1 = []
blankList2 = list()

myList1 = ['a', "x", 'y']
myList2 = list(('a', 'b', "c"))

print(myList1)  # ['a', 'x', 'y']
print(myList2)  # ['a', 'b', 'c']


myNewVal = myList1[0] + myList2[1]
print(myNewVal)  # returns string - ab

""" Difference of copying the list object with copying the values 
"""

copyTest1 = myList1
copyTest2 = myList1.copy()
print(copyTest1)  # ['a', 'x', 'y']
print(copyTest2)  # ['a', 'x', 'y']

print(copyTest1 is myList1)  # True - Since both point to same object.
print(copyTest2 is myList1)  # False - Objects are different
print(copyTest1 == myList1)  # True - Values are same. == checks on value
print(copyTest2 == myList1)  # True - Values are same. == checks on value


""" list.append(elem) -- adds a single element to the end of the list. 
    Common error: does not return the new list, just modifies the original. 
    
    list.pop(index) -- removes and returns the element at the given index. 
    Returns the rightmost element if index is omitted (roughly the opposite of append()).
"""
myList1.append("test")
myList1.append("end")
myList1.append("of")
myList1.append("list")
myList1.append("test Again")
print(myList1)  # ['a', 'x', 'y', 'test', 'end', 'of', 'list', 'test Again']
print(myList1.pop(3))
print(myList1.pop())
print(myList1)  # ['a', 'x', 'y', 'end', 'of', 'file']

""" list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
    
    list.remove(elem) -- searches for the first instance of the given element 
                         and removes it (throws ValueError if not present)
"""
myList2.insert(2,"at index 2")
myList2.insert(1,"at index 1")
print(myList2)  # ['a', 'at index 1', 'b', 'at index 2', 'c'] - Index 2 is at 3 since post insert of 2
                # new element added to index 1

myList2.remove("at index 1")  # ['a', 'b', 'at index 2', 'c']
print(myList2)

""" list.extend(list2) adds the elements in list2 to the end of the list. 
    Using + or += on a list is similar to using extend().
"""
myNewList2 = myList1 + myList2
myNewList1 = myList1.extend(myList2)
print(myNewList1)  # Prints None. Since extend() dont return a new object
print(myList1)  # ['a', 'x', 'y', 'end', 'of', 'list', 'a', 'at index 1', 'b', 'at index 2', 'c']
                # extends() changes the content in the caller list
print(myNewList2)  # ['a', 'x', 'y', 'end', 'of', 'list', 'a', 'at index 1', 'b', 'at index 2', 'c']

"""  list.sort() -- sorts the list in place (does not return it). (The sorted() function shown later is preferred.)
     list.reverse() -- reverses the list in place (does not return it)
"""

myList1.sort()
print(myList1)  # ['a', 'a', 'at index 2', 'b', 'c', 'end', 'list', 'of', 'x', 'y']
myList1.sort(reverse=True)
print(myList1)  # ['y', 'x', 'of', 'list', 'end', 'c', 'b', 'at index 2', 'a', 'a']
myList1.reverse()
print(myList1)  # ['a', 'a', 'at index 2', 'b', 'c', 'end', 'list', 'of', 'x', 'y']

""" List Iterations
"""
for item in myList1:
    print(item)

""" List comprehensions are a more advanced feature which is nice for some cases but is not needed for the 
    exercises and is not something you need to learn at first. A list comprehension is a compact way to 
    write an expression that expands to a whole list. 
    The syntax is [ expr for var in list ] -- the for var in list looks like a regular for-loop, 
    but without the colon (:). The expr to its left is evaluated once for each element 
    to give the values for the new list.
"""
numbers = [1,2,3,4,5]
squares = [ x * x for x in numbers ]
print(squares)

greet = ["Hello "+str(x)+" !" for x in squares]
print(greet)

""" Custom Sorting : sorted() helps to sort a list without modifying the actual list.
    This function returns a new list with the contents sorted in order mentioned.
    sorted() takes addtional argument for custom logic of sorting
"""

listTest = ['ax', 'aa', 'AAA', 'x', 'r', 'B', 'X']
print(sorted(listTest))  # ['AAA', 'B', 'X', 'a', 'aa', 'r', 'x'] - Consider CAPITAL first then lowers
print(sorted(listTest, key=str.lower))  # Considers all elements in lowercase and then sort
print(sorted(listTest, key=len))  # ['a', 'x', 'r', 'B', 'X', 'aa', 'AAA'] - sorts according to the length of the element


def MyFn(s):
    return s[-1] # returns the last character of the string

print(sorted(listTest, key=MyFn))  # ['AAA', 'B', 'X', 'aa', 'r', 'ax', 'x'] - sorted on last char of element
