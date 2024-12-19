# Databricks notebook source
from pyspark.sql.functions import lit

policy_schema= "policy_id int, policy_type string, customer_id int, start_date timestamp, end_date timestamp, premium double,  coverage_amount double"

df = spark.read.json("/mnt/smartpolicydatasystem/landing/PolicyData/", schema=policy_schema)
df_merg_flag = df.withColumn("merge_flag", lit(False))
df_merg_flag.write.option("path", "/mnt/smartpolicydatasystem/bronzelayer/PolicyData").mode("append").saveAsTable("bronzelayer.Policy")


# COMMAND ----------

from datetime import datetime

def getFilePathWithDates(filePath):
    # get the current time in mm-dd-yyyy format
    current_time = datetime.now().strftime('%m-%d-%Y')
    new_file_path = filePath+'/'+current_time
    return new_file_path

# COMMAND ----------

dbutils.fs.cp("/mnt/smartpolicydatasystem/landing/PolicyData", getFilePathWithDates("/mnt/smartpolicydatasystem/processed/PolicyData"), True)

# COMMAND ----------

