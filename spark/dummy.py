from pyspark.sql import SparkSession

spark = SparkSession.builder\
    .master('spark://localhost:7077')\
    .appName('jee_force')\
    .config('spark.driver.bindAddress', 'localhost')\
    .config('spark.driver.memory', '2g')\
    .config('spark.sql.autoBroadcastJoinThreshold', '-1')\
    .getOrCreate()
spark.stop()