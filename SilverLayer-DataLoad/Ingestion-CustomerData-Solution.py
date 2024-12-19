# Databricks notebook source
# MAGIC %md
# MAGIC <b>Remove all where Customer Id not null
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <b> 
# MAGIC Remove records where gender is other than Male/Female
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <b>Outlier check at some registration_date > DOb.
# MAGIC

# COMMAND ----------

df = spark.sql("select * from bronzelayer.customer where merge_flag  = false and customer_id  is not null and gender in ('Male', 'Female' ) and registration_date > date_of_birth ")
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC <b>Merge the data into silver layer while adding current_timestamp
# MAGIC

# COMMAND ----------

df.createOrReplaceTempView("clean_customer")
spark.sql(" MERGE INTO silverlayer.customer AS T USING clean_customer AS S ON t.customer_id = s.customer_id WHEN MATCHED then UPDATE SET t.first_name = s.first_name, t.email = s.email , t.phone = s.phone , t.last_name = s.last_name , t.country = s.country , t.city = s.city,  t.registration_date = s.registration_date,  t. date_of_birth  = s.date_of_birth, t.gender =s.gender, t.merged_timestamp = current_timestamp()  when not MATCHED then insert (customer_id ,first_name  ,last_name  ,email  ,phone  ,country ,city ,registration_date , date_of_birth , gender , merged_timestamp ) values (s.customer_id ,s.first_name  ,s.last_name  ,s.email  ,s.phone  ,s.country ,s.city ,s.registration_date , s.date_of_birth , s.gender ,current_timestamp() ) ")


# COMMAND ----------

# MAGIC %md
# MAGIC <b>Update the flag in the bronze layer

# COMMAND ----------

# MAGIC %sql
# MAGIC UPDATE bronzelayer.customer set merge_flag = true where merge_flag = false

# COMMAND ----------

