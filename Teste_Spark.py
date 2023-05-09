import findspark
findspark.init()

import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()

spark = (
    SparkSession.builder
        .master("local")
        .appName("Word Count")
        .config("spark.some.config.option", "some-value")
        .getOrCreate()
)
