######################## Using Functions in python #########################

# Define a function
def get_food():
    print("That was a good breakfast.")

def text_marginleft(text):
    width = 160
    left_margin = (width - len(str(text))) // 2 # using str() to convert to any input to test to calculate length
    print(" " * left_margin, text)

get_food() # call the function
text_marginleft("This is some text with margin from left")
text_marginleft("Hello World !!!")
text_marginleft(1234)

# Defining a custom function same as print() for printing only
def custom_print(*texts):
    text = ""
    for arg in texts:
        text += str(arg) + " "
    left_margin = 2
    print(" " * left_margin, text)

custom_print(1,2,"Hello","World")
print(1,2,"Hello","World")
custom_print("Just a single string")
print("Just a single string")
custom_print("Hello",12345,"World")
print("Hello",12345,"World")

# Defining a custom function same as print() with control parameters
def custom_print_param(*texts, x_sep=" ", x_end="\n", x_file=None, x_flush=False):
    text = ""
    for arg in texts:
        text += str(arg) + x_sep
    left_margin = 1
    print(" " * left_margin, text, end=x_end, file=x_file, flush=x_flush)

custom_print_param("--> Hello","--> World",x_sep="|")    


# Defining a function to return a string
def custom_print_ret(*texts):
    text = ""
    for arg in texts:
        text += str(arg) + " "
    left_margin = 2
    return " " * left_margin + text

print(custom_print_ret(" ---> Some text <---"))
print(custom_print_ret(" ---> Some text1 <---"," ---> Some text2 <---"))


################## LOCAL and GLOBAL VARIABLES #######################
# Local variables to function
def someFunction(text):
    val1 = 10
    list1 = list(range(10))
    print(list1)
    print(locals()) # Get the variables those are defined / used in this function scope

someFunction("someValue")    

### Global and Local Variable with same name
x = 5 # this is global variable

def foo():
    x = 10
    print("local x:", x) # 10

foo()
print("global x:", x) # 5


### Nonlocal Variables
# Nonlocal variable are used in nested function whose local scope is not defined.
# This means, the variable can be neither in the local nor the global scope.
def outer():
    s = "local"
    print("inner before nonlocal:", s) #Local
    
    def inner():
        nonlocal s # If this is commented, then outer variable will not be changed
        s = "nonlocal"
        print("inner after nonlocal:", s) # Nonlocal
    
    inner()
    print("outer:", s) # Nonlocal

outer()


### Global variable in function scope
x = 5 # this is global variable

def foo():
    global x # Using as global variable
    x = x * 5
    print("local x:", x) # 25

print("global x before:", x) # 5
foo()
print("global x after:", x) # 25

