
"""
Python Set Theory
"""

# Imagine we had two pokemon lists 

list_a = ['Bulbasaur', 'Charmander', 'Squirtle']
list_b = ['Caterpie', 'Pidgey', 'Squirtle'] 

# Imagine we wish to find the common pokemon from each list 

# we could do a loop method:
in_common = []
for pokemon_a in list_a:
    for pokemon_b in list_b:
            if pokemon_a == pokemon_b:
                in_common.append(pokemon_a) 
                
print(in_common)   # we can see Squirtle appears on both lists 

# However, iterating over each item in each list is extremely ineffcient, so we should instead use Python's Set Data Type to compare

# so, convert each list to a set type 
set_a = set(list_a) 
set_b = set(list_b) 

# we can then use the intersection method to compare each 
set_a.intersection(set_b)   # notice we get Squirtle out as expected 

# we can also use the set method to see pokemon that exist in one set, but not in the other 
set_a.difference(set_b) 
# Output = Bulbasaur & charmander from set a as they are not in set b 

# if we want to collect a pokemon that exists in either set a or b, but not both, we can use a method called symmetric difference
set_a.symmetric_difference(set_b) 
# see all pokemon except Squirtle are output 

# if we want to get all the unique pokemon from both sets, we can use the union method 
set_a.union(set_b) 

#-------------------------------------------------------------------------------------------------------------------

# Lets return to the example of the list of types for 720 pokemon 
# Imagine we want to find the unique types from this list 
# we could do a loop:

unique_types = []
for prim_type in primary_types:
    if prim_type not in unique_types:
        unique_types.append(prim_types) 
        
print(unique_types)


# However, using a set is much easier. A set by default is a unique list. So all we need do is convert the list into a set 
# and thus we will have all the uniqe types in an object 
unique_types_set = set(primary_types) 
print(unique_types_set) 
# This method is thus much more efficient 

# membership testing, we can do:

print('Squirtle' in list_a)  # True is posted to console 
print('Squirtle' in set_a)   # Also True (as expected) as posted to console

# if we were to check runtimes, we would see that member checking the set, rather than list, was quicker 
