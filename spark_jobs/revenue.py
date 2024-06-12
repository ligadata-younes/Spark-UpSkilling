from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize a SparkSession
spark = SparkSession.builder \
    .appName("Spark SQL Use Case") \
    .getOrCreate()

# Load the data (adjust the file path if necessary)
df = spark.read.option("header", "true").csv("/opt/bitnami/spark/data/online_retail.csv", inferSchema=True)

# Create a temporary view for the DataFrame
df.createOrReplaceTempView("sales")

# Perform the repartitioning using SQL
spark.sql("CACHE TABLE sales")  # Cache the table to ensure the repartitioning takes place

# Execute the SQL query to calculate total revenue per country
query = """
SELECT Country, SUM(Revenue) AS TotalRevenue
FROM (
    SELECT Country, Quantity * UnitPrice AS Revenue
    FROM sales
) 
GROUP BY Country
"""

# Show the execution plan for the SQL query
df_revenue_per_country = spark.sql(query)
df_revenue_per_country.explain()

# Show the result
df_revenue_per_country.show()

# Write the result to a CSV file on your local machine
output_path = "/opt/bitnami/spark/data/revenue_per_country.csv"
df_revenue_per_country.coalesce(1).write.option("header", "true").csv(output_path)

# Stop the SparkSession
spark.stop()



# /opt/bitnami/spark/jobs/revenue.py job path
# /opt/bitnami/spark/data sink path

# spark-submit /opt/bitnami/spark/jobs/revenue.py command to run the job