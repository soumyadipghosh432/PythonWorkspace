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
    print(" " * left_margin, text, end=x_end, file=x_file, flush=x_flush, sep=x_sep)


custom_print_param("--> Hello","--> World",x_sep="|")    
