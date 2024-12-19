# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TABLE Silverlayer.Claim (
# MAGIC
# MAGIC claim_id integer,
# MAGIC policy_id integer,
# MAGIC date_of_claim DATE,
# MAGIC claim_amount decimal(18,0),
# MAGIC claim_status string,
# MAGIC LastUpdatedTimeStamp timestamp,
# MAGIC merged_timestamp timestamp
# MAGIC
# MAGIC ) USING DELTA LOCATION '/mnt/smartpolicydatasystem/silverlayer/Claim'

# COMMAND ----------

