<h1>Smart Policy Data System: A Data Lakehouse Architecture</h1>

<h2>Problem Statement</h2>
<p>Insurance companies collect large amounts of policy data from various sources like agents, online forms, mobile apps, and customer service calls. However, this data is often incomplete, outdated, or contains errors, making it difficult to trust and use for risk analysis, claims processing, or customer insights. This project addresses the issue of Iow data veracity in insurance policy records.
Using Azure Cloud and Big Data technologies, the project aims to clean, validate, and manage policy
data more accurately and efficiently, ensuring that decision-making is based on reliable and up-to-date information.</p>

<h2>Project Overview</h2>
<p>The <strong>Smart Policy Data System</strong> is a comprehensive data engineering project designed to streamline policy data integration, transformation, and analysis. This project leverages modern data engineering tools and best practices to create a robust three-layered (Bronze/Silver/Gold) architecture, ensuring data quality, consistency, and scalability.</p>

<h2>Source Systems</h2>
<ul>
  <li><strong>Azure SQL Database</strong>: Branch, Claim, and Agent data.</li>
  <li><strong>ADLS (Azure Data Lake Storage)</strong>:
    <ul>
      <li>JSON files: Policy data (updated daily).</li>
      <li>CSV files: Customer information (updated daily).</li>
    </ul>
  </li>
  <li><strong>Azure Data Factory (ADF)</strong>: Pipelines for orchestrating data workflows.</li>
</ul>

<h2>Architecture Overview: Each layer is a data </h2>
<ul>
  <li><strong>Bronze Layer</strong>: Raw data ingestion and storage.</li>
  <li><strong>Silver Layer</strong>: Cleaned and transformed data ready for analysis</li>
  <li><strong>Gold Layer</strong>: Aggregated data stored used for reporting.</li>
</ul>

<h2>Implementation Steps</h2>
<ol>
  <li><strong>Data Ingestion</strong>:
    <ul>
      <li>Load raw data (JSON and CSV) from ADLS, SQL Tables to the Bronze Layer in Databricks as Delta Tables.</li>
      <li>Move processed files to the processed/{data} folder in ADLS.</li>
    </ul>
  </li>
  <li><strong>Data Transformation</strong>:
    <ul>
      <li>Clean and transform data in the Silver Layer.</li>
      <li>Merge new data by pulling records where merged_flag (used to indicate whether data from bronze layer has been processed to silver layer) is false from the Bronze Layer.</li>
      <li>Update the merged_flag to true for processed records.</li>
    </ul>
  </li>
  <li><strong>Data Aggregation</strong>:
    <ul>
      <li>Create custom tables in the Gold Layer to answer business questions.</li>
      <li>Store each query result as a table in the Gold Layer.</li>
    </ul>
  </li>
  <li><strong>Visualization</strong>:
    <ul>
      <li>Use Power BI to access the Gold Layer and create insightful reports and dashboards.</li>
    </ul>
  </li>
</ol>

<h2>Tools and Technologies</h2>
<ul>
  <li><strong>Azure Data Lake Storage (ADLS)</strong>: Centralized storage for raw and processed data.</li>
  <li><strong>Azure Data Factory (ADF)</strong>: Orchestrating data pipelines.</li>
  <li><strong>Databricks</strong>: Data transformation and Lakehouse implementation.</li>
  <li><strong>Power BI</strong>: Data visualization and reporting.</li>
</ul>

<h2>Directory Structure</h2>
<pre>
landing/{data}                          # Raw data ingestion
bronzelayer/{data}                      # Delta tables for raw data
processed/{data}                        # Processed files
silverlayer/{data}                      # Cleaned and transformed data
goldenlayer/{AggregatedData}            # Aggregated query results
</pre>

<h2>High-Level Architecture and Implementation</h2>
<p>Below are the diagrams illustrating the high-level architecture and project implementation:</p>
<ul>
  <li><img src="https://drive.google.com/uc?id=185JZ43LNl2mk1xEwDNEYWUWzg0bc8rOt" alt="High-Level Architecture" /></li>
  <li><img src="https://drive.google.com/uc?id=1ftN_PvHilpdBkEL4sux7HBv4Pj7KRcqE" alt="Project Implementation" /></li>
</ul>
