"""
Using window function sql for natural language processing
"""

# The goal of NLP is to load text data into a dataframe, and get rid of unwanted elements of the data, to
# focus analysis on the key text 

## --- Example - The Project Gutenberg eBook of The Adventure of Sherlock Holmes (by Sir Arthur Conan Doyle) 

# Step 1
# to load the text 
df = spark.read.text('sherlock.txt') 
print(df.first()) # prints the first row of the text file (which should contain the header) 
print(df.count()) # prints the number of rows in the text file 

# or, we could load a parquet type (Hadoop file type for data structure) rather than a text file 
df1 = spark.read.load('sherlock.parquet')


# Step 2
# Having loaded the text into a dataframe, show some of it
df1.show(15, truncate=False)   # this shows the first 15 rows of the loaded dataframe. Truncate False will print rows of any length and avoid them being truncated.

# Step 3
# convert all characters to lowercase 
df = df1.select(lower(col('value')))   # value is the name ov the variable that holds each line of text
df.columns # this will print ['lower(value)'] 

# Step 4
# We can also aliad the column 'value' to 'v' for shorthand
df = df1.select(lower(col('value')).alias('v')) 
df.columns # this will now print ['v'] 


# Step5 
# Replacing Text 
df = df1.select(regexp_replace('value', 'Mr\.', 'Mr').alias('v'))  # This step take the value column, replaces any instance of 'Mr.' with 'Mr' (using the \ as an escape key to read the . correctly). It then asigns the 'value' column as 'v' in new dataframe
#
# Example output    "Mr. Holmes."  ==>  "Mr Holmes."

# Another example, is to turn "don't know" into "do not know" 
df = df1.select(regexp_replace('value', 'don\'t', 'do not').alias('v'))


# Step 6 - Tokenize text
# Here we want to split each word on a line, into a list, so that each word becomes a 'token' 
df = df2.select(split('v', '[ ]').alias('words'))   # creates a variable, aliased as 'words', which is a list [a,b,c] of all words on a row
df.show(truncate=False)   # shows the first 15 rows by default, truncation off to uncap row length 

# Step 7 - discard split characters 
# This is important, as we want to get rid of all the different punctuation or split chars that can exist and 'dirty' our word lists 
punctuation = "_|.\?\!\",\'\[\]\*()" 
df3 = df2.select(split('v', '[ %s]' % punctuation). alias('words')) 
df3.sjow(truncate=False) 


# Step 8 - Exploding an Array 
# This is so that we take each list of words (on a row) and transpose them into one, giant, ordered list 
df4 = df3.select(explode('words').alias('word'))
df4.show()  

# Step 9 - remove blank / empty rows 
nonblank_df = df.where(length('word') > 0)

# Step 10 - add a row id column 
df2 = df.select('word', monotonically_increasing_id().alias('id')) 
df2.show() 

# Step 11 - partitioning the data 
df2 = df.withColumn('part', when(df.id < 25000, 0)
                             .when(df.id < 50000, 1)
                             .when(df.id < 75000, 2)
                             .otherwise(3))

# Re-partition on new column 
df2 = df.repartition(4, 'part')  # specifies number of partitions (first arg) and variable to partition by (second arg) 
print(df2.rdd.getNumPartitions()) # prints result 4

#
# Imagine text already paritioned, into multiple files in one folder directory >>> sherlock_part0.txt, sherlock_part1.txt etc etc
$ ls sherlock_parts # shell script to access folder directory & list items inside 

df_parts = spark.read.text('sherlock_parts')  # This will build a dataframe reading all the partitoned files together, having passed the folder directory as the argument 

# ----------------------------------------------------------------------------
## ---   Example code exercises 

# Load the dataframe
df = spark.read.load('sherlock_sentences.parquet')

# Filter and show the first 5 rows
df.where('id > 70').show(5, truncate=False)
#------------------------------------------------------------

# Split the clause column into a column called words 
split_df = clauses_df.select(split('clause', ' ').alias('words'))
split_df.show(5, truncate=False)

# Explode the words column into a column called word 
exploded_df = split_df.select(explode('words').alias('word'))
exploded_df.show(10)

# Count the resulting number of rows in exploded_df
print("\nNumber of rows: ", exploded_df.count())

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
"""
Moving Window Function Analysis 
"""

# create a dataframe which has the prior 2 words, the current word, and the subsequent 2 words, into one line, under each variable W1, W2, W3, W4, W5 etc
query = """
SELECT
part,
LAG(word, 2) OVER(PARTITION BY part ORDER BY id) AS w1,
LAG(word, 1) OVER(PARTITION BY part ORDER BY id) AS w2,
word AS w3,
LEAD(word, 1) OVER(PARTITION BY part ORDER BY id) AS w4,
LEAD(word, 2) OVER(PARTITION BY part ORDER BY id) AS w5
FROM text
"""
spark.sql(query).where("part = 12").show(10)


##----- Repartition data example:
# Repartition text_df into 12 partitions on 'chapter' column
repart_df = text_df.repartition(12, 'chapter')

# Prove that repart_df has 12 partitions
repart_df.rdd.getNumPartitions()  # prints the 12

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
"""
Common word sequences
"""

# Find the top 10 sequences of five words
query = """
SELECT w1, w2, w3, w4, w5, COUNT(*) AS count FROM (
   SELECT word AS w1,
   LEAD(word,1) OVER(PARTITION BY part ORDER BY id ) AS w2,
   LEAD(word,2) OVER(PARTITION BY part ORDER BY id ) AS w3,
   LEAD(word,3) OVER(PARTITION BY part ORDER BY id ) AS w4,
   LEAD(word,4) OVER(PARTITION BY part ORDER BY id ) AS w5
   FROM text
)
GROUP BY w1, w2, w3, w4, w5
ORDER BY count DESC
LIMIT 10
""" 
df = spark.sql(query)
df.show()


# Unique 5-tuples sorted in descending order
query = """
SELECT DISTINCT w1, w2, w3, w4, w5 FROM (
   SELECT word AS w1,
   LEAD(word,1) OVER(PARTITION BY part ORDER BY id ) AS w2,
   LEAD(word,2) OVER(PARTITION BY part ORDER BY id ) AS w3,
   LEAD(word,3) OVER(PARTITION BY part ORDER BY id ) AS w4,
   LEAD(word,4) OVER(PARTITION BY part ORDER BY id ) AS w5
   FROM text
)
ORDER BY w1 DESC, w2 DESC, w3 DESC, w4 DESC, w5 DESC 
LIMIT 10
"""
df = spark.sql(query)
df.show()


# Example utilising sub-query
#   Most frequent 3-tuple per chapter
query = """
SELECT chapter, w1, w2, w3, count FROM
(
  SELECT
  chapter,
  ROW_NUMBER() OVER (PARTITION BY chapter ORDER BY count DESC) AS row,
  w1, w2, w3, count
  FROM ( %s )
)
WHERE row = 1
ORDER BY chapter ASC
""" % subquery

spark.sql(query).show()
