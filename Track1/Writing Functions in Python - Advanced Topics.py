
"""
Writing Functions in Python - Advance Topics
"""

# Nested Contexts 

def copy(src, dst):
    """Copy the contents of one file to another.
    
    Args:
    src (str): File name of the file to be copied.
    dst (str): Where to write the new file.
    """
    # Open the source file and read in the contents
    with open(src) as f_src:
        contents = f_src.read()
        
    # Open the destination file and write out the contents
    with open(dst, 'w') as f_dst:
        f_dst.write(contents)


# The above method would work fine for copying a file from one location into another, unless, it's such a 
# large file, that we run out of memory space to read it in and hold it, before writing back out.
    
# To deal with this, we could do a line at a time over a for loop:
def copy(src, dst):
    """Copy the contents of one file to another.
    
    Args:
    src (str): File name of the file to be copied.
    dst (str): Where to write the new file.
    """
    # Open both files
    with open(src) as f_src:
        with open(dst, 'w') as f_dst:
            # Read and write each line, one at a time
            for line in f_src:
                f_dst.write(line)   


#--------------------------------------------------------------------------------------
                
"""
Handling Errors
"""

def get_printer(ip):
    p = connect_to_printer(ip)
    
    yield
    
    # This MUST be called or no one else will
    # be able to connect to the printer
    p.disconnect()
    print('disconnected from printer')
    
doc = {'text': 'This is my text.'}       # this line would cause an error - as it uses 'text' rather than 'txt' 

with get_printer('10.0.34.111') as printer:
    printer.print_page(doc['txt'])

# This means p.disconnect() doesn't get called - and thus, no one else can connect to the printer, as this connection is still open 
    
    
# so when Handling Errors:
"""
try:
    # code that might raise an error
    
except:
    # do something about the error
    
finally:
    # this code runs no matter what 
"""

# So as a solution to the above problem, we could include a try & finally statement as follows:

def get_printer(ip):
    p = connect_to_printer(ip)
    
    try:
        yield 
    finally:
        p.disconnect()
        print('disconnected from printer') 
        
# so now, when the programmer runs:
doc = {'text': 'This is my text.'}        

with get_printer('10.0.34.111') as printer:
    printer.print_page(doc['txt'])     

# we still get the error, but finally esnures the disconnect is called before the error is raised to the user 
    
#--------------------------------------------------------------------------------------
"""
Exercise 

Training deep neural nets is expensive! You might as well invest in NVIDIA stock since you're spending so much on GPUs. 
To pick the best time to invest, you are going to collect and analyze some data on how their stock is doing. 
The context manager stock('NVDA') will connect to the NASDAQ and return an object that you can use to get the latest 
price by calling its .price() method.

You want to connect to stock('NVDA') and record 10 timesteps of price data by writing it to the file NVDA.txt.
"""

# Use the stock('NVDA') context manager and assign the result to nvda.
# Open a file for writing with open('NVDA.txt', 'w') and assign the file object to f_out so you can record the price over time.
# Use the "stock('NVDA')" context manager
# and assign the result to the variable "nvda"

with stock('NVDA') as nvda:
  # Open 'NVDA.txt' for writing as f_out
  with open('NVDA.txt', 'w') as f_out:
    for _ in range(10):
      value = nvda.price()
      print('Logging ${:.2f} for NVDA'.format(value))
      f_out.write('{:.2f}\n'.format(value))
      