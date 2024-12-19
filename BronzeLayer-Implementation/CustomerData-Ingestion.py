# Databricks notebook source
from pyspark.sql.functions import lit
customer_schema = "customer_id int,first_name string ,last_name string, email string, phone string, country string, city string, registration_date timestamp, date_of_birth timestamp, gender string"

df= spark.read.csv("/mnt/smartpolicydatasystem/landing/Customer", inferSchema=False, schema=customer_schema, header=True)
df_merge_flag = df.withColumn("merge_flag", lit(False))
df_merge_flag.write.option("path", "/mnt/smartpolicydatasystem/bronzelayer/CustomerData").mode("append").saveAsTable("bronzelayer.Customer")



# COMMAND ----------

from datetime import datetime

def getFilePathWithDates(filePath):
    # get the current time in mm-dd-yyyy format
    current_time = datetime.now().strftime('%m-%d-%Y')
    new_file_path = filePath+'/'+current_time
    return new_file_path

# COMMAND ----------

dbutils.fs.cp("/mnt/smartpolicydatasystem/landing/Customer", getFilePathWithDates("/mnt/smartpolicydatasystem/processed/CustomerData"), True)

# COMMAND ----------

