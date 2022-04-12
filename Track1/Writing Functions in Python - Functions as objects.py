
"""
Writing Functions in Python - Functions as objects
"""

# Functions are much like anything else in Python 
# You can treat them as variables for example 

def my_function():
    print('Hello')
    
# then do, 
x = my_function 
type(x)   # prints out 'function' as the type 

x()  # this basically runs the function, as we assigned it to x - it prints Hello to the console 

#----------------------------------------------------------------------------------------------------

# we could do:
PrintyMcPrintface = print

# then do 
PrintyMcPrintface('Python is cool')    # and thus, the statement is printed to the console 

#----------------------------------------------------------------------------------------------------

# We can also add functions to lists or dictionaries 

list_of_functions = [my_function, open, print]    # we have placed our function, and two pre-defined ones, into a list 

# so, we can then call an element of the list (using it's index) and pass it arguments
# for example, say we want to print a statement? we could do:

list_of_functions[2]('I want to print this') 

# or we could call 'my function' which prints hello 
list_of_functions[0]()


# Or if we wanted a dictionary instead:
dict_of_functions = {
    'func1': my_function,
    'func2': open,
    'func3': print
}

# so similar to above, we can use the dictionary to call one of the functions, as if we were calling it directly, for example:
dict_of_functions['func3']('I am printing something here') # we have called the print function from the dictionary and then passed an argument to it

#---------------------------------------------------------------------------------------------------

# we can also define a function within another function 

# say we had this:
def foo(x, y):
    if x > 4 and x < 10 and y > 4 and Y < 10:
        print(x * y) 
        
# we could instead use a function within a function, making the 'If' line easier to read 
def foo(x, y):
    def in_range(v):
        return v > 4 and v < 10
    
    if in_range(x) and in_range(y):
        print(x * y) 
        

# Exercise Example:

function_map = {
  'mean': mean,
  'std': std,
  'minimum': minimum,
  'maximum': maximum
}

data = load_data()
print(data)

func_name = get_user_input()  # an outside function setup to get the user to input which function they wish to use 

# Call the chosen function and pass "data" as an argument
function_map[func_name](data)

