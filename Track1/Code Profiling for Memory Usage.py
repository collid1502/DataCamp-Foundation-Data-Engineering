
"""
Code Profiling for Memory Usage 
"""

# a quick & dirty appraoch for memory consumption checks is Pythons built in module, sys 
import sys 

# for example, we can get the size of an object in bytes, such as:
nums_list = [*range(0,1000)]
sys.getsizeof(nums_list)    # output was 4560 bytes to console 

# or 

import numpy as np 

nums_np = np.array(range(0,1000)) 
sys.getsizeof(nums_np)    # output was 4048 bytes to console 


"""
Code Profiling: Memory 

> detailed stats on memory consumption 
> line by line analysis 
> package used: memory_profiler 
"""

# using memory_profiler package:

pip install memory_profiler 

%load_ext memory_profiler 

# syntax for use is much like %lprun was:
%mprun -f convert_units convert_units(heroes, hts, wts) 

# NB ~ %mprun can only be used on physical files imported & not those created in the IPython session

# so, for example:
# we import a created function from file hero_funcs.py 

from hero_funcs import convert_units 
%load_ext memory_profiler 
%mprun -f convert_units convert_units(heroes, hts, wts)  


