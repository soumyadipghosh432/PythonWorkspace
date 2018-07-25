greeting = "Good Morning ! "
name = "Rob"

print("{0} {1}".format(greeting,name))


any_num = int(input("Enter any number : "))


guess = int(input("Guess the number : "))

if guess > 5:
    guess = int(input("Guess lower value : "))
    if guess == 5:
        print("You got it !")
    else:
        print("Sorry, Try again !")
elif guess < 5:
    guess = int(input("Guess higher value : "))
    if guess == 5:
        print("You got it !")
    else:
        print("Sorry, Try again !")
else:
    print("You got it frst time !!")


guess2 = int(input("Try another guess : "))

if (guess == 5) and (guess2 == 8):
    print("Doing great !")
else:
    if 5 <= guess2 <= 10 :
        print("Almost near")
    if (guess2 <= 0) and (guess2 >= 20):
        print("Not even close this time !")
    else:        
        print("Tough luck")


test_bool = ""
if test_bool:
    print("Yes")
else:
    print("No")

c = 8

if not(c > 15):
    print("The value is low enough")
    
    

