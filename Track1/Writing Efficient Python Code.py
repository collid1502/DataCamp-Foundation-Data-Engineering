
"""
Writing Efficient Python Code


The goal is to wirte code that has:
    1) Minimal completion time (fast runtime)
    2) Minimal resource consumption (small memory footprint) 
"""

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman'] 

# Print the list created using the Non-Pythonic approach
i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1
print(new_list)



# A more pythonic approach would be to loop over the contents of 'names' rather than using an index variable. 
# we will call this 'better_list' 

# Print the list created by looping over the contents of names
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)


# The best Pythonic method would be to use list comprehension 
# call this 'best_list' 

# Print the list created by using list comprehension
best_list = [name for name in names if len(name) >= 6]
print(best_list)


# collect the Zen of Python {Python Enchancement Proposals / PEP} 
import this 

#####################################################################################################################################

"""
Python built in functions 
"""
# range(start,stop)
nums = range(0,11)  # prints numbers 0 to 10 
nums_list = list(nums)
print(nums_list) 

# or, could use range(stop)  assuming we wish to start from 0 
nums = range(11)  # prints numbers 0 to 10 
nums_list = list(nums)
print(nums_list) 

# range can also except a start, stop & step value, for example:
even_nums = range(2, 11, 2) # even numbers between 1 & 10 
even_nums_list = list(even_nums)
print(even_nums_list) 


# enumerate() creates an indexed list of objects (remember, indexing starts at zero) 
letters = ['a','b','c','d']
indexed_letters = enumerate(letters)
indexed_letters_list = list(indexed_letters)
print(indexed_letters_list) 


# we can tell Python where to start the index if we like though, using a start= option 
indexed_letters = enumerate(letters, start=5)  # note the indexes are now > 5,6,7,8
indexed_letters_list = list(indexed_letters)
print(indexed_letters_list)


# the map() function applies a function over an object 
nums = [1.5, 2.3, 3.4, 4.6, 5.0] 
rnd_nums = map(round, nums) 
print(list(rnd_nums)) 

# map() can also be used with a lamda {anonymous function} 
nums = [1,2,3,4,5]
sqrd_nums = map(lambda x: x ** 2, nums)
print(list(sqrd_nums)) 


# NB ~ we can also create a range list by 'unpacking' a range object, with the * key. 
# for example, create a list of the odd numbers between 1 & 11 
nums_odd = [*range(1,12,2)]
print(nums_odd) 

###################################################################################


"""
Example Problems

In this exercise, you'll practice using Python's built-in function enumerate(). This function is useful for obtaining an indexed list. 
For example, suppose you had a list of people that arrived at a party you are hosting. 
The list is ordered by arrival (Jerry was the first to arrive, followed by Kramer, etc.):
    
If you wanted to attach an index representing a person's arrival order, you could use the following for loop:

indexed_names = []
for i in range(len(names)):
    index_name = (i, names[i])
    indexed_names.append(index_name)

[(0,'Jerry'),(1,'Kramer'),(2,'Elaine'),(3,'George'),(4,'Newman')]

"""

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman'] 

# Rewrite the for loop to use enumerate
indexed_names = []
for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)


"""
In this exercise, you'll practice using Python's built-in map() function to apply a function to every element of an object. 
Let's look at a list of party guests:

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
Suppose you wanted to create a new list (called names_uppercase) that converted all the letters in each name to uppercase. 
you could accomplish this with the below for loop:

names_uppercase = []

for name in names:
  names_uppercase.append(name.upper())

['JERRY', 'KRAMER', 'ELAINE', 'GEORGE', 'NEWMAN']
Let's explore using the map() function to do this more efficiently in one line of code.
"""

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman'] 

# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)

# Print the type of the names_map
print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*list(names_map)]

# Print the list created above
print(names_uppercase)

