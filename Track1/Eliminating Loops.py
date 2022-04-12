
"""
Eliminating Loops
"""

# List of HP, Attack, Defence & Speed (pokestats) 
poke_stats = [
    [90, 92, 75, 60],
    [25, 20, 15, 90],
    [65, 130, 60, 75]
]

# each row is a pokemon, each column is the value of the stat 

# to collect totals, we could use a For Loop method:
totals = []
for row in poke_stats:
    totals.append(sum(row)) 
    
print(totals) 


# we could accomplish the same task, in fewer lines of code, with list comprehension 
totals_comp = [sum(row) for row in poke_stats]
print(totals_comp) 

# or we could use the built in map function (this would be faster/more efficient than a loop) 
totals_map = [*map(sum, poke_stats)] 
print(totals_map) 

#------------------------------------------------------------------------------------------------------------

# Using NUMPY instead, which is more efficient that loops 
import numpy as np 

# build stats as an array 
poke_stats = np.array([
    [90, 92, 75, 60],
    [25, 20, 15, 90],
    [65, 130, 60, 75]
])

# if we wanted to calculate a mean for each row, we could then do (rather than an intensive loop):
avgs_np = poke_stats.mean(axis=1) 
print(avgs_np) 


#-----------------------------------------------------------------------------------------
# Example code from exercise replacing a loop function :

# Collect Pokémon that belong to generation 1 or generation 2
gen1_gen2_pokemon = [name for name,gen in zip(poke_names, poke_gens) if gen < 3]

# Create a map object that stores the name lengths
name_lengths_map = map(len, poke_names)

# Combine gen1_gen2_pokemon and name_lengths_map into a list
gen1_gen2_name_lengths = [*zip(gen1_gen2_pokemon, name_lengths_map)]

print(gen1_gen2_name_lengths_loop[:5])
print(gen1_gen2_name_lengths[:5])

#----------------------------------------------------------------------------------------
# Example code for collecting total & avg stats for each pokemon in a dataset
# Create a total stats array
total_stats_np = stats.sum(axis=1)

# Create an average stats array
avg_stats_np = stats.mean(axis=1)

# Combine names, total_stats_np, and avg_stats_np into a list
poke_list_np = [*zip(names, total_stats_np, avg_stats_np)]

print(poke_list_np == poke_list, '\n')
print(poke_list_np[:3])
print(poke_list[:3], '\n')
top_3 = sorted(poke_list_np, key=lambda x: x[1], reverse=True)[:3]
print('3 strongest Pokémon:\n{}'.format(top_3))
