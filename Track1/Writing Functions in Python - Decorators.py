
"""
Writing Functions in Python - Decorators
"""

# so what is a decorator?
# say you have a function, that takes some inputs & creates some outputs 
# well, a decorator is like a wrapper around that function, that can change the way it behaves 


# what does a decorator look like?
@double_args
def multiply(a, b):
    return a * b 

multiply(1, 5) 

# The @double_args decorator is a decorator that multiples every argument by 2, before passing them into the decorated function 

# so - the decorated version of the multiply function, when we pass 1 & 5 as the arguments into the function, they actually become 2 & 10
# Thus, the output is 20 rather than 5 

#-----------------------------------------------------------------------------------
#
# Let's build the double_args decorator above 

def multiply(a, b):
    return a * b

def double_args(func):
    return func 

new_multiply = double_args(multiply) 

# so atm, double_args doesn't modify anything. 


# Now, if we want to create a decorator to actually cause action/change, we could do:
def multiply(a, b):
    return a * b

def double_args(func):
    # Define a new function that we can modify 
    def wrapper(a, b):
        # call the passed in function, but double each argument 
        return func(a * 2, b * 2) 
    return wrapper 

multiply = double_args(multiply)   # overwrites the original multiply variable with new double_args one
   
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

"""
Exercises
---------

Using decorator syntax

You have written a decorator called print_args that prints out all of the arguments and their values any time a function that 
it is decorating gets called.
"""
 
## Decorate my_function() with the print_args() decorator by redefining my_function(). 
def my_function(a, b, c):
  print(a + b + c)

# Decorate my_function() with the print_args() decorator
my_function = print_args(my_function)

my_function(1, 2, 3)

# Decorate my_function() with the print_args() decorator
@print_args
def my_function(a, b, c):
  print(a + b + c)

my_function(1, 2, 3)

