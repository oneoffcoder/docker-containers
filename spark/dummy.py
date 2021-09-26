from pyspark.sql import SparkSession

spark = SparkSession.builder\
    .master('spark://localhost:7077')\
    .appName('jee_force')\
    .config('spark.driver.memory', '2g')\
    .getOrCreate()
sc = spark.sparkContext

rdd = sc.parallelize((i for i in range(1_000)))

n = rdd.reduce(lambda a, b: a + b)
print(f'reduce: {n}')

spark.stop()