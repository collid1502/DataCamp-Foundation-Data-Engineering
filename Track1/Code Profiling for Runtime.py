
"""
Code profiling for Runtime 
"""
# We saw previously, about using magic code %timeit - but for longer pieces of code, we need something 
# more substantial & efficient 

# Code profiling provides detailed stats on frequency & duration of function calls
# Line by line analysis 
# Package used: line_profiler 

conda install -c conda-forge spyder-line-profiler

pip install line_profiler 
import numpy as np 

# Example data for super heroes
heroes = ['Batman', 'Superman', 'Wonder Woman']

hts = np.array([188.0, 191.0, 183.0]) 
wts = np.array([95.0, 101.0, 74.0]) 

# so imagine we have a function for converting the data above 

def convert_units(heores, heights, weights):
    
    new_hts = [ht * 0.39370 for ht in heights] 
    new_wts = [wt * 2.20462 for wt in weights]
    
    hero_data = {} 
    
    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i]) 
        
    return hero_data 

# Now use defined function to convert data 
convert_units(heroes, hts, wts) 


# For code profiling using the line_profiler package, we would first need to load it in
%load_ext line_profiler 

# to then profile the created function 'convert_units' we would need to use:
%lprun -f convert_units convert_units(heroes, hts, wts) 
# %lprun is the syntax for line profiling, -f tells python we wish to do so to a function, then we set the function name to action on 
# you can now see the run time output to the console 

#--------------------------------------------------------------------------------------------------------------------------------------
#
# In the above code, we saw the bottleneck (long time to run) was the new_hts list comprehension 
# So, lets look at fixing it 

"""
In the previous exercise, you profiled the convert_units() function and saw that the new_hts list comprehension could be a potential bottleneck. 
Did you notice that the new_wts list comprehension also accounted for a similar percentage of the runtime? 
This is an indication that you may want to create the new_hts and new_wts objects using a different technique.

Since the height and weight of each hero is stored in a numpy array, you can use array broadcasting rather than list comprehension to 
convert the heights and weights. This has been implemented in the below function:
"""
def convert_units_broadcast(heroes, heights, weights):

    # Array broadcasting instead of list comprehension
    new_hts = heights * 0.39370
    new_wts = weights * 2.20462

    hero_data = {}

    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])

    return hero_data

convert_units_broadcast(heroes, hts, wts) 


# check the runtime with the line profiler 
%lprun -f convert_units_broadcast convert_units_broadcast(heroes, hts, wts)    # Can see from output now runs quicker 

