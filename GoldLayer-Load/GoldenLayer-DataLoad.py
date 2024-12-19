# Databricks notebook source
# MAGIC %md
# MAGIC <b> Sales By Policy Type and Month: </b>
# MAGIC This table would contain the total sales for each policy type and each month. It would be used to analyze the performance of different policy types over time.

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace temp view vw_sales_by_policy_type_and_month as
# MAGIC SELECT  
# MAGIC     p.policy_type,
# MAGIC     EXTRACT(MONTH FROM p.start_date) AS sale_month,
# MAGIC     SUM(p.premium) AS total_premium
# MAGIC FROM 
# MAGIC     silverlayer.policy p
# MAGIC GROUP BY 
# MAGIC     p.policy_type, 
# MAGIC     EXTRACT(YEAR FROM p.start_date),
# MAGIC     EXTRACT(MONTH FROM p.start_date);

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from vw_sales_by_policy_type_and_month

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO goldenlayer.sales_by_policy_type_and_month AS T
# MAGIC USING vw_sales_by_policy_type_and_month AS S
# MAGIC ON T.policy_type = S.policy_type
# MAGIC    AND T.sale_month = S.sale_month
# MAGIC WHEN MATCHED THEN
# MAGIC   UPDATE SET 
# MAGIC     T.total_premium = S.total_premium,
# MAGIC     T.updated_timestamp = current_timestamp()
# MAGIC WHEN NOT MATCHED THEN
# MAGIC   INSERT (
# MAGIC     policy_type,
# MAGIC     sale_month,
# MAGIC     total_premium,
# MAGIC     updated_timestamp
# MAGIC   )
# MAGIC   VALUES (
# MAGIC     S.policy_type,
# MAGIC     S.sale_month,
# MAGIC     S.total_premium,
# MAGIC     current_timestamp()
# MAGIC   );
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC <b>Claims By Policy Type and Status:</b>
# MAGIC  This table would contain the number and amount of claims by policy type and claim status. It would be used to monitor the claims process and identify any trends or issues.

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace temp view vw_gold_claims_by_policy_type_and_status
# MAGIC AS
# MAGIC SELECT
# MAGIC   policy_type,
# MAGIC   claim_status,
# MAGIC   SUM(claim_amount) AS total_claims_amount,
# MAGIC   COUNT(*) AS total_claims
# MAGIC FROM 
# MAGIC   silverlayer.claim c
# MAGIC JOIN
# MAGIC   silverlayer.policy p ON c.policy_id = p.policy_id
# MAGIC GROUP BY
# MAGIC   policy_type,
# MAGIC   claim_status having p.policy_type is not null;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from vw_gold_claims_by_policy_type_and_status

# COMMAND ----------

# MAGIC %sql
# MAGIC Merge into goldenlayer.claims_by_policy_type_and_status AS T USING vw_gold_claims_by_policy_type_and_status AS S
# MAGIC ON t.policy_type = s.policy_type and t.claim_status = s.claim_status
# MAGIC WHEN MATCHED THEN
# MAGIC   UPDATE SET 
# MAGIC   T.total_claims_amount = s.total_claims_amount,
# MAGIC   T.total_claims = s.total_claims,
# MAGIC   T.updated_timestamp = current_timestamp()
# MAGIC WHEN NOT MATCHED THEN
# MAGIC INSERT(
# MAGIC   policy_type,
# MAGIC   claim_status,
# MAGIC   total_claims_amount,
# MAGIC   total_claims,
# MAGIC   updated_timestamp
# MAGIC )
# MAGIC VALUES(
# MAGIC   s.policy_type,
# MAGIC   s.claim_status,
# MAGIC   s.total_claims_amount,
# MAGIC   s.total_claims,
# MAGIC   current_timestamp()
# MAGIC )

# COMMAND ----------

# MAGIC %md
# MAGIC <b>
# MAGIC Analyze the claim data based on the policy type like AVG, MAX, MIN, Count of claim.

# COMMAND ----------

# MAGIC %sql
# MAGIC create or replace temp view vw_gold_claims_analysis as
# MAGIC SELECT
# MAGIC   policy_type,
# MAGIC   SUM(claim_amount) AS sum_claim_amount,
# MAGIC   AVG(claim_amount) AS avg_claim_amount,
# MAGIC   MIN(claim_amount) AS min_claim_amount,
# MAGIC   MAX(claim_amount) AS max_claim_amount,
# MAGIC   COUNT (DISTINCT claim_id) AS total_claims
# MAGIC FROM
# MAGIC   silverlayer.claim c
# MAGIC JOIN 
# MAGIC   silverlayer.policy p
# MAGIC ON c.policy_id = p.policy_id
# MAGIC GROUP BY
# MAGIC policy_type having p.policy_type is NOT NULL;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from vw_gold_claims_analysis

# COMMAND ----------

# MAGIC %sql
# MAGIC Merge into goldenlayer.claims_analysis AS T USING vw_gold_claims_analysis AS S
# MAGIC ON t.policy_type = s.policy_type
# MAGIC WHEN MATCHED THEN
# MAGIC   UPDATE SET 
# MAGIC   T.sum_claim_amount = s.sum_claim_amount,
# MAGIC   T.avg_claim_amount = s.avg_claim_amount,
# MAGIC   T.min_claim_amount = s.min_claim_amount,
# MAGIC   T.max_claim_amount = s.max_claim_amount,
# MAGIC   T.total_claims = s.total_claims,
# MAGIC   T.updated_timestamp = current_timestamp()
# MAGIC WHEN NOT MATCHED THEN
# MAGIC INSERT(
# MAGIC   policy_type,
# MAGIC   sum_claim_amount,
# MAGIC   avg_claim_amount,
# MAGIC   min_claim_amount,
# MAGIC   max_claim_amount,
# MAGIC   total_claims,
# MAGIC   updated_timestamp
# MAGIC )
# MAGIC VALUES(
# MAGIC   s.policy_type,
# MAGIC   s.sum_claim_amount,
# MAGIC   s.avg_claim_amount,
# MAGIC   s.min_claim_amount,
# MAGIC   s.max_claim_amount,
# MAGIC   s.total_claims,
# MAGIC   current_timestamp()
# MAGIC )

# COMMAND ----------

