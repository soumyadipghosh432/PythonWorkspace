################ Usage of Import and underscore ####################
#### Assumption that someFile.py is having below content ####
#def someFunction():
#	print("doing nothing.....")
#
#def anotherFunction():
#	print("doing nothing too....")	
#
#def _privFunction():
#	print("this is a private function...")	
#
#
#print("Scope from libs :", __name__) # this variable is used to print the currrent scope
#
#someVal = 580
#__privateVal = 440 # this is a private variable which is not intedded to change in any programs who import this.
#
# if this IF statement is not present then following statements will be executed whenever imported from any other external program
#if __name__ == '__main__':
#	print("Calling start from libs")
#	print(someVal * 20)
#	someFunction()
#	anotherFunction()
#	print("Calling end from libs")

import someFile


print("Scope from caller :", __name__) # this will print __main__ since calling from this function. there will another print from import since we used

# globals() is used to print the items in global scope for this program
# if using : import someFile --> then globals() will print someFile as an item in the list.
# members to be used by someFile.<memberName>
print (sorted(globals()))
someFile.someFunction()


from someFile import *
# if using : from someFile import * --> then globals() will print all public members of someFile as an item in the list.
# this will not print any private members i.e. name starting with _
# members to be used by directly calling the member names
print (sorted(globals()))
someFunction()
