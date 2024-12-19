# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE table silverlayer.Branch(
# MAGIC
# MAGIC   branch_id INT,
# MAGIC   branch_country string,
# MAGIC   branch_city string,
# MAGIC   merged_timestamp TIMESTAMP
# MAGIC ) USING DELTA LOCATION '/mnt/smartpolicydatasystem/silverlayer/Branch'

# COMMAND ----------

