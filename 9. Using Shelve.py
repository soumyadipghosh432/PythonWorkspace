import shelve

# traditional way of using
fruit = shelve.open("testShelve")  # open the shelve
fruit['orange'] = "a sweet and round fruit"
fruit['grape'] = "a fruit grow in bunches"
print(fruit['orange'])
fruit.close()  # mandatory to close

# pythonic way of using shelve
# shelve open with read-write mode normally. once values writen can read further from data files
with shelve.open("testShelve") as fruits:  # this will create a data file in the same location of the program
    fruits['orange'] = "a sweet and round fruit"
    fruits['grape'] = "a fruit grow in bunches"
    fruits['apple'] = "a health fruit used to make cider"
    fruits['strawberry'] = "a red sweet yummy fruit"
    print(fruits)  # this will print the value of the object reference
    print(fruits['strawberry'])  # this will bring error if the index key is mis-spelled or absent
    print(fruits.get('strawbery'))  # this will return none if no match found, but dont throw error

    del fruits['grape']  # delete an entry

    for keys in fruits:
        print("{} --> {}".format(keys, fruits.get(keys)))

    print("=" * 25)

    # for keys in sorted order to diaplsy
    ordered_keys = list(fruits.keys())
    ordered_keys.sort()
    for keys in ordered_keys:
        print("{} --> {}".format(keys, fruits.get(keys)))

    print("=" * 25)
    # get the values not keys
    for x in fruits.values():
        print(x)
    print(fruits.values()) # print the object reference

    print("=" * 25)
    # get the items as key-value pairs
    for x in fruits.items():
        print(x)
    print(fruits.items()) # print the object reference

########### UPDATE in SHELVE #############

sandwitch = ["bread", "cheese", "chicken"]
pasta = ["pasta", "sweet corn"]
tea = ["tea leaf", "water", "milk", "sugar"]

with shelve.open("recipe") as recipe:
    recipe["sandwitch"] = sandwitch
    recipe["pasta"] = pasta
    recipe["tea"] = tea

with shelve.open("recipe") as recipes: #reopening the shelve
    recipes["sandwitch"].append("Butter") #since this shelve is containing lists append is allowed
    print(recipes.get("sandwitch")) #this will not reflect the changes in the list

    # this will reflect the changes in the list
    temp_list = recipes["sandwitch"]
    temp_list.append("Butter")
    recipes["sandwitch"] = temp_list
    print(recipes.get("sandwitch"))

# reopening the shelve with writeback to support direct write
with shelve.open("recipe", writeback=True) as recipes:
    recipes["sandwitch"].append("tomato")
    print(recipes.get("sandwitch"))
