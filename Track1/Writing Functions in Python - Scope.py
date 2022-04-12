
"""
Writing Functions in Python - Scope 
"""

## The global keyword 
# if we did:

x = 7 

def foo():
    x = 42 
    print(x) 
    
# if we call 
foo()   # this prints 42 to the console

# if we call 
print(x)  # this prints 7 to the console

# This is because Python creates a new 'local' x for the function, but does not supercede the x created outside the function, 
# so when the function isn't in use, it's just using the original x 


# If we wanted to change this, we would need to use a 'global' statement 
x = 7
def foo():
    global x 
    x = 42 
    print(x) 
    
foo()     # prints 42 
print(x)  # prints 42 

# This is because we now set x as global within the function, so that value is assigned to x throughout Python now 

#--------------------------------------------------------------------------------------------------------------------------

## The nonlocal keyword 

# This can be used when you are inside a nested function, and want to update a variable within the parent function 

def foo():
    x = 10
    
    def bar():
        x = 200
        print(x) 
        
    bar()      # will run the print 200 
    print(x)   # will run the print 10 

foo()    #  calls function and prints 200 & 10 to the console 


# we could instead use the nonlocal keyword which will then reset the first x=10 to x=200 overall, and thus print 200 twice:
def foo():
    x = 10
    
    def bar():
        nonlocal x   # allows the x=10 to be overriden by the statement now below 
        x = 200
        print(x) 
        
    bar()      # will run the print 200 
    print(x)   # will now also print 200 

foo()    #  calls function and prints 200 & 200 to the console 

#------------------------------------------------------------------------------------------------------------------------

