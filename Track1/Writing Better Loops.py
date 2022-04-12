
"""
Writing Better Loops
"""

names = ['Pikachu', 'Squirtle', 'Articuno']
legend_status = [False, False, True]
generations = [1 ,1, 1]

# to create a list of 'lists' aka, a list of each of the corresponding data points together we can do:

poke_data = []
for poke_tuple in zip(names, legend_status, generations):
    poke_list = list(poke_tuple) 
    poke_data.append(poke_list)
    
print(poke_data) 
                 
# The current loop is having to perform a tuple to list conversion in each iteration 

# A more efficient approach, would be to move this outside the loop and perform afterwards, via a map function 
poke_data_tuples = []
for poke_tuple in zip(names, legend_status, generations):
    poke_data_tuples.append(poke_tuple) 
    
poke_data = [*map(list, poke_data_tuples)] 
print(poke_data) 

#----------------------------------------------------------------------------------------------------------------------------
# Example code for writing a better loop (in exercise) 

# Collect all possible pairs using combinations()
possible_pairs = [*combinations(pokemon_types, 2)]

# Create an empty list called enumerated_tuples
enumerated_tuples = []

# Add a line to append each enumerated_pair_tuple to the empty list above
for i,pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_tuples.append(enumerated_pair_tuple)

# Convert all tuples in enumerated_tuples to a list
enumerated_pairs = [*map(list, enumerated_tuples)]
print(enumerated_pairs)


#----------------------------------------------------------------------------------------------------------------------------
"""
A list of 720 Pokémon has been loaded into your session as names. Each Pokémon's corresponding Health Points is stored in a 
NumPy array called hps. You want to analyze the Health Points using the z-score to see how many standard deviations each 
Pokémon's HP is from the mean of all HPs.

The below code was written to calculate the HP z-score for each Pokémon and gather the Pokémon with the highest HPs based 
on their z-scores:
    
poke_zscores = []

for name,hp in zip(names, hps):
    hp_avg = hps.mean()
    hp_std = hps.std()
    z_score = (hp - hp_avg)/hp_std
    poke_zscores.append((name, hp, z_score))
highest_hp_pokemon = []

for name,hp,zscore in poke_zscores:
    if zscore > 2:
        highest_hp_pokemon.append((name, hp, zscore))  
    
"""

# Use NumPy to eliminate the for loop used to create the z-scores.
# Then, combine the names, hps, and z_scores objects together into a list called poke_zscores2

# Calculate the total HP avg and total HP standard deviation
hp_avg = hps.mean()
hp_std = hps.std()

# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std

# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')

# Use list comprehension with the same logic as the highest_hp_pokemon code block
highest_hp_pokemon2 = [(name, hp, zscore) for name,hp,zscore in poke_zscores2 if zscore > 2]
print(*highest_hp_pokemon2, sep='\n')
