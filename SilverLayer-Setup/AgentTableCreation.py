# Databricks notebook source
# MAGIC %sql
# MAGIC create or replace table Silverlayer.Agent(
# MAGIC agent_id integer,
# MAGIC agent_name string, 
# MAGIC agent_email string,
# MAGIC agent_phone string, 
# MAGIC branch_id integer, 
# MAGIC create_timestamp timestamp,
# MAGIC merged_timestamp TIMESTAMP
# MAGIC ) USING DELTA LOCATION '/mnt/smartpolicydatasystem/silverlayer/Agent'

# COMMAND ----------

