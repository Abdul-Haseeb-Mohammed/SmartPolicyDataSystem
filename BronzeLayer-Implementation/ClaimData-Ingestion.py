# Databricks notebook source
from pyspark.sql.functions import lit

claim_schema= "claim_id int, policy_id int, date_of_claim timestamp, claim_amount double, claim_status string, LastUpdatedTimeStamp timestamp"

df= spark.read.parquet("/mnt/smartpolicydatasystem/landing/ClaimData/*.parquet", inferSchema =False, schema= claim_schema)
df_merge_flag = df.withColumn("merge_flag", lit(False))

df_merge_flag.write.option("path", "/mnt/smartpolicydatasystem/bronzelayer/ClaimData").mode("append").saveAsTable("bronzelayer.Claim")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM bronzelayer.claim

# COMMAND ----------

from datetime import datetime

def getFilePathWithDates(filePath):
    # get the current time in mm-dd-yyyy format
    current_time = datetime.now().strftime('%m-%d-%Y')
    new_file_path = filePath+'/'+current_time
    return new_file_path

# COMMAND ----------

dbutils.fs.mv("/mnt/smartpolicydatasystem/landing/ClaimData", getFilePathWithDates("/mnt/smartpolicydatasystem/processed/ClaimData"), True )

# COMMAND ----------

