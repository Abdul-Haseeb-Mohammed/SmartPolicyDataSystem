# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE table silverlayer.Customer (
# MAGIC customer_id int,first_name string ,last_name string ,email string ,phone string ,country string,city string,registration_date timestamp, date_of_birth timestamp, gender string, merged_timestamp TIMESTAMP
# MAGIC ) USING Delta location '/mnt/smartpolicydatasystem/silverlayer/Customer' 
# MAGIC

# COMMAND ----------

