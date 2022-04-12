
"""
Writing Functions in Python - Decorators that take arguments
"""

"""
Run_n_times()

In the video exercise, I showed you an example of a decorator that takes an argument: run_n_times(). 
The code for that decorator is repeated below to remind you how it works. Practice different ways of 
applying the decorator to the function print_sum(). Then I'll show you a funny prank you can play on 
your co-workers:

"""
def run_n_times(n):
  """Define and return a decorator"""
  def decorator(func):
    def wrapper(*args, **kwargs):
      for i in range(n):
        func(*args, **kwargs)
    return wrapper
  return decorator

#-------------------------------------------------------------------------------------------------
  
# Make print_sum() run 10 times with the run_n_times() decorator
@run_n_times(10)
def print_sum(a, b):
  print(a + b)
  
print_sum(15, 20)



# Use run_n_times() to create the run_five_times() decorator
run_five_times = run_n_times(5)

@run_five_times
def print_sum(a, b):
  print(a + b)
  
print_sum(4, 100)


# Modify the print() function to always run 20 times
print = run_n_times(20)(print)

print('What is happening?!?!')

#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
 
"""
A real world example - Timeout(): a real world example 
"""

"""
Tag your functions 

Tagging something means that you have given that thing one or more strings that act as labels. For instance, we often tag emails or
photos so that we can search for them later. You've decided to write a decorator that will let you tag your functions with an 
arbitrary list of tags. You could use these tags for many things:

> Adding information about who has worked on the function, so a user can look up who to ask if they run into trouble using it.
> Labeling functions as "experimental" so that users know that the inputs and outputs might change in the future.
> Marking any functions that you plan to remove in a future version of the code.
Etc
"""

# Define a new decorator, named decorator(), to return
# Ensure the decorated function keeps its metadata
# Call the function being decorated and return the result
# Return the new decorator

def tag(*tags):
  # Define a new decorator, named "decorator", to return
  def decorator(func):
    # Ensure the decorated function keeps its metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
      # Call the function being decorated and return the result
      return func(*args, **kwargs)
    wrapper.tags = tags
    return wrapper
  # Return the new decorator
  return decorator

@tag('test', 'this is a tag')
def foo():
  pass

print(foo.tags)


#-------------------------------------------------------------------------------------------------------------

"""
Check the return type 

Python's flexibility around data types is usually cited as one of the benefits of the language. It can occasionally cause problems 
though if incorrect data types go unnoticed. You've decided that in order to make sure your code is doing exactly what you want it 
to do, you will explicitly check the return types of all of your functions and make sure they are what you expect them to be. To do 
that, you are going to create a decorator that checks that the return type of the decorated function is correct.

Note: assert(condition) is a function that you can use to test whether something is true. If condition is True, this function doesn't 
do anything. If condition is False, this function raises an error. The type of error that it raises is called an AssertionError.
"""

# Start by completing the returns_dict() decorator so that it raises an AssertionError if the return type of the decorated 
# function is not a dictionary.
def returns_dict(func):
  # Complete the returns_dict() decorator
  def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    assert(type(result) == dict)
    return result
  return wrapper

@returns_dict
def foo(value):
  return value

try:
  print(foo([1,2,3]))
except AssertionError:
  print('foo() did not return a dict!')
    
  
# Now complete the returns() decorator, which takes the expected return type as an argument.
def returns(return_type):
  # Write a decorator that raises an AssertionError if the
  # decorated function returns a value that is not return_type
  def decorator(func):
    def wrapper(*args, **kwargs):
      result = func(*args, **kwargs)
      assert(type(result) == return_type)
      return result
    return wrapper
  return decorator
  
@returns(dict)
def foo(value):
  return value

try:
  print(foo([1,2,3]))
except AssertionError:
  print('foo() did not return a dict!') 
  