from pyspark.sql import SparkSession
from pyspark.sql.functions import col,sum,round
#from pyspark.sql.types import FloatType



spark = SparkSession.builder.appName("App").getOrCreate()

#load Data
df = spark.read.csv("file:///home/cdpadmin/data/orders.csv",header=True,inferSchema=True)


#clean Data

df_clean = df.dropna(subset=['order_id','product_id','customer_id','amount'],how="any")\
             .withColumn('amount',col('amount').cast("float"))
#df_clean.show()
#df_clean.printSchema()

#total revenue per product

df_revenue = df_clean.groupBy("product_id")\
                     .agg(round(sum('amount'),2).alias("revenue"))\
                     #.withColumn("revenue",round("revenue",2))
                     
df_revenue.show()
#df_revenue.printSchema()

