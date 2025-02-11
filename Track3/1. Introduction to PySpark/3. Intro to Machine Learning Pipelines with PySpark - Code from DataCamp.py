
"""
Topic: Intro to Machine Learning Pipelines
"""
#----------------------------------------------------------------------------------------------------------------------------------
"""
Machine Learning Pipelines

At the core of the pyspark.ml module are the Transformer and Estimator classes. Almost every other class in the module behaves similarly to these two basic classes.

Transformer classes have a .transform() method that takes a DataFrame and returns a new DataFrame; usually the original one with a new column appended. For example, you might use the 
class Bucketizer to create discrete bins from a continuous feature or the class PCA to reduce the dimensionality of your dataset using principal component analysis.

Estimator classes all implement a .fit() method. These methods also take a DataFrame, but instead of returning another DataFrame they return a model object. 
This can be something like a StringIndexerModel for including categorical data saved as strings in your models, or a RandomForestModel that uses the random forest algorithm for classification or regression.
"""
# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------

"""
Join the DataFrames 

you'll be working to build a model that predicts whether or not a flight will be delayed based on the flights data we've been working with. 
This model will also include information about the plane that flew the route, so the first step is to join the two tables: flights and planes!
"""

# Rename year column to plane_year
planes = planes.withColumnRenamed("year", "plane_year")

# Join the DataFrames
model_data = flights.join(planes, on="tailnum", how="leftouter")

# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------

"""
Data Types 

Before you get started modeling, it's important to know that Spark only handles numeric data. That means all of the columns in your DataFrame must be either integers or decimals (called 'doubles' in Spark).

When we imported our data, we let Spark guess what kind of information each column held. Unfortunately, Spark doesn't always guess right and you can see that some of the columns in our DataFrame are strings 
containing numbers as opposed to actual numeric values.
To remedy this, you can use the .cast() method in combination with the .withColumn() method. It's important to note that .cast() works on columns, while .withColumn() works on DataFrames.
The only argument you need to pass to .cast() is the kind of value you want to create, in string form. For example, to create integers, you'll pass the argument "integer" and for decimal numbers you'll use "double".
You can put this call to .cast() inside a call to .withColumn() to overwrite the already existing column
"""
# Cast the columns to integers
model_data = model_data.withColumn("arr_delay", model_data.arr_delay.cast("integer"))
model_data = model_data.withColumn("air_time", model_data.air_time.cast("integer"))
model_data = model_data.withColumn("month", model_data.month.cast("integer"))
model_data = model_data.withColumn("plane_year", model_data.plane_year.cast("integer"))

# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------

"""
Create a new column 

In the last exercise, you converted the column plane_year to an integer. This column holds the year each plane was manufactured. 
However, your model will use the planes' age, which is slightly different from the year it was made!
Create the column plane_age using the .withColumn() method and subtracting the year of manufacture (column plane_year) from the year (column year) of the flight.
"""
# Create the column plane_age
model_data = model_data.withColumn("plane_age", model_data.year - model_data.plane_year)

# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------

"""
Making a Boolean

Consider that you're modeling a yes or no question: is the flight late? However, your data contains the arrival delay in minutes for each flight. 
Thus, you'll need to create a boolean column which indicates whether the flight was late or not!
"""
# Create is_late
model_data = model_data.withColumn("is_late", model_data.arr_delay > 0)

# Convert to an integer
model_data = model_data.withColumn("label", model_data.is_late.cast("integer"))

# Remove missing values
model_data = model_data.filter("arr_delay is not NULL and dep_delay is not NULL and air_time is not NULL and plane_year is not NULL")

# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------

"""
Strings & Factors

As you know, Spark requires numeric data for modeling. So far this hasn't been an issue; even boolean columns can easily be converted to integers without any trouble. 
But you'll also be using the airline and the plane's destination as features in your model. These are coded as strings and there isn't any obvious way to convert them to a numeric data type.

Fortunately, PySpark has functions for handling this built into the pyspark.ml.features submodule. You can create what are called 'one-hot vectors' to represent the carrier and the destination of each flight. 
A one-hot vector is a way of representing a categorical feature where every observation has a vector in which all elements are zero except for at most one element, which has a value of one (1).

Each element in the vector corresponds to a level of the feature, so it's possible to tell what the right level is by seeing which element of the vector is equal to one (1).

The first step to encoding your categorical feature is to create a StringIndexer. Members of this class are Estimators that take a DataFrame with a column of strings and map each unique string to a number. 
Then, the Estimator returns a Transformer that takes a DataFrame, attaches the mapping to it as metadata, and returns a new DataFrame with a numeric column corresponding to the string column.

The second step is to encode this numeric column as a one-hot vector using a OneHotEncoder. This works exactly the same way as the StringIndexer by creating an Estimator and then a Transformer. 
The end result is a column that encodes your categorical feature as a vector that's suitable for machine learning routines!

This may seem complicated, but don't worry! All you have to remember is that you need to create a StringIndexer and a OneHotEncoder, and the Pipeline will take care of the rest.
"""

# In this exercise you'll create a StringIndexer and a OneHotEncoder to code the carrier column. To do this, you'll call the class constructors with the arguments inputCol and outputCol.
# The inputCol is the name of the column you want to index or encode, and the outputCol is the name of the new column that the Transformer should create.

# Create a StringIndexer
carr_indexer = StringIndexer(inputCol="carrier", outputCol="carrier_index")

# Create a OneHotEncoder
carr_encoder = OneHotEncoder(inputCol="carrier_index", outputCol="carrier_fact")

# Now you'll encode the dest column just like you did above
# Create a StringIndexer
dest_indexer = StringIndexer(inputCol="dest", outputCol="dest_index")

# Create a OneHotEncoder
dest_encoder = OneHotEncoder(inputCol="dest_index", outputCol="dest_fact")

# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------

"""
Assemble a vector 

The last step in the Pipeline is to combine all of the columns containing our features into a single column. 
This has to be done before modeling can take place because every Spark modeling routine expects the data to be in this form. 
You can do this by storing each of the values from a column as an entry in a vector. Then, from the model's point of view, every 
observation is a vector that contains all of the information about it and a label that tells the modeler what value that observation corresponds to.

Because of this, the pyspark.ml.feature submodule contains a class called VectorAssembler. This Transformer takes all of the columns you specify and 
combines them into a new vector column.
"""

# Make a VectorAssembler
vec_assembler = VectorAssembler(inputCols=["month", "air_time", "carrier_fact", "dest_fact", "plane_age"], outputCol="features")

# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------

"""
Create the pipeline

Pipeline is a class in the pyspark.ml module that combines all the Estimators and Transformers that you've already created. 
This lets you reuse the same modeling process over and over again by wrapping it up in one simple object.
"""
# Import Pipeline from pyspark.ml
from pyspark.ml import Pipeline

# Call the Pipeline() constructor with the keyword argument 'stages' to create a Pipeline called flights_pipe.
# 'stages' should be a list holding all the stages you want your data to go through in the pipeline.
flights_pipe = Pipeline(stages=[dest_indexer, dest_encoder, carr_indexer, carr_encoder, vec_assembler])

# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------

"""
Test vs Train 

After you've cleaned your data and gotten it ready for modeling, one of the most important steps is to split the data into a test set and a train set. 
After that, don't touch your test data until you think you have a good model! As you're building models and forming hypotheses, you can test them on 
your training data to get an idea of their performance.

Once you've got your favorite model, you can see how well it predicts the new data in your test set. This never-before-seen data will give you a much 
more realistic idea of your model's performance in the real world when you're trying to predict or classify new data.

In Spark it's important to make sure you split the data after all the transformations. This is because operations like StringIndexer don't always produce 
the same index even when given the same list of strings.
"""

# ---------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------

"""
Transform the data 

Create the DataFrame piped_data by calling the Pipeline methods .fit() and .transform() in a chain. 
Both of these methods take model_data as their only argument.
"""

# Fit and transform the data
piped_data = flights_pipe.fit(model_data).transform(model_data)


"""
Split the data

After all your manipulations, the last step before modeling is to split the data!
Use the DataFrame method .randomSplit() to split piped_data into two pieces.
Training with 60% of the data, and Test with 40% of the data by passing the list [.6, .4] to the .randomSplit() method.
"""
# Split the data into training and test sets
training, test = piped_data.randomSplit([.6, .4])


# end #