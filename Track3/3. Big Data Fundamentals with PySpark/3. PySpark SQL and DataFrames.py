"""
Introduction to PySpark SQL & DataFrames
"""
# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------

# So like SparkContext (sc) was the entry point for RDDs, SparkSession is the API entry point for working with Data Frames.
# can be used to create dataframes, register dataframes and execute SQL queries
# SparkSession is available in PySpark shell as 'spark'
#
# Two different methods for creating DataFrames in PySpark
#   1) from existing RDDs using SparkSession's createDataFrame() method 
#   2) from various data sources (CSV,JSON,TXT etc.) using SparkSession's read method 
#
# Schema controls the data and helps dataframes to optimise queries 
# Schema provides information about column name, type of data in column, empty/null values etc 

# create a dataframe from RDD
iphones_RDD = sc.parallelize([
    ('XS', 2018, 5.65, 2.19, 6.24),
    ('XR', 2018, 5.94, 2.98, 6.84),
    ('X10', 2017, 6.65, 2.79, 6.13),
    ('8Plus', 2017, 6.23, 3.07, 7.12) 
    ])

names = ['Model', 'Year', 'Height', 'Width', 'Weight']

iphones_df = spark.createDataFrame(iphones_RDD, schema=names) 


# create a dataframe from reading a CSV/JSON/TXT file
df_csv = spark.read.csv("people.csv", header=True, inferSchema=True) 
df_json = spark.read.json("people.json", header=True, inferSchema=True) 
df_txt = spark.read.txt("people.txt", header=True, inferSchema=True) 

# ---------------------------------------------------------------------------------------------------------------

"""
Common DataFrame operators in PySpark

common dataframe transformations ~ select(), filter(), groupby(), orderby(), dropDuplicates(), withColumnRenamed() 
common dataframe actions         ~ printSchema(), head(), show(), count(), columns, describe() 
"""
# Examples

df_id_age = test.select('Age')  # creates dataframe selecting column age 
df_id_age.show(5)      # shows top 5 rows in dataframe 

new_df_age21 = new_df.filter(new_df.Age > 21)  # creates new dataframe having filtered results for Age over 21 only 
new_df_age21.show(5) 

test_df_age_group = test_dfgroupby('Age')  # creates a new df, which has grouped by the column Age
test_df_age_group.count().show(3)          # counts number of obs per each 'Age', then shows the top 3 rows from the new dataframe

test_df_age_group.count().orderBy('Age').show(3)  # Order the dataframe by Age (ascending auto) then shows top 3 rows 

test_df_no_dup = test_df.select('User_ID','Gender','Age').dropDuplicates()   # This will create a new DF that has dropped any duplicate rows
test_df_no_dup.count()  # counts number of non-duplicate rows

test_df_sex = test_df.withColumnRenamed('Gender','Sex')  # renames the column Gender to Sex 

test_df.printSchema()  # this operation prints the types of columns in the DF 

test_df.columns # this prints all the column names into a list 

test_df.describe().show()  # the describe() operation computes summary stats on numerical columns within the DataFrame. Show() shows results. 

# ---------------------------------------------------------------------------------------------------------------

"""
Interacting with DataFrames using PySpark SQL 
"""
# in PySpark you can interact with SparkSQL through DataFrame API and SQL queries 
# all of the operations seen above, could also be done using specific SQL queries, rather than the API 

# we cannot pass SQL queries direct to a dataframe, so we need to create a temporary table to work on
df.createOrReplaceTempView("myTableName")
df2 = spark.sql(
    "select var1, var2 from myTableName"
    )
df2.collect()

# we could also do
test_df.createOrReplaceTempView("testtable")
query = ''' select product_id, product from testtable'''
test_product_df = spark.sql(query)
test_product_df.show(10) 

## Example script
# Filter the people table to select female sex 
people_female_df = spark.sql('SELECT * FROM people WHERE sex=="female"')

# Filter the people table DataFrame to select male sex
people_male_df = spark.sql('SELECT * FROM people WHERE sex=="male"')

# Count the number of rows in both DataFrames
print("There are {} rows in the people_female_df and {} rows in the people_male_df DataFrames".format(people_female_df.count(), people_male_df.count()))

# ---------------------------------------------------------------------------------------------------------------

"""
Data Visualisation in PySpark using DataFrames 

open source plotting tools to aid visualisation in Python
    Matplotlib, Seaborn, Bokeh etc.
    
plotting graphs using PySpark DataFrames is done using three methods
    1) pyspark_dist_explore library 
    2) toPandas() 
    3) HandySpark library 
"""

# Example using pyspark_dist_explore - which contains hist(), distplot() & pandas_histogram() 
test_df = spark.read.csv("test.csv", header=True, inferSchema=True) 
test_df_age = test_df.select('Age')
hist(test_df_age, bins=20, color="red") 


# Example using toPandas() 
test_df = spark.read.csv("test.csv", header=True, inferSchema=True)  # read in original data 
test_df_sample_pandas = test_df_sample.toPandas() # creates a new pandas DF from our original data 
test_df_sample_pandas.hist('Age')  # plots historgram against 'Age variable 

"""
Pandas DataFrame vs PySpark DataFrame 

1) Pandas DFs are in-memory, single-server based structures and operations on PySpark run in parallel 
2) The result is generated as we apply any operation in Pandas, whereas operations in PySpark DF are lazy evaluation 
3) Pandas DF are mutable, PySpark DFs are immutable 
4) Pandas API support more operations than PySpark DF API 
"""

# Example using HandySpark 
test_df = spark.read.csv("test.csv", header=True, inferSchema=True)   # original Data
hdf = test_df.toHandy()   # converts to a HandySpark DataFrame 
hdf.cols['Age'].hist()   # plots historgram of Age variable 


## Course Examples ##

# Example 1
# Check the column names of names_df
print("The column names of names_df are", names_df.columns)
# Convert to Pandas DataFrame  
df_pandas = names_df.toPandas()
# Create a horizontal bar plot
df_pandas.plot(kind='barh', x='Name', y='Age', colormap='winter_r')
plt.show()


# Example 2
# Load the Dataframe
fifa_df = spark.read.csv(file_path, header=True, inferSchema=True)

# Check the schema of columns
fifa_df.printSchema()

# Show the first 10 observations
fifa_df.show(10)

# Print the total number of rows
print("There are {} rows in the fifa_df DataFrame".format(fifa_df.count()))

# Create a temporary view of fifa_df
fifa_df.createOrReplaceTempView('fifa_df_table')

# Construct the "query"
query = '''SELECT Age FROM fifa_df_table WHERE Nationality == "Germany"'''

# Apply the SQL "query"
fifa_df_germany_age = spark.sql(query)

# Generate basic statistics
fifa_df_germany_age.describe().show()

# Convert fifa_df to fifa_df_germany_age_pandas DataFrame
fifa_df_germany_age_pandas = fifa_df_germany_age.toPandas()

# Plot the 'Age' density of Germany Players
fifa_df_germany_age_pandas.plot(kind='density')
plt.show()
