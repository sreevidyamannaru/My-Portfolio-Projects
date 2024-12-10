
from pyspark.sql import SparkSession

def read_data(file_path):
    spark = SparkSession.builder.appName("DataIngestion").getOrCreate()
    df = spark.read.csv(file_path, header=True)
    return df
            