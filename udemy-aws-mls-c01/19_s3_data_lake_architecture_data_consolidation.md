# S3 Data Lake Architecture - Data Consolidation

## Introduction to Data Lake (Lesson 188)

### Concept of Data Lakes and Data Warehouses
- **Data Lake**: Vast pool of raw data, purpose not yet defined.
- **Data Warehouse**: Repository for structured, filtered data processed for a specific purpose.

### Differences Between Data Lakes and Data Warehouses
- **Flexibility**: Data lakes store raw data, more adaptable than data warehouses.
- **Purpose**: Data lakes for undefined future use; data warehouses for known, structured queries.
- **Cost and Time**: Data warehouses are more expensive and less flexible to change.

### Building a Data Lake on AWS
1. **Storage Options**:
   - **S3**: Primary storage solution for data lakes.
   - **Amazon Glacier**: For data backup and long-term archival.

2. **Data Ingestion/Consolidation**:
   - **Kinesis Firehose**: For real-time streaming data capture and loading.
   - **Storage Gateway**: Integrates on-premises data with S3.
   - **Snowball & Snowmobile**: Physical appliances for large-scale data transfer to AWS.
   - **SDK, CLI and more**: AWS SDKs, Command Line tools, third-party tools for S3 data storage.

3. **Metadata and Data Catalog**: Essential for data discoverability and preventing data swamps.
   - **Do-it-yourself**: Manual logic for metadata collection.
   - **AWS Glue**: Automated building and maintaining of data catalog.

### Data Lake vs. Data Swamp
- **Data Swamp**: Unmanaged, inaccessible data lake with little value.
- **Prevention**: Maintain a comprehensive and updated data catalog.

## Kinesis - Streaming and Batch Processing (Lesson 189)

### Overview of Amazon Kinesis
- Ingest, buffer, and process streaming data in real-time.
- Handles massive streaming data from numerous sources with low latency.
- Offers a comprehensive, managed platform for streaming data solutions.

### Understanding Streaming Data
- **Definition**: Data generated continuously, often from multiple sources, with small payloads.
- **Examples**: Log files, fitness monitoring data, social network activities, in-game player actions.

### Comparison: Streaming vs. Batch Processing
1. **Batch Processing**:
   - Data collected and stored in databases or data lakes.
   - Analyzed periodically (hourly, daily, weekly).
   - Suitable for non-time-sensitive analytics.
   - Tools: Spark on EMR, machine learning, etc.

2. **Stream Processing**:
   - Data analyzed as it arrives.
   - Responds within seconds or minutes.
   - Essential for real-time insights and actions.
   - Use Cases: GPS navigation, billing alerts, medical emergency alerts.

### Kinesis Product Family
1. **Kinesis Video Streams**:
   - Securely stream video from various devices.
   - Applications: Video playback, security monitoring, analytics.

2. **Kinesis Data Streams**:
   - Offers control over streaming data for custom real-time applications.
   - Integrates with Kinesis Data Analytics, Spark on EMR, EC2, Lambda.

3. **Kinesis Firehose**:
   - Simplest solution for capturing and processing data streams.
   - Automatically loads data into AWS services (S3, Redshift, Elasticsearch, Splunk).
   - Enables analysis using existing BI tools.

4. **Kinesis Data Analytics**:
   - Query streaming data using SQL.
   - Process and route data to AWS data stores.

## Data Formats and Tools for Data Format Conversion (Lesson 190)

- **Purpose**: Understanding data formats for optimal storage and query performance in AWS Data Lakes.

### Data Formats and Their Strengths
- **Row-Based Formats**:
  - Ideal for reading complete records but inefficient for subset queries.
  - **CSV & Tab-Delimited**: Easy-to-use text formats. 
  - **JSON**: Suitable for web services. Supports data types and hierarchical data.
  - **JSON Lines**: Variant of JSON, stores records in single lines.
  - **Avro**: Optimized row format, ideal for write-heavy scenarios.

- **Columnar Storage Formats**:
  - Optimized for queries on subsets of columns. 
  - **Apache Parquet**: Compressed storage, wide tool support.
  - **Optimized Row Columnar (ORC)**: Similar to Parquet, columnar format.

- Avro, Apache Parquet, and ORC are binary formats.

### Tools for Data Transformation
- **Amazon EMR (Elastic MapReduce)**:
  - Managed Hadoop cluster for running Apache Spark, Hive.
  - Ideal for converting data to/from Parquet, ORC, Avro.

- **Apache Spark**:
  - Load data from S3, transform to Parquet or other formats.

- **AWS Glue ETL**:
  - Automatically generates ETL scripts for data transformation.
  - Uses Scala or Python, runs on Apache Spark.
  - Provisions resources as needed and terminates post-job.

- **Kinesis Firehose**:
  - Supports streaming data transformation.
  - Converts data to Parquet, ORC, retains original data in S3.

## In-Place Analytics and Portfolio of Tools (Lesson 191)

- Explore in-place SQL querying and analytics tools in AWS Data Lakes architecture.
- Data stored in S3 can be queried directly, facilitating a range of analytics applications.

### In-Place Querying Tools
1. **Amazon Athena**:
   - Interactive query service for S3 data using SQL.
   - Serverless, pay-per-query model.
   - Supports CSV, JSON, Parquet, ORC, Avro.
   - Use Case: Ideal for ad-hoc data discovery and SQL querying.

2. **Redshift Spectrum**:
   - Queries data on S3 directly.
   - Advanced query optimization, distributed across nodes.
   - Integrates with Redshift data warehouse.
   - Use Case: Suited for complex queries and large user bases.

### Querying Streaming Data
1. **Kinesis Data Analytics**:
   - SQL querying for streaming data.
   - Continuously running queries for real-time monitoring.
   - Use Case: Real-time analytics on streaming data.

### Broader Analytics Portfolio
1. **Amazon EMR**:
   - Runs Hadoop workloads (Spark, Hive, HBase).
   - Consumes data from S3.

2. **Amazon SageMaker**:
   - Machine learning with supervised, unsupervised, and reinforcement learning.
   - Trains on data in S3, provides real-time and batch predictions.

3. **Amazon AI Services**:
   - Pre-built services for video and image analysis, NLP.
   - Analyzes data in S3.

4. **Amazon QuickSight**:
   - BI tool for interactive dashboards.
   - Connects to Redshift, Athena, databases, S3.

5. **Amazon Redshift**:
   - Petabyte-scale data warehouse.
   - Loads data from S3, extends with Redshift Spectrum.

6. **AWS Lambda**:
   - Executes business logic for data lake.
   - Integrates with S3 data lake.

## Monitoring and Optimization (Lesson 192)

### Monitoring Tools
1. **AWS CloudWatch**:
   - Monitors health of data lake components.
   - Tracks metrics, sets alarms, and automates responses.
   - Supports both AWS-generated and custom application metrics.
   - Includes CloudWatch Logs for log file consolidation and event monitoring.

2. **AWS CloudTrail**:
   - Provides an audit trail of all AWS API activities.
   - Captures actions across web console, CLI, SDKs.
   - CloudTrail logs are queryable using Athena and SQL.

### Data Storage Optimization
- **S3 Lifecycle Management**:
  - Automates migration to lower-cost storage tiers.
  - Deletes obsolete data.
  - Based on asset age, name, tags, and folder structure.

- **Storage Classes**:
  - **S3 Standard**: For frequently accessed ("hot") data.
  - **S3 Infrequent Access**: Lower-cost for rarely used but immediately needed data ("warm" data).
  - **Glacier**: Low-cost for archives and backups, suitable for "cold" data.

- **Intelligent Tiering**
   - Automatically moves data between frequent and infrequent access tiers.
   - Eliminates retrieval fees.
   - Ideal for data with unpredictable access patterns.

- **Glacier and Deep Archive**
   - **Glacier**: For long-term storage with access time from minutes to hours.
   - **Glacier Deep Archive**: Cheapest, for long-term storage with 12-48 hours retrieval time.
   - **Vault Lock**: Ensures immutability of objects for compliance needs.

- **Data Formats**
   - Using formats like Parquet can significantly reduce storage and query costs.
   - Improves query performance.
   - Essential for efficient data management in a data lake.

## Security and Protection (Lesson 193)

### Access Control
- **Resource-Based Policies**:
   - Attached directly to resources like S3 buckets or objects.
   - Enforce policies that should not be bypassed (e.g., access only from corporate network).

- **User-Based Policies**:
   - Permissions granted directly to users.
   - Recommended for easier management via role-based groups.
   - Assign users to groups with specific permissions.

### Data Encryption
- **Server-Side Encryption**:
  - Data encrypted at rest in S3.
  - Managed through AWS Key Management Service (KMS).
  - Options for default S3 keys or customer-managed keys in KMS.
  - Customer-managed keys add an extra layer of security.

- **Client-Side Encryption**:
  - Encrypt data before storing in S3.
  - Maintain keys in KMS for enhanced security.

### Data Durability and Versioning
- **S3 Durability**:
  - Offers 99.999999999% (11 9s) durability.
  - Redundant data storage across multiple availability zones.

- **Versioning**:
  - Protects against accidental or malicious modifications and deletions.
  - Enables restoration of previous object versions.
  - Supports lifecycle rules for version management.

- **Multi-Factor Authentication (MFA)**: adds an additional layer of security for object deletion or modification.

- **Disaster Recovery**: Cross-Region Replication (CRR)
  - Maintains a copy of the S3 bucket in a different region.
  - Ensures data availability in case of regional disruptions.

### Tag-Based Security
- Classify objects using key-value pairs (e.g., PHI for protected health information).
- Define security policies based on tags.
- Restrict access to sensitive data to authorized users.

## Lab - Glue Data Catalog (Lesson 194 & 195)

### 1. Setting Up Permissions for Glue
1. Open IAM Console
2. Create Role, select "Glue"
3. On the Permissions page, search for "Glue". Select `AWSGlueServiceRole` policy.
4. Name the role `AWSGlueServiceRoleDefault`.
5. Create the role.

### 2. S3 Bucket Setup
1. Create S3 Bucket. Use naming convention: `aws-glue-yourname`.
2. In the bucket, create a folder named `iris`.
3. Inside `iris`, create a subfolder `csv`.
4. In the course distribution, find [iris_all.csv](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/DataLake/Iris/iris_all.csv).
5. Place `iris_all.csv` in the `iris/csv` folder of your S3 bucket.

### 3. Configure Glue Crawler
1. Open Glue Console. Ensure the region matches your S3 bucket.
2. Create Crawler. Name the crawler `iris_csv_crawler`.
3. Choose "Data Stores" as the source and set "Crawl all folders".
4. Select "S3" as the data store.
5. Choose "Specified path in my account". Include path: `s3://aws-glue-yourname/iris/csv/`.
5. Set IAM Role. Select the `AWSGlueServiceRoleDefault` role.
7. Add a new database named `demo_db`. 
8. Prefix tables with `iris_`.
6. Crawler Frequency: Choose "Run on demand".
7. Run the crawler.
8. Wait for the crawler to complete (check for "Tables added" count).
9. Go to "Tables" in Glue. Select the `iris_csv` table. Review schema details and data types.


## Lab – Query with Athena (Lesson 196 & 197)

- Learn to query Iris data using Amazon Athena.

### Athena Configuration
1. Open Athena Console. From the AWS console, access the Athena service.
2. In Athena, expand the left navigation and select "Query editor".

### Setup Query Results
1. Before running queries, set up an S3 location for query results.
2. Click on "View Settings", then "Manage".
3. Follow the recommended naming convention: `aws-athena-query-results-MyAcctID-MyRegion`.
4. Example S3 location: `s3://aws-athena-query-results-1234567890-us-east-1/`.
5. Save the changes.

### Running Queries
1. **Select Data Source & Database**:
   - In the Query Editor, ensure the Editor tab is selected.
   - For Data source, choose `AWSDataCatalog`.
   - Select `demo_db` as the database.
2. **Preview Table**:
   - Find the `iris_csv` table under Tables.
   - Click the three dots next to `iris_csv`, select "Preview table".
   - This generates a sample SQL query: `SELECT * FROM "demo_db"."iris_csv" limit 10;`.

### Example Queries
- **Query Specific Class**:
  ```sql
  SELECT * FROM "demo_db"."iris_csv"
  WHERE class = 'Iris-setosa';
  ```

- **Wildcard Query**:
  ```sql
  SELECT * FROM "demo_db"."iris_csv"
  WHERE class like '%setosa%';
  ```

- **Count Records**:
  ```sql
  SELECT count(*) AS COUNT FROM "demo_db"."iris_csv"
  ```

- **Compute Area**:
  ```sql
  SELECT sepal_length, sepal_width,
  sepal_length * sepal_width as sepal_area
  FROM "demo_db"."iris_csv";
  ```

## 198. Glue ETL - Pandas DataFrame vs Spark DataFrame vs Glue DynamicFrame

### Introduction
- **Objective**: Understand ETL (Extraction, Transformation, and Loading) functions in AWS Glue.
- **ETL Explained**: 
  - **Extraction**: Data is sourced from various databases or files.
  - **Transformation**: Data is converted into a format suitable for analysis, involving merging from different sources, data type conversions, handling missing values, data cleansing, and organization.
  - **Loading**: Clean data is loaded to destinations like data lakes or warehouses.
- **Glue ETL Service**: AWS Glue offers a fully managed environment for running data transformation jobs using a serverless Apache Spark environment.

### Underlying Concepts
- **DataFrames in Python & R**: Common for small to medium datasets. Data is loaded into memory for fast processing.
- **Apache Spark**: Suitable for large datasets; data is distributed across a cluster of machines.
- **Glue Dynamic Frame**: Specific to Glue ETL, similar to Spark DataFrame but with additional features for ETL workflows.

### Dynamic Frame Features
- **Integration with Glue Catalog**: Access to more data sources including Amazon S3, Redshift, RDS, etc.
- **Handling Mixed Data Types**: Uses choice or union types to manage fields with mixed data types.
- **Resolving Data Inconsistencies**: Convert a column to a single data type or keep all data types as separate columns.
- **Conversion to Spark DataFrame**: Easily convert between Glue Dynamic Frame and Apache Spark DataFrame.

### Bookmarks in Glue
- **Usage**: Track data processed in previous ETL job runs.
- **Avoid Reprocessing**: Only process new data in scheduled job runs.
- **Strategies**: Different methods to identify new data based on the data source.

### Types of Jobs in Glue
1. **Spark Jobs**: Batch data processing.
2. **Streaming ETL Jobs**: Continuous processing of streaming data.
3. **Python Shell Jobs**: Run Python scripts without Apache Spark.
4. **Radio Jobs**: New capability for machine learning workflows.

### Summary
- **DataFrames**: Used for small/medium datasets on a single machine.
- **Apache Spark**: For large-scale data processing.
- **Glue Dynamic Frame**: Optimized for ETL workflows with additional features for AWS integrations.
- **Bookmarks**: For incremental processing of new data.
- **Job Types in Glue**: Cater to different data processing needs including machine learning workflows.
- **Usage**: Dynamic Frame for AWS integrations; Spark DataFrame for data processing and transformation.

## Labs (Lecture 199 - 205)

1. Glue ETL - Convert format to Parquet (Lecture 199)
2. Query Amazon Customer Reviews with Athena (Lecture 200)
3. Sentiment of the Customer Review (Lecture 201)
4. Query Sentiment of Customer Reviews using Athena (Lecture 202)
5. Serverless Customer Review Solution Part 1 (Lecture 204)
6. Serverless Customer Review Solution Part 2 (Lecture 205)
