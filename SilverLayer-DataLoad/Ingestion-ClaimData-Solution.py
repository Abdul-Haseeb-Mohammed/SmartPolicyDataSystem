# Databricks notebook source
# MAGIC %md
# MAGIC <b>Remove all where claim_id, policy_id is ,claim status,claim_amount,lastupdated null
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <b>Remove all rows where policy_id Id not exist in Policy table
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <b>Convert date_of_claim to Date column with formate (MM-dd-yyyy)
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <b>Ensure  claim amount is >0

# COMMAND ----------

df = spark.sql("SELECT c.claim_id, c.claim_amount, c.LastUpdatedTimeStamp, c.policy_id, c.claim_status, to_date(date_format(c.date_of_claim, 'MM-dd-yyyy'), 'MM-dd-yyyy') as date_of_claim from bronzelayer.claim c INNER JOIN bronzelayer.policy p ON c.policy_id = p.policy_id  WHERE c.claim_amount  is not null and c.claim_id is not null and c.policy_id is not null and c.claim_status is not null and c.LastUpdatedTimeStamp is not null and c.merge_flag = FALSE and c.claim_amount >0")

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC <b>Add the merged_date_timestamp (current timesatmp)

# COMMAND ----------

df.createOrReplaceTempView('clean_claim')


# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO silverlayer.Claim AS T USING clean_claim AS S ON 
# MAGIC   t.claim_id = s.claim_id WHEN MATCHED THEN
# MAGIC   UPDATE SET
# MAGIC
# MAGIC       t.claim_amount = s.claim_amount,
# MAGIC       t.LastUpdatedTimeStamp = s.LastUpdatedTimeStamp,
# MAGIC       t.policy_id = s.policy_id,
# MAGIC       t.claim_status = s.claim_status,
# MAGIC     t.date_of_claim = s.date_of_claim,
# MAGIC       t.merged_timestamp = current_timestamp()
# MAGIC
# MAGIC   WHEN not MATCHED THEN
# MAGIC
# MAGIC   INSERT (claim_id,claim_amount, LastUpdatedTimeStamp, policy_id, claim_status, date_of_claim,merged_timestamp ) 
# MAGIC   VALUES (s.claim_id, s.claim_amount, s.LastUpdatedTimeStamp, s.policy_id, s.claim_status, s.date_of_claim,current_timestamp())
# MAGIC

# COMMAND ----------

spark.sql(" UPDATE bronzelayer.claim set merge_flag = TRUE where merge_flag = FALSE")