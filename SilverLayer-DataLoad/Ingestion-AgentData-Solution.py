# Databricks notebook source
# MAGIC %md
# MAGIC <b> Load all the new rows from bronze layer Agent table which is yet not merged

# COMMAND ----------

# MAGIC %md
# MAGIC <b> Remove all rows where Barnch Id not exist in Branch table

# COMMAND ----------

# MAGIC %md
# MAGIC <b> Ensure all the phone have valid 10 digit phone no.

# COMMAND ----------

df = spark.sql("SELECT a.* FROM bronzelayer.agent a INNER JOIN bronzelayer.branch b on  a.branch_id = b.branch_id where a.merge_flag = FALSE and length(a.agent_phone)=10")

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC <b>Replace all the empty email with 'admin@azurelib.com'

# COMMAND ----------

df.createOrReplaceTempView("agent_temp")
df_email = spark.sql("select a.agent_id, a.agent_name, a.agent_phone, a.branch_id,a.create_timestamp, regexp_replace(a.agent_email, '', 'admin@azurelib.com') as agent_email from agent_temp a where a.agent_email =''  UNION  select  a.agent_id, a.agent_name, a.agent_phone, a.branch_id,a.create_timestamp, agent_email from agent_temp a where a.agent_email !='' ")

display(df_email)



# COMMAND ----------

# MAGIC %md
# MAGIC <b>Add the merged_date_timestamp (current timesatmp)

# COMMAND ----------

#df_final = df_email.withColumn("merged_timestamp", current_timestamp())
df_email.createOrReplaceTempView("clean_agent")

spark.sql(" MERGE INTO silverlayer.agent AS T USING clean_agent AS S ON  t.agent_id = s.agent_id  WHEN MATCHED THEN UPDATE SET t.agent_phone = s.agent_phone, t.agent_email = s.agent_email, t.agent_name = s.agent_name, t.branch_id= s.branch_id, t.create_Timestamp = s.create_TimeStamp, T.merged_timestamp  =  current_timestamp() When not matched then INSert (agent_phone, agent_email , agent_name, branch_id ,create_Timestamp , merged_timestamp, agent_id) values (s.agent_phone, s.agent_email , s.agent_name, s.branch_id ,s.create_Timestamp , current_timestamp(), s.agent_id)")



# COMMAND ----------

spark.sql("update bronzelayer.agent set merge_flag =True WHERE merge_flag = false")

# COMMAND ----------

