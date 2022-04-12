
"""
Examining Code Run Time
"""

# Say we wish to time how long it takes to run the following:

import numpy as np 
rand_nums = np.random.rand(0,1000) 

# we can time it bu using %timeit 

%timeit rand_nums = np.random.rand(0,1000) 

# In order to get a more accurate picture, rather than a one off, we can perform multiple 
# runs & loops to get the average run statistics. You'll see in the output from running the above, 
# the console print there were 7 runs and 1,000,000 loops 
# In using the timeit line magic function, we can specify the number of runs & loops

# Set number of runs to 2 (-r2) 
# Set number of loops to 10 (-n10) 

%timeit -r2 -n10 rand_nums = np.random.rand(0,1000) 

# We can also use time it in cell magic mode, aka, use it across multiple lines of code 

%%timeit
nums = []
for x in range(10):
    nums.append(x) 

# we can save the output of timeit to a variable, using the -o flag.

times = %timeit -o rand_nums = np.random.rand(0,1000) 
print(times) 


#---------------------------------------------------------------------------------------------------------------------------------------
# Some examples:

# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

# Create a list of integers (0-50) by unpacking range
nums_unpack = [*range(51)]
print(nums_unpack)

# Now, use timeit to identify which method was faster

%timeit nums_list_comp = [num for num in range(51)] 

%timeit nums_unpack = [*range(51)]   # This proved faster!!


#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
# Python allows you to create data structures using either a formal name or a literal syntax. In this exercise, you'll explore 
# how using a literal syntax for creating a data structure can speed up runtimes.
"""
Data Structure         Formal Name              Literal Syntax 

  list                  list()                     [] 
dictionary              dict()                     {} 
  tuple                tuple()                     ()
"""

# Example 

# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

# Print out the type of formal_list
print(type(formal_list))

# Print out the type of literal_list
print(type(literal_list))

"""
Both show class 'list' printed to the console 
"""
# Using %timeit to compare:

%timeit formal_list = list() 
%timeit literal_list = []     # Literal syntax is shown to be faster (times printed to console) 

#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
"""
From here on out, you'll be working with a superheroes dataset. For this exercise, a list of each hero's weight in kilograms 
(called wts) is loaded into your session. You'd like to convert these weights into pounds.

You could accomplish this using the below for loop:
"""
hero_wts_lbs = []
for wt in wts:
    hero_wts_lbs.append(wt * 2.20462)

# or  you could use a numpy array to accomplish this task: 
wts_np = np.array(wts)
hero_wts_lbs_np = wts_np * 2.20462   
    
"""
Use %%timeit in your IPython console to compare runtimes between these two approaches. Make sure to press SHIFT+ENTER after the 
magic command to add a new line before writing the code you wish to time. After you've finished coding, 
answer the following question:

Which of the above techniques is faster?
"""
%%timeit
    hero_wts_lbs = []
    for wt in wts:
        hero_wts_lbs.append(wt * 2.20462)
        
%%timeit  
     wts_np = np.array(wts)
     hero_wts_lbs_np = wts_np * 2.20462      
    
## Note - Using NUMPY would be fast, as it makes use of the broadcasting element 
    
    