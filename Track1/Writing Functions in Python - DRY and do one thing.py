
"""
Writing Functions in Python - DRY and "Do One Thing" 
"""

# DRY - aka Don't Repeat Yourself 


# If copy & pasting code, repeating chunks of code with minor changes, you can fall in to traps of 
# of forgetting to update certain variables etc.

# Best practice is to use functions to avoid repetition - like so:

def load_and_plot(path):
"""Load a data set and plot the first two principal components.
Args:
path (str): The location of a CSV file.
Returns:
tuple of ndarray: (features, labels)
"""
data = pd.read_csv(path)
y = data['label'].values
X = data[col for col in train.columns if col != 'label'].values
pca = PCA(n_components=2).fit_transform(X)
plt.scatter(pca[:,0], pca[:,1])
return X, y

train_X, train_y = load_and_plot('train.csv')
val_X, val_y = load_and_plot('validation.csv')
test_X, test_y = load_and_plot('test.csv')

# This way, we can use the read in & plot 3 times, without copy and pasting the code out 3 times (like a SAS Macro) 

#------------------------------------------------------------------
#
# The concept of Do One Thing is to keep functions simple - aka do one step only
# So:

def load_data(path):
"""Load a data set.
Args:
path (str): The location of a CSV file.
Returns:
tuple of ndarray: (features, labels)
"""
data = pd.read_csv(path)
y = data['labels'].values
X = data[col for col in data.columns
if col != 'labels'].values
return X, y

def plot_data(X):
"""Plot the first two principal components of a matrix
Args:
X (numpy.ndarray): The data to plot.
"""
pca = PCA(n_components=2).fit_transform(X)
plt.scatter(pca[:,0], pca[:,1]) 

"""
Advantages of 'Do One Thing'

The code becomes:
    > More flexible 
    > More easily understood 
    > Simpler to test 
    > Simpler to debug 
    > Easier to change 
"""

#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

# Example Function 
"""
While you were developing a model to predict the likelihood of a student graduating from college, you wrote this bit of code 
to get the z-scores of students' yearly GPAs. Now you're ready to turn it into a production-quality system, so you need to do 
something about the repetition. Writing a function to calculate the z-scores would improve this code.

# Standardize the GPAs for each year
df['y1_z'] = (df.y1_gpa - df.y1_gpa.mean()) / df.y1_gpa.std()
df['y2_z'] = (df.y2_gpa - df.y2_gpa.mean()) / df.y2_gpa.std()
df['y3_z'] = (df.y3_gpa - df.y3_gpa.mean()) / df.y3_gpa.std()
df['y4_z'] = (df.y4_gpa - df.y4_gpa.mean()) / df.y4_gpa.std()
"""

def standardize(column):
  """Standardize the values in a column.

  Args:
    column (pandas Series): The data to standardize.

  Returns:
    pandas Series: the values as z-scores
  """
  # Finish the function so that it returns the z-scores
  z_score = (column - column.mean()) / column.std()
  return z_score

# Use the standardize() function to calculate the z-scores
df['y1_z'] = standardize(df.y1_gpa)
df['y2_z'] = standardize(df.y2_gpa)
df['y3_z'] = standardize(df.y3_gpa)
df['y4_z'] = standardize(df.y4_gpa)

