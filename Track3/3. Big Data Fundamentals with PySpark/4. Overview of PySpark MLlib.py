"""
Overview of PySpark MLlib (Machine Learning Library)
"""
# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------

"""
Details:

PySpark MLlib is the Apache Spark scalable machine learning library in Python
consisting of common learning algorithms and utilities. 

Scikit-learn is a popular Python lib for data mining and machine learning, however, 
Scikit-learn algorithms only work for small datasets on a single machine. 

Spark's MLlib algorithms are designed for parallel processing on a cluster.
Spark also provides a high-level API to build macgine learning pipelines (a workflow of mutliple algorithms together) 
"""

# Example of PySpark MLlib imports 
from pyspark.mllib.recommendation import ALS 
from pyspark.mllib.classification import LogisticRegressionWithLBFGS
from pyspark.mllib.clustering import KMeans 

# ----------------------------------------------------------------------------
# Example ML script for a recommendation engine (collaborative filtering) - This example is around ratings for Movies

# Load the data into RDD
data = sc.textFile(file_path)

# Split the RDD 
ratings = data.map(lambda l: l.split(','))

# Transform the ratings RDD
ratings_final = ratings.map(lambda line: Rating(int(line[0]), int(line[1]), float(line[2])))   # note, each line of the RDD has userID[0], productID[1] & rating[2]. So we replace each line by mapping a created Tuple of the 3 items of info from the row

# Split the data into training and test
training_data, test_data = ratings_final.randomSplit([0.8, 0.2])    # this randomly splits the data, 80% into training, 20% into test 

# Create the ALS model on the training data
model = ALS.train(training_data, rank=10, iterations=10)    # specify training data to be used by model. rank ~ number of latent factors in the model.  iterations ~ number of iterations to run.

# Drop the ratings column 
testdata_no_rating = test_data.map(lambda p: (p[0], p[1])  # take our test data. Drop ratings column as we want to predict this with our built model 

# Predict the model  
predictions = model.predictAll(testdata_no_rating)      # run a prediction for the rating, for each row of our test data, using the model built 

# Print the first rows of the RDD
predictions.take(2)    # show the first few rows of the model predictions of the test data set


# Prepare ratings data
rates = ratings_final.map(lambda r: ((r[0], r[1]), r[2]))   # organises original ratings data and maps each row into ((user, product) rating). (user, product) acts as a key. Rating is the value.

# Prepare predictions data
preds = predictions.map(lambda r: ((r[0], r[1]), r[2]))     # does the saem for the predictions data - into format above 

# Join the ratings data with predictions data
rates_and_preds = rates.join(preds)               # joins the two together. The key is (user, product) for which the join will be performed on.

# Calculate and print MSE
MSE = rates_and_preds.map(lambda r: (r[1][0] - r[1][1])**2).mean()   # using the newly joined DF, calculate the difference between each predicted rating, and actual observed rating (squared to account for negative differences). Take the mean of this!
print("Mean Squared Error of the model for the test data = {:.2f}".format(MSE))  # print the MSE reults from model build 

# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# Example ML script for Classification with Logistic Regression for Binary Outcomes  ~ in this case, is an email spam or not

# Load the datasets into RDDs
spam_rdd = sc.textFile(file_path_spam)
non_spam_rdd = sc.textFile(file_path_non_spam)

# Split the email messages into words
spam_words = spam_rdd.flatMap(lambda email: email.split(' '))
non_spam_words = non_spam_rdd.flatMap(lambda email: email.split(' '))

# Print the first element in the split RDD
print("The first element in spam_words is", spam_words.first())
print("The first element in non_spam_words is", non_spam_words.first())

# Create a HashingTf instance with 200 features
tf = HashingTF(numFeatures=200)

# Map each word to one feature
spam_features = tf.transform(spam_words)
non_spam_features = tf.transform(non_spam_words)

# Label the features: 1 for spam, 0 for non-spam
spam_samples = spam_features.map(lambda features:LabeledPoint(1, features))
non_spam_samples = non_spam_features.map(lambda features:LabeledPoint(0, features))

# Combine the two datasets
samples = spam_samples.union(non_spam_samples)


# Split the data into training and testing
train_samples,test_samples = samples.randomSplit([0.8, 0.2])

# Train the model
model = LogisticRegressionWithLBFGS.train(train_samples)

# Create a prediction label from the test data
predictions = model.predict(test_samples.map(lambda x: x.features))

# Combine original labels with the predicted labels
labels_and_preds = test_samples.map(lambda x: x.label).zip(predictions)

# Check the accuracy of the model on the test data
accuracy = labels_and_preds.filter(lambda x: x[0] == x[1]).count() / float(test_samples.count())
print("Model accuracy : {:.2f}".format(accuracy))


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# Example ML script for K-means Clustering (unsupervised learning method) to organise a collection fo data into groups 

# Load the dataset into a RDD
clusterRDD = sc.textFile(file_path)

# Split the RDD based on tab
rdd_split = clusterRDD.map(lambda x: x.split("\t"))

# Transform the split RDD by creating a list of integers
rdd_split_int = rdd_split.map(lambda x: [int(x[0]), int(x[1])])

# Count the number of rows in RDD 
print("There are {} rows in the rdd_split_int dataset".format(rdd_split_int.count()))

# Train the model with clusters from 13 to 16 and compute WSSSE 
for clst in range(13, 17):
    model = KMeans.train(rdd_split_int, clst, seed=1)
    WSSSE = rdd_split_int.map(lambda point: error(point)).reduce(lambda x, y: x + y)
    print("The cluster {} has Within Set Sum of Squared Error {}".format(clst, WSSSE))

# Train the model again with the best k 
model = KMeans.train(rdd_split_int, k=15, seed=1)

# Get cluster centers
cluster_centers = model.clusterCenters

# Convert rdd_split_int RDD into Spark DataFrame
rdd_split_int_df = spark.createDataFrame(rdd_split_int, schema=["col1", "col2"])

# Convert Spark DataFrame into Pandas DataFrame
rdd_split_int_df_pandas = rdd_split_int_df.toPandas()

# Convert "cluster_centers" that you generated earlier into Pandas DataFrame
cluster_centers_pandas = pd.DataFrame(cluster_centers, columns=["col1", "col2"])

# Create an overlaid scatter plot
plt.scatter(rdd_split_int_df_pandas["col1"], rdd_split_int_df_pandas["col2"])
plt.scatter(cluster_centers_pandas["col1"], cluster_centers_pandas["col2"], color="red", marker="x")
plt.show()
