
"""
Writing Functions in Python - Docstrings
"""


# Docstrings is basically using the """ to write multiple lines of commented code. 
# It can be best practice to include these when writing a function 
# Example:

def function_name(arguments):
    """
    1) Describe what the function does 
    2) Description of arguments needed, if any 
    3) Description of return value(s), if any
    4) Description of errors raised, if any 
    5) optional extra notes or examples of usage etc.
    
    """
# now write in function code from here etc etc.
    
#--------------------------------------------------------------------------------------------------------
    
# Google Style 
def function(arg_1, arg_2=42):
"""Description of what the function does.

Args:
arg_1 (str): Description of arg_1 that can break onto the next line
if needed.
arg_2 (int, optional): Write optional when an argument has a default
value.

Returns:
bool: Optional description of the return value
Extra lines are not indented.

Raises:
ValueError: Include any error types that the function intentionally
raises.

Notes:
See https://www.datacamp.com/community/tutorials/docstrings-python
for more info.
"""


# Numpydoc Style - most commonly used in scientific community 
def function(arg_1, arg_2=42):
"""
Description of what the function does.

Parameters
----------
arg_1 : expected type of arg_1
Description of arg_1.
arg_2 : int, optional
Write optional when an argument has a default value.
Default=42.

Returns
-------
The type of the return value
Can include a description of the return value.
Replace "Returns" with "Yields" if this function is a generator.
"""

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

# Retrieving Docstrings 

# Imagine we have this dummy function, with docstrings 
def the_answer():
    """Return the answer to life,
    the universe, and everything.
    
    Returns:
        int 
    """
    return 42 

# If we use:
print(the_answer.__doc__)   # it prints the docstrings text to the console 


# likewise, we can also use the 'inspect' module 
import inspect 
print(inspect.getdoc(the_answer))    # And prints the clean version of docstrings to the console 
  
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
# Create a function that collects the docstring for any other function you pass into it 
def build_tooltip(function):
  """Create a tooltip for any function that shows the 
  function's docstring.
  
  Args:
    function (callable): The function we want a tooltip for.
    
  Returns:
    str
  """
  # Use 'inspect' to get the docstring
  docstring = inspect.getdoc(function)
  border = '#' * 28
  return '{}\n{}\n{}'.format(border, docstring, border)

print(build_tooltip(count_letter))
print(build_tooltip(range))
print(build_tooltip(print))

