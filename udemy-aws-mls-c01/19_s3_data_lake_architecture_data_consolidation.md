# 188. Introduction to Data Lake

## Concept of Data Lakes and Data Warehouses
- **Data Lake**: Vast pool of raw data, purpose not yet defined.
- **Data Warehouse**: Repository for structured, filtered data processed for a specific purpose.

## Differences Between Data Lakes and Data Warehouses
- **Flexibility**: Data lakes store raw data, more adaptable than data warehouses.
- **Purpose**: Data lakes for undefined future use; data warehouses for known, structured queries.
- **Cost and Time**: Data warehouses are more expensive and less flexible to change.

## Building a Data Lake on AWS
1. **Storage Options**:
   - **S3 (Simple Storage Service)**: Primary storage solution for data lakes.
   - **Amazon Glacier**: For data backup and long-term archival.

2. **Data Consolidation**:
   - **Kinesis Firehose**: For real-time streaming data capture and loading.
   - **Storage Gateway**: Integrates on-premises data with S3.
   - **Snowball & Snowmobile**: Physical appliances for large-scale data transfer to AWS.

3. **Data Ingestion and Migration**:
   - Tools: AWS SDKs, Command Line tools, third-party tools for S3 data storage.

4. **Metadata and Data Catalog**:
   - **Importance**: Essential for data discoverability and preventing data swamps.
   - **Approaches**:
     - Manual logic for metadata collection.
     - **AWS Glue**: Automated building and maintaining of data catalog.

## Data Lake vs. Data Swamp
- **Data Swamp**: Unmanaged, inaccessible data lake with little value.
- **Prevention**: Maintain a comprehensive and updated data catalog.

## Importance of a Data Catalog
- **Function**: Provides a queryable interface for all assets in the data lake.
- **Implementation**:
  - Lambda functions to collect metadata.
  - DynamoDB and Elasticsearch for metadata storage and querying.
  - AWS Glue for automated data cataloging.

## Conclusion
- A data lake on AWS combines storage, data ingestion, migration, and cataloging.
- It's a flexible and scalable solution for storing and managing large volumes of raw data.

# 189. Kinesis - Streaming and Batch Processing

## Overview of Amazon Kinesis
- **Purpose**: Ingest, buffer, and process streaming data in real-time.
- **Capability**: Handles massive streaming data from numerous sources with low latency.
- **Fully Managed**: Offers a comprehensive, managed platform for streaming data solutions.

## Understanding Streaming Data
- **Definition**: Data generated continuously, often from multiple sources, with small payloads.
- **Examples**: Log files, fitness monitoring data, social network activities, in-game player actions.

## Comparison: Streaming vs. Batch Processing
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

## Kinesis Product Family
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

## Building Streaming Applications with Kinesis
- Combine Kinesis capabilities to create complex streaming data pipelines.
- Example: Firehose output processed by Data Analytics and routed to data stores.

## Conclusion
- Amazon Kinesis offers robust solutions for managing and analyzing streaming data in real-time.
- It's a versatile platform suitable for a variety of real-time analytics and processing needs.

# 190. Data Formats and Tools for Data Format Conversion

## Overview
- **Purpose**: Understanding data formats for optimal storage and query performance in AWS Data Lakes.
- **Focus**: Compare popular data formats and explore tools for data format conversion.

## Data Formats and Their Strengths
1. **Row-Based Formats**:
   - **CSV & Tab-Delimited**: Easy-to-use text formats. Ideal for reading complete records but inefficient for subset queries.
   - **JSON**: Suitable for web services. Supports data types and hierarchical data.
   - **JSON Lines**: Variant of JSON, stores records in single lines.

2. **Columnar Storage Formats**:
   - **Apache Parquet**: Optimized for queries on subsets of columns. Compressed storage, wide tool support.
   - **Optimized Row Columnar (ORC)**: Similar to Parquet, columnar format.
   - **Avro**: Optimized row format, ideal for write-heavy scenarios.

3. **Comparison**: 
   - Row formats are better for complete record retrieval.
   - Columnar formats are efficient for subset queries and compression.
   - Binary formats (Parquet, ORC, Avro) require tools or SDKs for interaction.

## When to Convert Data Formats
- **Recommended Approach**: Collect data in native format, then transform for analytics in the data lake.
- **Conversion Scenarios**:
  - Data transformation for analytics.
  - Converting to efficient formats like Parquet for space savings and query performance.

## Tools for Data Transformation
1. **Amazon EMR (Elastic MapReduce)**:
   - Managed Hadoop cluster for running Apache Spark, Hive.
   - Ideal for converting data to/from Parquet, ORC, Avro.

2. **Apache Spark**:
   - Load data from S3, transform to Parquet or other formats.

3. **AWS Glue ETL**:
   - Automatically generates ETL scripts for data transformation.
   - Uses Scala or Python, runs on Apache Spark.
   - Provisions resources as needed and terminates post-job.

4. **Kinesis Firehose**:
   - Supports streaming data transformation.
   - Converts data to Parquet, ORC, retains original data in S3.

## Conclusion
- Understanding and choosing the right data format is crucial for efficient data storage and querying in AWS Data Lakes.
- AWS offers multiple tools for data format conversion, catering to different use cases and data transformation needs.

# 191. In-Place Analytics and Portfolio of Tools

## Overview
- **Purpose**: Explore in-place SQL querying and analytics tools in AWS Data Lakes architecture.
- **Context**: Data stored in S3 can be queried directly, facilitating a range of analytics applications.

## In-Place Querying Tools
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

3. **Kinesis Data Analytics**:
   - SQL querying for streaming data.
   - Continuously running queries for real-time monitoring.
   - Use Case: Real-time analytics on streaming data.

## Selecting Between Athena and Redshift Spectrum
- **Athena**: Best for ad-hoc querying and simple to moderate SQL tasks.
- **Redshift Spectrum**: Optimal for intricate querying scenarios and supporting multiple concurrent users.

## Broader Analytics Portfolio
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

## Conclusion
- A data lake must be flexible to accommodate a variety of tools.
- AWS offers a comprehensive set of tools for querying and analyzing data in S3-based data lakes.
- Choice of tools depends on specific use cases, complexity, and scale requirements.

# 192. Monitoring and Optimization

## Overview
- **Purpose**: Discuss tools for monitoring and optimizing AWS data lakes.
- **Focus**: Ensure health and cost-efficiency of data lake components.

## Monitoring Tools
1. **AWS CloudWatch**:
   - Monitors health of data lake components.
   - Tracks metrics, sets alarms, and automates responses.
   - Supports both AWS-generated and custom application metrics.
   - Includes CloudWatch Logs for log file consolidation and event monitoring.

2. **AWS CloudTrail**:
   - Provides an audit trail of all AWS API activities.
   - Captures actions across web console, CLI, SDKs.
   - CloudTrail logs are queryable using Athena and SQL.

## Data Storage Optimization
### Lifecycle Management and Storage Classes
- **S3 Lifecycle Management**:
  - Automates migration to lower-cost storage tiers.
  - Deletes obsolete data.
  - Based on asset age, name, tags, and folder structure.

- **Storage Classes**:
  - **S3 Standard**: For frequently accessed ("hot") data.
  - **S3 Infrequent Access**: Lower-cost for rarely used but immediately needed data ("warm" data).
  - **Glacier**: Low-cost for archives and backups, suitable for "cold" data.

### Intelligent Tiering
- Automatically moves data between frequent and infrequent access tiers.
- Eliminates retrieval fees.
- Ideal for data with unpredictable access patterns.

### Glacier and Deep Archive
- **Glacier**: For long-term storage with access time from minutes to hours.
- **Glacier Deep Archive**: Cheapest, for long-term storage with 12-48 hours retrieval time.
- **Vault Lock**: Ensures immutability of objects for compliance needs.

### Format Optimization
- Using formats like Parquet can significantly reduce storage and query costs.
- Improves query performance.
- Essential for efficient data management in a data lake.

## Conclusion
- Effective monitoring and optimization are crucial for maintaining a healthy and cost-effective data lake.
- AWS offers a suite of tools for monitoring, auditing, and optimizing data storage and access.
- Leveraging these tools can enhance the performance and reduce the costs associated with data lakes.

# 193. Security and Protection

## Overview
- **Purpose**: Discuss strategies for securing and managing data in AWS data lakes.
- **Key Focus**: Utilize AWS S3 for data security and management.

## Access Control
1. **Resource-Based Policies**:
   - Attached directly to resources like S3 buckets or objects.
   - Enforce policies that should not be bypassed (e.g., access only from corporate network).

2. **User-Based Policies**:
   - Permissions granted directly to users.
   - Recommended for easier management via role-based groups.
   - Assign users to groups with specific permissions.

## Data Encryption
- **Server-Side Encryption**:
  - Data encrypted at rest in S3.
  - Managed through AWS Key Management Service (KMS).
  - Options for default S3 keys or customer-managed keys in KMS.
  - Customer-managed keys add an extra layer of security.

- **Client-Side Encryption**:
  - Encrypt data before storing in S3.
  - Maintain keys in KMS for enhanced security.

## Data Durability and Versioning
- **S3 Durability**:
  - Offers 99.999999999% (11 9s) durability.
  - Redundant data storage across multiple availability zones.

- **Versioning**:
  - Protects against accidental or malicious modifications and deletions.
  - Enables restoration of previous object versions.
  - Supports lifecycle rules for version management.

## Multi-Factor Authentication (MFA)
- Adds an additional layer of security for object deletion or modification.

## Disaster Recovery
- **Cross-Region Replication (CRR)**:
  - Maintains a copy of the S3 bucket in a different region.
  - Ensures data availability in case of regional disruptions.

## Data Classification with Object Tagging
- **Tag-Based Security**:
  - Classify objects using key-value pairs (e.g., PHI for protected health information).
  - Define security policies based on tags.
  - Restrict access to sensitive data to authorized users.

## Conclusion
- AWS S3 offers comprehensive features to secure and protect data in a centralized data lake.
- Implementing these security measures is crucial as part of the shared responsibility model in cloud computing.
- Proper configuration of these features aligns with organizational security needs.

## Action Points
- Assess current data lake security measures.
- Implement appropriate encryption, versioning, and access control policies.
- Regularly review and update security configurations to align with evolving organizational needs.

# 194. Lab Instructions - Glue Data Catalog

## Introduction
- **Objective**: Configure a crawler in AWS Glue.
- **Context**: Complements "Lab - Glue Data Catalog" video.
- **Recommendation**: Watch the video first, then follow these instructions.

## Setting Up Permissions for Glue
1. **Open IAM Console**:
   - Navigate to the AWS IAM service console.
2. **Create Role**:
   - Select "Roles" from the left pane.
   - Click "Create Role".
   - Choose AWS service, then select "Glue".
3. **Assign Policy**:
   - On the Permissions page, search for "Glue".
   - Select `AWSGlueServiceRole` policy.
   - Proceed to the Review page.
   - Name the role `AWSGlueServiceRoleDefault`.
   - Create the role.

## S3 Bucket Setup
1. **Create S3 Bucket**:
   - Use naming convention: `aws-glue-yourname`.
   - The prefix `aws-glue-` is required as per IAM role permissions.
   - Ensure the bucket is in the intended region.
   - Example: `aws-glue-cl` in N.Virginia.
2. **Create Folders**:
   - In the bucket, create a folder named `iris`.
   - Inside `iris`, create a subfolder `csv`.

## Upload Data
- **File Location**: In the course distribution, under `DataLake/Iris`, find `iris_all.csv`.
- **Upload**: Place `iris_all.csv` in the `iris/csv` folder of your S3 bucket.

## Configure Glue Crawler
1. **Open Glue Console**:
   - Ensure the region matches your S3 bucket.
2. **Create Crawler**:
   - Go to "Crawler" in the left pane.
   - Name the crawler `iris_csv_crawler`.
3. **Input Specification**:
   - Choose "Datastores" as the source.
   - Set "Crawl all folders".
4. **Datastore Configuration**:
   - Select S3 as the data store.
   - Choose `Specified path in my account`.
   - Include path: `s3://aws-glue-yourname/iris/csv/`.
5. **Set IAM Role**:
   - Select the `AWSGlueServiceRoleDefault` role.
6. **Crawler Frequency**:
   - Choose "Run on demand".
7. **Output Configuration**:
   - Add a new database named `demo_db`.
   - Prefix tables with `iris_`.

## Run Crawler
1. **Start Crawler**:
   - Select `iris_csv_crawler`.
   - Click "Run Crawler".
   - Wait for the crawler to complete (check for "Tables added" count).

## Explore Glue Tables
1. **View Table Details**:
   - Go to "Tables" in Glue.
   - Select the `iris_csv` table.
   - Review schema details and data types.

## Summary
- Accomplished metadata collection for data lake files using Glue Catalog.
- Users can now explore data lake content via the catalog, abstracting file details.
- Prepared for SQL querying in the next lab activity.

# 195. Lab – Glue Data Catalog

## Introduction
- **Objective**: Learn to query Iris data using Amazon Athena.
- **Context**: Complements "Lab - Athena In-place Querying" video.
- **Recommendation**: Watch the video first, then use these instructions.

## Athena Configuration
1. **Open Athena Console**:
   - From the AWS console, access the Athena service.
2. **Query Editor**:
   - In Athena, expand the left navigation and select "Query editor".

## Setup Query Results
- **Configure S3 Location**:
  - Before running queries, set up an S3 location for query results.
  - Click on "View Settings", then "Manage".
  - Follow the recommended naming convention: `aws-athena-query-results-MyAcctID-MyRegion`.
  - Example S3 location: `s3://aws-athena-query-results-1234567890-us-east-1/`.
  - Save the changes.

## Running Queries
1. **Select Data Source & Database**:
   - In the Query Editor, ensure the Editor tab is selected.
   - For Data source, choose `AWSDataCatalog`.
   - Select `demo_db` as the database.
2. **Preview Table**:
   - Find the `iris_csv` table under Tables.
   - Click the three dots next to `iris_csv`, select "Preview table".
   - This generates a sample SQL query: `SELECT * FROM "demo_db"."iris_csv" limit 10;`.

## Example Queries
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

## Summary

- Learned to directly query S3 data using SQL in Athena.
- Athena's serverless approach enables easy access to large amounts of unstructured data.

# 197. Lab - Query with Athena

# 198. Glue ETL - Pandas DataFrame vs Spark DataFrame vs Glue DynamicFrame

## Introduction
- **Objective**: Understand ETL (Extraction, Transformation, and Loading) functions in AWS Glue.
- **EDL Explained**: 
  - **Extraction**: Data is sourced from various databases or files.
  - **Transformation**: Data is converted into a format suitable for analysis, involving merging from different sources, data type conversions, handling missing values, data cleansing, and organization.
  - **Loading**: Clean data is loaded to destinations like data lakes or warehouses.

## Glue ETL Service
- **Managed Service**: AWS Glue offers a fully managed environment for running data transformation jobs using a serverless Apache Spark environment.

## Underlying Concepts
- **DataFrames in Python & R**: Common for small to medium datasets. Data is loaded into memory for fast processing.
- **Apache Spark**: Suitable for large datasets; data is distributed across a cluster of machines.
- **Glue Dynamic Frame**: Specific to Glue ETL, similar to Spark DataFrame but with additional features for ETL workflows.

## Dynamic Frame Features
- **Integration with Glue Catalog**: Access to more data sources including Amazon S3, Redshift, RDS, etc.
- **Handling Mixed Data Types**: Uses choice or union types to manage fields with mixed data types.
- **Resolving Data Inconsistencies**: Convert a column to a single data type or keep all data types as separate columns.
- **Conversion to Spark DataFrame**: Easily convert between Glue Dynamic Frame and Apache Spark DataFrame.

## Bookmarks in Glue
- **Usage**: Track data processed in previous ETL job runs.
- **Avoid Reprocessing**: Only process new data in scheduled job runs.
- **Strategies**: Different methods to identify new data based on the data source.

## Types of Jobs in Glue
1. **Spark Jobs**: Batch data processing.
2. **Streaming ETL Jobs**: Continuous processing of streaming data.
3. **Python Shell Jobs**: Run Python scripts without Apache Spark.
4. **Radio Jobs**: New capability for machine learning workflows.

## Summary
- **DataFrames**: Used for small/medium datasets on a single machine.
- **Apache Spark**: For large-scale data processing.
- **Glue Dynamic Frame**: Optimized for ETL workflows with additional features for AWS integrations.
- **Bookmarks**: For incremental processing of new data.
- **Job Types in Glue**: Cater to different data processing needs including machine learning workflows.
- **Usage**: Dynamic Frame for AWS integrations; Spark DataFrame for data processing and transformation.

# 199. Lab - Glue ETL - Convert format to Parquet

# 200. Lab - Query Amazon Customer Reviews with Athena

# 201. Lab – Sentiment of the Customer Review

# 202. Lab - Query Sentiment of Customer Reviews using Athena

# 203. Lambda UI Changes

In the next lab, when creating a lambda function, the console now shows a "Deploy" button instead of "save".

After you create the function, click on Deploy to save the code and then test.

Thank you Dan for finding a solution and thank you Craig for reporting this issue.

# 204. Lab – Serverless Customer Review Solution Part 1

## Objective
- Develop a serverless solution for processing customer reviews, analyzing sentiment, and storing results in S3.

## Components
- **Python Client**: Generates streaming data (customer reviews).
- **Kinesis Firehose**: Ingests streaming data.
- **Lambda Function**: Processes reviews and adds sentiment analysis.
- **S3 Data Lake**: Stores transformed data.
- **Glue and Athena**: Queries data near real-time.
- **Comprehend**: Analyzes sentiment (approx. $1/MB).

## Setting Up Lambda Function
1. **IAM Role Setup**:
   - Create a role with Comprehend read-only and Lambda basic execution policies.
   - Role name: `lambda_comprehend_invoke`.
2. **Implement Lambda Function**:
   - Use AWS Management Console to create the function.
   - Use AWS-provided `kinesis-firehose-process-record-python` template.
   - Function Name: `product_review_sentiment`.
   - Role: `lambda_comprehend_invoke`.
   - Modify provided code with custom transformation logic.
   - Ensure base64 decoding and newline characters for Athena compatibility.

## Testing Lambda Function
1. **Create Test Event**:
   - Use Base64 encoded JSON payload with a customer review.
   - Test Event Name: `product_review_testevent`.
   - Check for sentiment in the response.
2. **CloudWatch Logs**:
   - Monitor execution errors and print statements in CloudWatch Logs.
   - Configure timeout to at least 60 seconds as recommended for Kinesis Firehose integration.

## Summary
- Configured a Lambda function to process customer reviews and add sentiment.
- Prepared for integrating with Kinesis Firehose to complete the sentiment analysis pipeline.
- Next Steps: Create a Kinesis Firehose data stream to test the end-to-end solution.

# 205. Lab – Serverless Customer Review Solution Part 2

## Objective
- Develop a solution for ingesting, transforming, and delivering customer reviews to S3, with querying capabilities using Athena.

## Components
- **Firehose Stream**: Accepts and processes customer reviews.
- **Lambda Function**: Adds sentiment data to reviews.
- **S3**: Destination for processed data.
- **Glue and Athena**: For querying the processed data.

## Creating Firehose Stream
1. **Firehose Configuration**:
   - Name: `customer_review_stream`.
   - Source: Direct PUT.
   - Transformation: Enabled using the `product_review_sentiment` Lambda function.
   - Format Conversion: Disabled.
   - Destination: S3 bucket (e.g., `aws-glue-cl`).
   - S3 Prefix: `product_review_fh/`.

2. **Buffering Criteria**:
   - Configured to process records in batches (e.g., 3 MB or 60 seconds).

3. **IAM Role for Firehose**:
   - Automatically generated based on configuration.

## Testing with Notebook Client
1. **Setup**:
   - Start SageMaker notebook instance.
   - Attach Amazon Kinesis Firehose Full Access policy to the notebook's IAM role.

2. **Executing Notebook**:
   - Download and preprocess Amazon reviews dataset.
   - Establish a session and acquire a Firehose client.
   - Send a sample of reviews (e.g., first 10) to the Firehose stream.

3. **Firehose Processing**:
   - Buffers records before invoking Lambda for transformation.
   - Waits for 5 minutes before delivering to S3.
   - Monitor via CloudWatch metrics.

4. **S3 Data Check**:
   - Data partitioned by year, month, day, and hour in the `product_review_fh` folder.

5. **Post-lab Cleanup**:
   - Delete the Firehose stream to avoid unnecessary charges.
   - Stop the notebook instance.

## Summary
- Constructed a serverless solution for handling customer reviews.
- Utilized Firehose for data ingestion, Lambda for data transformation, and S3 for data storage.
- Demonstrated the ability to query data using Athena, showcasing the efficiency of AWS's S3-based data lake architecture.
