for i in range(1,5):
    print("The value is {}".format(i))


phone="+91 90.38.678.449"

for i in range(0, len(phone)):
    if not ((phone[i] == ".") or (phone[i] == " ")):
        #changing the seperator for line prints. default is \n
        print(phone[i],end='') 
print()

for char in phone:
    if char in '+0123456789':
        print(char,end='')
    

#third parameter is range
for i in range (4,50,8): 
    print(i)
else:
    #this should be in the proper indentation with LOOP
    print("I'm the final code. If any BREAK in loop I'll be not reachable")


for i in range(1,6):
    for j in range(1,10):
        print("{0:4}    X {1:4} = {2:5}".format(i,j,i*j))
    print("========================")


i=0
while i<10:
    print(i)
    i+= 1


exit_options = ["A","F","R"]
choice =""
while choice not in exit_options:
    choice=input("Enter choice. Type 'quit' to quit game")
    if choice == "quit":
        print("Game Over")
        break
else:
    print("You choose right")
    
