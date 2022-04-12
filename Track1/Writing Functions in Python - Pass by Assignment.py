
"""
Writing Functions in Python - Pass by Assignment
"""

# if we had a function, called foo

def foo(x):
    x[0] = 99    # Takes the first object in a list, changes it to 99
    
my_list = [1,2,3]   # we create a list 
foo(my_list)        # we pass the created list into the foo function 

print(my_list)      # and as we now print 'my_list' - we see 99, 2, 3

# This is because lists are 'mutable' - aka they can be changed 

#-----------------------------------------------------------------------------------------

# if we had a function called bar that adds 90 to an object:

def bar(x):
    x = x + 90    # we add 90 to an object under this function 
    
my_var = 3         # create a variable with value 3 
bar(my_var)        # apply that variable into out function 
print(my_var)      # print out m,y_var again - it's still 3. NOT 93. This is because integers are 'Immutable' - aka can't be changed 

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

"""
Mutable default arguments are dangerous 
"""
# Imagin we have a function to create an emoty list and append a 1 to it 
def foo(var=[]):
    var.append(1)
    return var

foo()   # we run it, as expected, we get a list >>> [1] 

# but look, if we run it again, 
foo()   # we now get a list:  [1, 1]   - this is because we have already mutated var 


# The better approach would be:
def foo(var=None):
    if var is None:
        var = []
    var.append(1)
    return var 

foo()  # now, when you run this function, it will only ever print a list [1] - regardless of how many times you run it 

#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------

def store_lower(_dict, _string):
  """Add a mapping between `_string` and a lowercased version of `_string` to `_dict`

  Args:
    _dict (dict): The dictionary to update.
    _string (str): The string to add.
  """
  orig_string = _string
  _string = _string.lower()
  _dict[orig_string] = _string

d = {}
s = 'Hello'

store_lower(d, s)

print(d)
print(s) 

