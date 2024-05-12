from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator

# Begin Spark session
spark_session = SparkSession.builder \
    .appName("Music_Recommendation_Spotify") \
    .config("spark.mongodb.input.uri", "mongodb://192.168.93.129:27017/db.collection") \
    .getOrCreate()

# Import data from MongoDB into Spark DataFrame
music_df = spark_session.read.format("mongo").load()

# Transform categorical data to numerical values
genre_indexer = StringIndexer(inputCol="genre_Title", outputCol="genreIndex")
indexed_music_df = genre_indexer.fit(music_df).transform(music_df)

# Divide data into training and testing datasets
(training_set, testing_set) = indexed_music_df.randomSplit([0.8, 0.2])

# Initialize ALS model
als_model = ALS(maxIter=5, regParam=0.01, userCol="user_id", itemCol="track_id", ratingCol="rating",
                coldStartStrategy="drop")

# Train ALS model
music_recommendation_model = als_model.fit(training_set)

# Make predictions
recommendations = music_recommendation_model.transform(testing_set)

# Evaluate model performance using RMSE
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
root_mean_squared_error = evaluator.evaluate(recommendations)
print("Root Mean Squared Error (RMSE) = " + str(root_mean_squared_error))
