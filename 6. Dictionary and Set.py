#################### DICTIONARY ########################

fruit = {
    "lemon" : "Round and Yellow coloured fruit",
    "strawberry" : "Red and sweet",
    "grape" : "small, round, sweet and grow in bunches",
    "lemon" : "this is duplicate and will replace the initial value for lemon"
}

print(fruit)
print(fruit["lemon"])

#add new key-value pair
fruit["apple"] = "sweet fruit"

#get all keys, values and pair tuples
print(fruit.keys())
print(fruit.values())
print(fruit.items())

#get dictionary values
key = input("Enter fruit name : ")
value = fruit.get(key)
#value = fruit[key] #this is also correct but in case of any entry which is not existing then it will throw error
print(value)

#modified approach
value = fruit.get(key, "The entered item does not exist in the dictionary")
print(value)

#iterating the dictionary
for item in fruit:
    print(item) #returns the key
    print(fruit.get(item)) #returns the value


#create a list from dictionary and sort the values
ordered_keys = list(fruit.keys())
ordered_keys.sort()
for k in ordered_keys:
    print("{} - {}".format(k, fruit.get(k)))


#tuple <-> dictionary
tup = tuple(fruit.items())
new_fruit = dict(tup)


#merge dictionaries
new_fruit = { "some fruit" : "no description"}
new_fruit.update(fruit) #this will not create a new object
print(new_fruit)


#copy dictionary. this will create a new object
copied_fruits = fruit.copy()


#delete a key-value pair
del fruit["lemon"]

#clear a dictionary
fruit.clear()

#delete the dictionary object
del fruit
#print(fruit) #this will throw error



#################### SETS #######################

animals = {"cow", "sheep", "goat"}
print(animals)

animals.add("horse")

#create an empty set
empty_set = set()
empty_set = {} #this is wrong. this will create an empty dictionary

#other typs to sets
wild_animals = set(["Lion", "Tiger", "Panther"]) #convert list to set
print(wild_animals)

evens = set(range(0,40,2)) #list to set
squares_tuple = (1,4,9,16,25)
squares = set(squares_tuple) #tuple to set

print(squares.union(evens))
print(squares.intersection(evens))

print(squares & evens) #AND operation

#difference between sets. these returns a new set
print(squares.difference(evens))
print(squares - evens)#similar to above
print(evens.difference(squares))
print(evens - squares)#similar to above

#difference update makes update for difference and returns a new object without the different values
print(sorted(evens))
evens.difference_update(squares)
print(sorted(evens))

#symmetric one set to another set. opposite to intersection
print(evens.symmetric_difference(squares)) #returns a new object
print(squares.symmetric_difference(evens)) #returns a new object


#remove item from set
print("=" * 25)
squares.remove(9) #works fine
evens.discard(10) #works fine
print(squares)
#squares.remove(4545) #throws error
squares.discard(4545)

try:
    squares.remove(4545)
    print("Value removed successfully")
except KeyError:
    print("Value is not present in set")


#frozen set
vowels = frozenset("aeiou")
print(vowels)


#Superset and Subset
if evens.issuperset(squares):
    print("Evens is a superset of squares")

if squares.issubset(evens):
    print("Squares is a subset of evens")
