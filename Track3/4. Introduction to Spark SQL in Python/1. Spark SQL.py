"""
Spark SQL 
"""
## Example script(s) & assumed Spark setup 

# Start by creating a dataframe from your CSV file 
df = spark.read.csv("filepath", header=True) 

# remember, can't sql query direct to spark dataframe, so create temp tab;e/view over it to query against
df.createOrReplaceTempView("callItWhatYouLike")

# now you can run your query
spark.sql("select * from callItWhatYouLike where variable = 'condition'").show()   # the .show() will reveal first 20 rows of result by default 

# inspecting table schema 
result = spark.sql("show columns from tablenbame")

# show the columns by
result.show() 
# or 
print(result.columns) 

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

"""
Window Function SQL

This can be used to do things like lag/lead functions in SAS. We could create a new variable, that on each row, shows the NEXT row's time, for the same ID etc. This would then allow us 
to perform calculations, such as difference between the two times etc. etc. 
This is the same as the window function for Hive QL. Using the OVER clause and the ORDER BY clause.
"""
query = """
select 
    train_id, station, time, 
    lead(time, 1) over (order by time) as time_next 
from schedule_data
where train_id=123 """
spark.sql(query).show() 

# imagine doing for multiple trains (so remove the where clause focusing on train_id) We would need to use the PARTITION BY in the query.
query = """
select 
    train_id, station,
    time,
    lead(time,1) over (partition by train_id order by time) as time_next 
from schedule_data """
spark.sql(query).show() 


#-------- Example - Building a running total ----------------------------------
# Add col running_total that sums diff_min col in each group
query = """
SELECT train_id, station, time, diff_min,
SUM(diff_min) OVER (PARTITION BY train_id ORDER BY time) AS running_total
FROM schedule
"""

# Run the query and display the result
spark.sql(query).show()

#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

"""
Dot notation & SQL 
"""

# imagine a dataset with 3 columns, of which we want to choose 2 >>> train_id and station
# for dot notation instead of SQL query notation
# we can do:
df.select('train_id', 'station')
# or 
df.select(df.train_id, df.station)
# or
from pyspark.sql.functions import col 
df.select(col('train_id'), col('station')) 

# similarly, if we wanted to rename a column, we could do:
df.select('train_id','station').withColumnRenamed('train_id','train').show(5) 

# We can also do window functions through dot notation 
from pyspark.sql import Window,
from pyspark.sql.functions import row_number
df.withColumn("id", row_number()
              .over(
                  Window.partitionBy('train_id').orderBy('time')
                  )
)
# The above step creates an ID column, placing an ID for each stop, per train. So that stop 1 will be 1, then 2 etc etc, with each train following that sequence.

## Function Notes ##
# ROW_NUMBER in SQL :  pyspark.sql.functions.row_number 
# The inside of the OVER clause:  pyspark.sql.Window 
# PARTITION BY :  pyspark.sql.Window.partitionBy
# ORDER BY :   pyspark.sql.Window.orderBY 

# Typically, using a WindowSpec - specify the window first, then run it within the Over() function [which corresponds to SQLs over clause] 
window = Window.partitionBy('train_id').orderBy('time')
dfx = df.withColumn('next', lead('time',1).over(window)) 


## ------ Examples of SQL notation & dot notation for the same query -------------
spark.sql('SELECT train_id, MIN(time) AS start FROM schedule GROUP BY train_id').show()
df.groupBy('train_id').agg({'time':'min'}).withColumnRenamed('min(time)', 'start').show()

# Print the second column of the result
spark.sql('SELECT train_id, MIN(time), MAX(time) FROM schedule GROUP BY train_id').show()
result = df.groupBy('train_id').agg({'time':'min', 'time':'max'})
result.show()
print(result.columns[1])


## ------ Examples of SQL notation & dot notation for the same query -------------
# 
# Mtach an SQL notation window function with the dot notation equivalent 
df = spark.sql("""
SELECT *, 
LEAD(time,1) OVER(PARTITION BY train_id ORDER BY time) AS time_next 
FROM schedule
""")

# Obtain the identical result using dot notation 
dot_df = df.withColumn('time_next', lead('time', 1)
        .over(Window.partitionBy('train_id')
        .orderBy('time')))

# Example query using Unix Timestamp 
query = """
SELECT *, 
(UNIX_TIMESTAMP(LEAD(time, 1) OVER (PARTITION BY train_id ORDER BY time),'H:m') 
 - UNIX_TIMESTAMP(time, 'H:m'))/60 AS diff_min 
FROM schedule 
"""
sql_df = spark.sql(query)
sql_df.show()

