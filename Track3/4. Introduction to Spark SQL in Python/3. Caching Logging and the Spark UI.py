"""
Caching, Logging and the Spark UI
"""
#-----------------------------------------------------------------------------
"""
Caching
"""
# Unpersists df1 and df2 and initializes a timer
prep(df1, df2) 

# Cache df1
df1.cache()

# Run actions on both dataframes
run(df1, "df1_1st") 
run(df1, "df1_2nd")
run(df2, "df2_1st")
run(df2, "df2_2nd", elapsed=True)

# Prove df1 is cached
print(df1.is_cached)

#-----------------------------------------------------------------------------
# Unpersist df1 and df2 and initializes a timer
prep(df1, df2) 

# Persist df2 using memory and disk storage level 
df2.persist(storageLevel=pyspark.StorageLevel.MEMORY_AND_DISK)

# Run actions both dataframes
run(df1, "df1_1st") 
run(df1, "df1_2nd")
run(df2, "df2_1st")
run(df2, "df2_2nd", elapsed=True)

#-----------------------------------------------------------------------------
# List the tables
print("Tables:\n", spark.catalog.listTables())

# Cache table1 and Confirm that it is cached
spark.catalog.cacheTable('table1')
print("table1 is cached: ", spark.catalog.isCached('table1'))

# Uncache table1 and confirm that it is uncached
spark.catalog.uncacheTable('table1')
print("table1 is cached: ", spark.catalog.isCached('table1'))


#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
"""
Logging
"""

# Log columns of text_df as debug message
logging.debug("text_df columns: %s", text_df.columns)

# Log whether table1 is cached as info message
logging.info("table1 is cached: %s", spark.catalog.isCached(tableName="table1"))

# Log first row of text_df as warning message
logging.warning("The first row of text_df:\n %s", text_df.first())

# Log selected columns of text_df as error message
logging.error("Selected columns: %s", text_df.select("id", "word"))


## ------- Uncomment the 5 statements that do NOT trigger text_df ------------
logging.debug("text_df columns: %s", text_df.columns)
logging.info("table1 is cached: %s", spark.catalog.isCached(tableName="table1"))
# logging.warning("The first row of text_df: %s", text_df.first())
logging.error("Selected columns: %s", text_df.select("id", "word"))
logging.info("Tables: %s", spark.sql("SHOW tables").collect())
logging.debug("First row: %s", spark.sql("SELECT * FROM table1 LIMIT 1"))
# logging.debug("Count: %s", spark.sql("SELECT COUNT(*) AS count FROM table1").collect())

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
"""
Query Planning
"""

# We know from regular RDBMS syntax that a query such as:
"""
EXPLAIN SELECT * FROM table1
"""
# The 'explain' keyword will provide details on the query plan, without actually running the query. It returns a query explanation plan, aka the set of steps used to access the data from the query
# Query plan is to be read from bottom up

# Run explain on text_df
text_df.explain()

# Run explain on "SELECT COUNT(*) AS count FROM table1" 
spark.sql("SELECT COUNT(*) AS count FROM table1").explain()

# Run explain on "SELECT COUNT(DISTINCT word) AS words FROM table1"
spark.sql("SELECT COUNT(DISTINCT word) AS words FROM table1").explain()

