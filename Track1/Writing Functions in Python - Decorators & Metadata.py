
"""
Writing Functions in Python - Decorators & Metadata 
"""

"""
Your friend has come to you with a problem. They've written some nifty decorators and added them to the functions in 
the open-source library they've been working on. However, they were running some tests and discovered that all of the 
docstrings have mysteriously disappeared from their decorated functions. Show your friend how to preserve docstrings 
and other metadata when writing decorators.
"""

from functools import wraps

def add_hello(func):
  # Decorate wrapper() so that it keeps func()'s metadata
  @wraps(func)
  def wrapper(*args, **kwargs):
    """Print 'hello' and then call the decorated function."""
    print('Hello')
    return func(*args, **kwargs)
  return wrapper
  
@add_hello
def print_sum(a, b):
  """Adds two numbers and prints the sum"""
  print(a + b)
  
print_sum(10, 20)
print(print_sum.__doc__)


"""
Why is all this important?

essentially, if we tried to see the docstrings of a function, that we have manipulated through a decorator, then nothing will be 
posted back.
In order to actually see the metadata of our function, even if we have manipulated it with a decorator, we can use wraps imported 
from the functools to help achieve this. 
"""
