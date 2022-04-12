
"""
Intro to Pandas DataFrame iteration 
"""

# Pandas is a library for used for data analysis 
# Main data structure is the DataFrame 
#   > Tabular data with labelled rows & columns 
#   > Built on top of the NumPy array structure 

import pandas as pd 

baseball_df = pd.read_csv(r"C:\Users\Dan\Desktop\Work\Python\DataCamp - Data Engineering\Track1\baseball_stats.csv") # add r to make string raw 
print(baseball_df.head()) 

# calculating teams win percentage 

import numpy as np 

def calc_win_perc(wins, games_played):
    win_perc = wins / games_played 
    return np.round(win_perc,2) 


# so, we wish to add a win percentage column to our dataframe (dataset)
# To do this, we need to iterate a calculation over all rows in the dataframe 
    
win_perc_list = []  # empty list to store the calculated win percentages 

for i in range(len(baseball_df)):    # creates a loop from 0 to the number of rows in the dataframe, setting the ndex variable as i
    row = baseball_df.iloc[i]        # then uses iloc to identify each individual row from the index value 
    wins = row['W']                  # assigns the value from W to our variable 'wins'
    games_played = row['G']          # assigns the value from G to our variable 'games_played' 
    win_perc = calc_win_perc(wins, games_played)  # uses the above defined function, to utilise the two variables just set, and create a calc
    win_perc_list.append(win_perc)    # appends each result from the calculation into the empty list we created earlier 
    
baseball_df['WP'] = win_perc_list   # we create our desired column in the dataframe and set equal to the win percentage list 

# now, print the first 5 rows again 
print(baseball_df.head())   # we can see WP (win percentage) has been added to our dataframe 


#-----------------------------------------------------------------------------------------------------------
#
# a more efficient method would be to utilise pandas.interrows() method 
# it returns each row, with that rows index as the first variable, and the rows data as the second variable 
#

win_perc_list = []

for i,row in baseball_df.iterrows():   # so .iterrows() handles the indexing for us 
     wins = row['W']                  
    games_played = row['G']          
    win_perc = calc_win_perc(wins, games_played)  
    win_perc_list.append(win_perc)  
      
baseball_df['WP'] = win_perc_list

#-----------------------------------------------------------------------------------------------------------
#
# Example code for Lesson exercises:
#
"""
In the video, we discussed that .iterrows() returns each DataFrame row as a tuple of (index, pandas Series) pairs. But, what does this mean? 
Let's explore with a few coding exercises.

A pandas DataFrame has been loaded into your session called pit_df. This DataFrame contains the stats for the Major League Baseball 
team named the Pittsburgh Pirates (abbreviated as 'PIT') from the year 2008 to the year 2012. It has been printed into your console 
for convenience.
"""

# Iterate over pit_df and print each row
for i,row in pit_df.iterrows():
    print(row)
    
# Iterate over pit_df and print each index variable and then each row
for i,row in pit_df.iterrows():
    print(i)
    print(row)
    print(type(row)) 
    
# Use one variable instead of two to store the result of .iterrows()
for row_tuple in pit_df.iterrows():
    print(row_tuple)   

# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(row_tuple)
    print(type(row_tuple)) 

#-----------------------------------------------------------------------------------------------------------
# More example code:
# Create an empty list to store run differentials
run_diffs = []

# Write a for loop and collect runs allowed and runs scored for each row
for i,row in giants_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']
    
    # Use the provided function to calculate run_diff for each row
    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    # Append each run differential to the output list
    run_diffs.append(run_diff)

giants_df['RD'] = run_diffs
print(giants_df)
    
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

"""
Another iterator method: itertuples() 
"""

# we could use .itertuples to loop over our dataframe instead (Example from slides) 
for row_namedtuple in team_wins_df.itertuples():
    print(row_namedtuple) 
    
    
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

"""
Pandas alternative to Looping 
"""    
# an alternative to iterative looping, is to use the pandas.apply() method 
#   > It takes a function and applies it to a DataFrame 
#   > Must specify axis to apply function to (0 for columns, 1 for rows)
# Can be used with anonymous functions (lambda functions) 

# Example of the baseball_df dataset

run_diffs_apply = baseball_df.apply(
    lambda row: calc_run_diff(row['RS'], row['RA']),  # so we are basically collecting RS & RA for each row, then passing them to our earlier created run differentials function 
    axis=1  # specifies to operate on rows 
)
# This means we won't don't need to use a For loop
# And we can just specify the new column like we would have before 

baseball_df['RD'] = runs_diff_apply 
print(baseball_df.head()) 

# The above method will be much more efficient / fast 

#--------------------------------------------------------------------
# Examples from coding exercises :

# Gather sum of all columns
stat_totals = rays_df.apply(sum, axis=0)
print(stat_totals)

# Gather total runs scored in all games per year
total_runs_scored = rays_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored)

# Convert numeric playoffs to text
textual_playoffs = rays_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

"""
Optimal Pandas Iterating
"""

# Using pandas, we can use simple dot notation from arrays, such as:
# in the Baseball dataframe we loaded in 

wins_np = baseball_df['W'].values   # we have now assigned the values in the W column from baseball_df to the variable wins_np 
print(type(wins_np))  # we can see the type created for this 'variable' is a numpy array 

# verify contents 
print(wins_np)


# The arrays 'broadcasting' facility is bsically vectorisation (think Data Step in SAS). It allows you to efficiently apply 
# methods/steps to all data in an array at once, rather than processing loops etc. etc. 

# This means we can perform calculations on the underlying numpy arrays within our dataframe 
# for example:
"""
run_diffs_np = baseball_df['RS'].values - baseball_df['RA'].values    (to calculate the run differential)
"""
# so, let's run this calc, add the column to our baseball dataframe & print the results 

run_diffs_np = baseball_df['RS'].values - baseball_df['RA'].values     # create the calc of the run diff values 
baseball_df['RD'] = run_diffs_np                                       # set up a new column in dataset and set calc values into it 
print(baseball_df)                                                     # View results 


#-------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
"""
Exercise using the Baseball DF 

A pandas DataFrame (baseball_df) has been loaded into your session. For convenience, a dictionary describing each column 
within baseball_df has been printed into your console. You can reference these descriptions throughout the exercise.

You'd like to attempt to predict a team's win percentage for a given season by using the team's total runs scored in a season 
('RS') and total runs allowed in a season ('RA') with the following function:
    
def predict_win_perc(RS, RA):
    prediction = RS ** 2 / (RS ** 2 + RA ** 2)
    return np.round(prediction, 2)
    
Let's compare the approaches you've learned to calculate a predicted win percentage for each season (or row) in your DataFrame.
"""

# Part 1 
# Use a for loop and .itertuples() to predict the win percentage for each row of baseball_df with the predict_win_perc() function. 
# Save each row's predicted win percentage as win_perc_pred and append each to the win_perc_preds_loop list.

win_perc_preds_loop = []

# Use a loop and .itertuples() to collect each row's predicted win percentage
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)


# Part 2 
# Apply predict_win_perc() to each row of the baseball_df DataFrame using a lambda function. 
# Save the predicted win percentage as win_perc_preds_apply.

# Apply predict_win_perc to each row of the DataFrame
win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)


# Part 3 
# Calculate the predicted win percentages by passing the underlying 'RS' and 'RA' arrays from baseball_df into predict_win_perc(). 
# Save these predictions as win_perc_preds_np.

# Calculate the win percentage predictions using NumPy arrays
win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)
baseball_df['WP_preds'] = win_perc_preds_np
print(baseball_df.head())

"""
Of the 3 methods above, using the Numpy array (part 3) method would be the quickest if we timed them with the magic command %%timeit
in the IPython console
"""
