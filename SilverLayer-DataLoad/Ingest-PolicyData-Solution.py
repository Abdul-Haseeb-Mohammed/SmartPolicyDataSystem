# Databricks notebook source
# MAGIC %md
# MAGIC <b>Remove all the rows where Customer Id,Policy ID is null
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <b>
# MAGIC Remove all rows where Customer Id not exist in Customer table
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <b>
# MAGIC Every policy must have preminum & covergae amount >0
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <b>
# MAGIC Validate end_date>start_date
# MAGIC

# COMMAND ----------

df = spark.sql(" SELECT p.* FROM bronzelayer.policy p INNER JOIN  bronzelayer.customer c  ON p.customer_id = c.customer_id  where p.customer_id is not null and p.policy_id is not null and p.merge_flag = FALSE and p.premium >0 and  p.coverage_amount >0 AND p.end_date > p.start_date ")
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC <b>
# MAGIC Merged the table with merged_date_timestamp as current timesatmp

# COMMAND ----------

df.createOrReplaceTempView('clean_policy')
spark.sql("Merge into  silverlayer.policy AS T USING clean_policy AS S ON t.policy_id = s.policy_id WHEN MATCHED THEN UPDATE SET T.policy_type = s.policy_type , T.premium = s.premium, T.end_date = s.end_date, T.start_date = s.start_date, T.coverage_amount =s.coverage_amount, T.customer_id = s.customer_id, T.merged_timestamp = current_timestamp()  WHEN NOT MATCHED THEN INSERT (policy_id, policy_type,premium,end_date, start_date,coverage_amount,customer_id,merged_timestamp ) VALUES  (s.policy_id, s.policy_type,s.premium,s.end_date, s.start_date,s.coverage_amount,s.customer_id,current_timestamp())")

# COMMAND ----------

# MAGIC %md
# MAGIC <b>
# MAGIC Update the merged_flag in the bronze layer

# COMMAND ----------

# MAGIC %sql
# MAGIC UPDATE bronzelayer.policy SET merge_flag = True WHERE merge_flag = FALSE

# COMMAND ----------

