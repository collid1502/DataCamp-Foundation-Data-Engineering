
"""
Efficiently combining, counting and iterating 
"""

names = ['Bulbasaur', 'Charmander', 'Squirtle']  # Pokemon names 
hps = [45, 39, 44]   # corresponding Health Points Score 

# we can use Pythin's combined zip function to essentially merge these data points together into one list 

combined_zip = zip(names, hps) 
print(type(combined_zip)) 

# unpack it before printing 
combined_zip_list = [*combined_zip]
print(combined_zip_list) 


# you can also do this with slices, for example:

tester = [*zip(names[0:1], hps[0:1])] 
print(tester) 
# notice it only runs for the first index - aka Bulbasaur 

#---------------------------------------------------------------------------------------------------------------

# In order to get counts of items efficiently, we can use a counter function from the collections module 

# so imagine a list of pokemon types (720 in total) 
poke_types = ['Grass', 'Fire', 'Dark', ...] # etc. 
from collections import Counter 
type_counts = Counter(poke_types) 
print(type_counts) 

# Example Output will show something like:
#
#  'Water':105 , 'Normal':92, 'Fire':80   etc etc based on the list of 720 'types' above 
#

#------------------------------------------------------------------------------------------------

# combinations using itertools 

poke_types = ['Bug', 'Fire', 'Ghost', 'Grass', 'Water']
from itertools import combinations 
combos_obj = combinations(poke_types, 2) 
print(type(combos_obj)) 

combos = [*combos_obj]
print(combos)           # You will now see printed all the combinations of the values within poke_types list 

