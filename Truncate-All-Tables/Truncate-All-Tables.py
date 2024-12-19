# Databricks notebook source
# Define the list of tables to truncate
tables = ['agent', 'branch', 'claim', 'customer', 'policy', 
          'claims_analysis', 'claims_by_policy_type_and_status', 'sales_by_policy_type_and_month']

# Define the list of databases
databases = ['bronzelayer', 'silverlayer', 'goldenlayer']

# Loop through databases and tables to truncate if they exist
for database in databases:
    for table in tables:
        # Check if the table exists in the current database
        table_check_query = f"SHOW TABLES IN {database} LIKE '{table}'"
        result = spark.sql(table_check_query)
        
        # If the table exists, truncate it
        if not result.isEmpty():
            truncate_query = f"TRUNCATE TABLE {database}.{table}"
            spark.sql(truncate_query)
            print(f"Truncated table {database}.{table}")
        else:
            print(f"Table {database}.{table} does not exist in {database}.")