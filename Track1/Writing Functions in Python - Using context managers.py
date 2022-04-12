
"""
Writing Functions in Python - Using context managers
"""

# A real world example of a context manager 

with open('my_file.txt') as my_file:
    text = my_file.read() 
    length = len(text) 
    
print('The file is {} characters long'.format(length)) 

# open() does three things:
#
# > Sets up a context by opening a file 
# > Lets you run any code you want on that file 
# > Removes the context by closing the file 


# The general formula/code for a context manager is:

with <context-manager>(<args>) as <variable-name>:
    # Run your code here
    # This code is running "inside the context"
    
# This code runs after the context is removed

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
    
"""
Writing Context Managers in Python 
"""

# the generic format is:

def my_context():
    # Add any set up code you need
    yield 
    # Add any teardown code you need 
    
"""
1. Define a Function 
2. (optional) Add any set up code your context needs 
3. Use the 'yield' keyword 
4. (optional) Add any teardown code your context needs 
"""

# Example code of a context manager that accesses a Database

@contextlib.contextmanager
def database(url):
    # set up database connection 
    db = postgres.connect(url)
    
    yield db 
    
    # tear down database connection 
    db.disconnect() 

# Then in use:
url = 'http://datacamp.com/data' 
with database(url) as my_db:
    course_list = my_db.execute(
        'SELECT * FROM courses'
    )
    
#-------------------------------------------------------------------------------
# Example of a "Read Only" context manager 
    
@contextlib.contextmanager
def open_read_only(filename):
  """Open a file in read-only mode.

  Args:
    filename (str): The location of the file to read

  Yields:
    file object
  """
  read_only_file = open(filename, mode='r')
  # Yield read_only_file so it can be assigned to my_file
  yield read_only_file
  # Close read_only_file
  read_only_file.close()

with open_read_only('my_file.txt') as my_file:
  print(my_file.read())
