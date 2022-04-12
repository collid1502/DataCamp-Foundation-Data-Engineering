
"""
The power of NumPy Arrays 

NumPy - Numerical Python 
"""

# Python arrays provide a fast & more efficient alternative to Python Lists 
nums_list = list(range(5)) 
print(nums_list) 


import numpy as np 
nums_np = np.array(range(5)) 
print(nums_np) 


# Arrays are homogenous - so each data point needs to be the same type in the array 
# if we created and array with the following 3 values:  1, 2.5, 3
# then python would convert the 1 to 1.  and the 3 to 3. (aka change them to a float) in order to maintain float dtype array wide 
nums_np_floats = np.array([1, 2.5, 3]) 
print(nums_np_floats) 



# EXAMPLE - say we wanted to create a list of squared values of another list of numbers 
nums = [-2, -1, 0, 1, 2] 

# For Loop (inefficent approach) 
sqrd_nums = []
for num in nums:
    sqrd_nums.append(num ** 2)
print(sqrd_nums) 

# or using a list comprehension (better option but not best) 
sqrd_nums = [num ** 2 for num in nums] 
print(sqrd_nums) 

# However, using an array is most efficient 
nums_np = np.array([-2, -1, 0, 1, 2])  
nums_np ** 2 


# 2-D list 
nums2 = [[1,2,3],
         [4,5,6]]

# 2-D Array 
nums2_np = np.array(nums2) 


# To do basic indexing, if we were to find the value '2' from the nums2 list, we would have to do row 0, column 1 
nums2[0][1] 

# but for the array we would do:
nums2_np[0,1]

# To collect all the items in the first column, for the List approach:
[row[0] for row in nums2] 

# for the Array :
nums2_np[:,0] 


# NumPy arrays alos allow Boolean indexing 
# for example:
nums = [-2, -1, 0, 1, 2] 
nums_np = np.array(nums) 

nums_np > 0   # This returns a False or True statement in each index position if the relevant value meets the condition 


#########################################################################################

## Let's Practice 
##
"""
Let's practice slicing numpy arrays and using NumPy's broadcasting concept. Remember, broadcasting refers to a numpy array's 
ability to vectorize operations, so they are performed on all elements of an object at once.

A two-dimensional numpy array has been loaded into your session (called nums) and printed into the console for your convenience. 
"""

# Print second row of nums
print(nums[1,:])

# Print all elements of nums that are greater than six
print(nums[nums > 6])

# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)

# Replace the third column of nums
nums[:,2] = nums[:,2] + 1
print(nums)



"""
 In this exercise, you will be throwing a party—a Festivus if you will!

You have a list of guests (the names list). Each guest, for whatever reason, has decided to show up to the party 
in 10-minute increments. For example, Jerry shows up to Festivus 10 minutes into the party's start time, Kramer shows 
up 20 minutes into the party, and so on and so forth.

We want to write a few simple lines of code, using the built-ins we have covered, to welcome each of your guests and 
let them know how many minutes late they are to your party. Note that numpy has been imported into your session as np 
and the names list has been loaded as well.

Let's welcome your guests!
"""

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']  

# Create a list of arrival times
arrival_times = [*range(10, 60, 10)]
print(arrival_times)

# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3
print(new_times)

# Create a list of arrival times
arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i],time) for i,time in enumerate(new_times)]
print(guest_arrivals)


"""
A function named welcome_guest() has been pre-loaded into your session. Use map() to apply this function to 
each element of the guest_arrivals list and save it as the variable welcome_map
"""
# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(*guest_welcomes, sep='\n')

