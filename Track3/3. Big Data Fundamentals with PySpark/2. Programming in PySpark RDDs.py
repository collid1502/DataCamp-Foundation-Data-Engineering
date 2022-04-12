"""
Programming in PySpark RDDs   (Resilient Distributed Datasets)
"""
# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------

"""
if we wish to create RDDs from python lists, we can use parallelize() 
"""
# Example (assume Spark Context 'sc' loaded)
numRDD = sc.parallelize([1,2,3,4]) 
type(numRDD) 

# or 
helloRDD = sc.parallelize("Hello world")
type(helloRDD) 

#-----------------------------------------------------------------------------------------------------------------
"""
if we wish to create an RDD from an external dataset (such as a text file)
"""
fileRDD = sc.textFile(<"file_path">)
type(fileRDD) 

#-----------------------------------------------------------------------------------------------------------------
"""
Partitioning in Spark

A partition is a logical division of a large distributed data set 
"""
# parallelize() method:
numRDD = sc.parallelize(range(10), minPartitions = 6)

# textFile() method:
fileRDD = sc.textFile("<file_path">, minPartitions = 6)

# we can also use the getNumPartitions() method to find the number of existing partitions in an RDD 

#-----------------------------------------------------------------------------------------------------------------
"""
Basic RDD Transformations & Actions 
"""
# map() Transformation 
# the map() transformation applies a function to all elements in the RDD 
# example:
RDD = sc.parallelize([1,2,3,4]) 
RDD_map = RDD.map(lambda x: x * x)   # function to return square value of each value passed from list >> so [1,4,9,16] 


# filter() Transformation 
# the filter() transformation will return only elements that pass the condition 
# example:
RDD = sc.parallelize([1,2,3,4]) 
RDD_filter = RDD.filter(lambda x: x > 2)    # will return a new list of just [3,4] 


# flatMap() Transformation 
# the flatMap() transformation returns multiple values for each element of the original RDD 
# example:
RDD = sc.parallelize(["hello world", "how are you"]) 
RDD_flatmap = RDD.flatMap(lambda x: x.split(" "))    # run a split on each element by space. So, for each word/text around a space, will be broken into a list such as: ["hello","world","how","are","you"] etc. 


# union() Transformation 
# the union() transformation can combine two RDDs to form a new RDD 
# example:  Imagine we have a textfile, which is logs of jobs. Create a first RDD from this file, that captures errors. Then a second, that captures warnings. Then combine the two.
inputRDD = sc.textFile(<"my_text_file">)
errorRDD = inputRDD.filter(lambda x: "error" in x.split()) 
warningsRDD = inputRDD.filter(lambda x: "warnings" in x.split()) 
combinedRDD = errorRDD.union(warningsRDD) 

#
# Basic Actions 
# --------------
# collect() & take() Actions
#
# collect() returns all the elements of the dataset as an array 
# take(N) returns an array with the first N elements of the dataset 
# examples:
RDD_map.collect()
# or 
RDD_map.take(3) 

# first() prints the first element in an RDD
# and 
# count() returns the total number of elements from the RDD 

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------

"""
Creating Pair RDDs
"""
# Two common ways to create pair RDDs:
# 1) From a list of key-value tuples
# 2) From a regular RDD 

# Get Data into key/value form for paired RDD 
my_tuple = [('Sam',23), ('Mary',34), ('Peter',25)] 
pairRDD_tuple = sc.parallelize(my_tuple) 

# or 
my_list = ['Sam 23', 'Mary 34', 'Peter 25']
regularRDD = sc.parallelize(my_list) 
pairRDD_RDD = regularRDD.map(lambda s: (s.split(' ')[0], s.split(' ')[1])) 


"""
Transformations on pair RDDs

1) all regular transformations work on pair RDDs
2) have to pass functions that operate on key value pairs rather than on individual elements

examples of paired RDD transformations:
    reduceByKey(func)  ~   Combine values with the same key 
    groupByKey()       ~   Group values with the same key 
    sortByKey()        ~   Return an RDD sorted by the key 
    join()             ~   Join two pair RDDs based on their key 
"""

# Example reduceByKey() transformation  
#
# it runs parallel operations for each key in the dataset 
# it is a transformation and not action 
regularRDD = sc.parallelize([("Messi",23), ("Ronaldo",34), ("Neymar", 22), ("Messi", 24)])
pairRDD_reducebykey = regularRDD.reduceByKey(lambda x,y : x + y) 
pairRDD_reducebykey.collect() 

# results would show - player & total goals scored as value:
# [("Neymar", 22), ("Ronaldo", 34), ("Messi", 47)] 

#------------------------------------------------------------------------------

# Example of sortByKey() transformation 
#
# sortByKey() operation orders pair RDD by key 
# returns an RDD sorted by key in ascending or descending order 
pairRDD_reducebykey_rev = pairRDD_reducebykey.map(lambda x: (x[1], x[0])) 
pairRDD_reducebykey_rev.sortByKey(ascending=False).collect() 

# Resulting output:
# [("Messi", 47), ("Ronaldo", 34), ("Neymar", 22)]

#------------------------------------------------------------------------------

# Example of groupByKey() transformation 
#
# groupByKey() groups all the values with the same key in the pair RDD 
airports = [("US","JFK"), ("UK","LHR"), ("FR","CDG"), ("US","SFO")]
regularRDD = sc.parallelize(airports)
pairRDD_group = regularRDD.groupByKey().collect()
for cont, air in pairRDD_group:
    print(cont, list(air)) 

 
# resulting output:
# 
# FR ['CDG']
# US ['JFK','SFO']
# UK ['LHR'] 

#------------------------------------------------------------------------------

# Example of join() transformation 
#
# imagine 2 RDDs where the player name is the key, and in one RDD is the number of goals, the second is income (in millions)
RDD1 = sc.parallelize([("Messi",34), ("Ronaldo",32), ("Neymar", 24)])
RDD2 = sc.parallelize([("Ronaldo",80), ("Neymar",120), ("Messi", 100)])

RDD1.join(RDD2).collect() 

# resulting output:
# [("Neymar", (24, 120)), ("Ronaldo", (32, 80)), ("Messi", (34, 100))] 

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
"""
More advanced transformations/actions for RDDs
"""

# Example of reduce() action 
#
# reduce(func) action is used for aggregating the elements of a regular RDD 
# the function should be commutative (changeing the order of the operands does not change the result) and associative 
x = [1,3,4,6]
RDD = sc.parallelize(x)
RDD.reduce(lambda x, y : x + y)


# Example of saveAsTextFile() action 
# 
# In many cases, it is not advisableto run collect action on RDDs because of the huge size of the data. In these cases, it's common to write data out to a 
# distributed storage system, such as HDFS or Amazon S3. saveAsTextFile action can be used to save a RDD as a text file inside a particular directory. 
# By default, the action saves RDD with each partition as a separate file inside a directory. 

RDD.saveAsTextFile("tempFile") 
# the coalesce() method can be used to save RDD as a single text file 
RDD.coalesce(1).saveAsTextFile("tempFile") 


# Example of countByKey() action  -  note, this action should only be used on a dataset small enough in size to fit in memory
#
# countByKey() only available for type (key, value) 
# countByKey() action counts the number of elements for each key 
# example:
rdd = sc.parallelize([("a",1), ("b",1), ("a",1)])
for kee, val in rdd.countByKey().items():
    print(kee, val) 

# resulting output:
# ('a', 2)
# ('b', 1)


# Example of collectAsMap() action 
#
# collectAsMap() return the key-value pairs in the RDD as a dictionary 
# Example of collectAsMap() on a simple tuple
sc.parallelize([(1,2), (3,4)]).collectAsMap() 

# resulting output 
# {1: 2, 3: 4} 
