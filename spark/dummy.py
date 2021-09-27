from pyspark.sql import SparkSession

spark = SparkSession.builder\
    .appName('jee_force')\
    .config('spark.driver.memory', '2g')\
    .getOrCreate()
sc = spark.sparkContext

rdd = sc.parallelize((i for i in range(1_000_000))).repartition(5)

n = rdd.reduce(lambda a, b: a + b)

print('')
print('-' * 15)
print(f'reduce: {n}')
print('-' * 15)
print('')

spark.stop()