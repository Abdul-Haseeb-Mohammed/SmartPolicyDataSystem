# Databricks notebook source
from pyspark.sql.functions import lit

schema = "agent_id integer, agent_name string, agent_email string,agent_phone string, branch_id integer, create_timestamp timestamp"
df = spark.read.parquet("/mnt/smartpolicydatasystem/landing/AgentData/*.parquet")
df_with_flag = df.withColumn("merge_flag", lit(False))
df_with_flag.write.option("path", "/mnt/smartpolicydatasystem/bronze/AgentData").mode("append").saveAsTable("bronzelayer.Agent")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from bronzelayer.agent

# COMMAND ----------

from datetime import datetime

def getFilePathWithDates(filePath):
    # get the current time in mm-dd-yyyy format
    current_time = datetime.now().strftime('%m-%d-%Y')
    new_file_path = filePath+'/'+current_time
    return new_file_path

# COMMAND ----------

dbutils.fs.mv("/mnt/smartpolicydatasystem/landing/AgentData/", getFilePathWithDates("/mnt/smartpolicydatasystem/processed/AgentData/"), True)

# COMMAND ----------

