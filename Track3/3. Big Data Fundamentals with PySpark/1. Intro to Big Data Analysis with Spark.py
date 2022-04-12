"""
Intro to Big Data analysis with PySpark
"""
# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------

"""
Use of the Lambda function in python - map() 
"""
# map() function takes a function and a list and returns a new list which contains items returned by that function for each item 
# general syntax of map():
#   map(function, list) 
#
# Example of map() 
items = [1,2,3,4]
list(map(lambda x: x + 2, items))   # This will now add 2 to each item on the original list and return the new list of 3,4,5,6

# -------------------------------------------------------------------------------------------------------------------------------

"""
Use of the Lambda function in python - filter() 
"""
# filter() function takes a function and a list and returns a new list for which the function evaluates as true 
# general syntax of filter():
#   filter(function, list)
#
# Example of filter() 
items2 = [1,2,3,4]
list(filter(lambda x: (x%2 != 0), items))  # This checks for odd numbers only. the % divides by the following number and checks for a remainder. So we are checking that any remainder from dividing by 2 is not equal to 0

