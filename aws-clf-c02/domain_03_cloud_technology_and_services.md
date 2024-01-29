# Domain 3: Cloud Technology and Services

## Task Statement 3.1: Define Methods of Deploying and Operating in the AWS Cloud
- Focus on deployment models and connectivity options in AWS.
- Exploration of different methods for deploying applications and services.

## Task Statement 3.2: Define the AWS Global Infrastructure
- In-depth look at AWS infrastructure components: Availability Zones, Regions, and Edge Locations.
- Understanding the significance of each component in AWS's global network.

## Task Statement 3.3: Identify AWS Compute Services
- Examination of various AWS compute services and their use cases.
- Differentiation between compute options and when to use them.

## Task Statement 3.4: Identify AWS Database Services
- Overview of AWS database services and their functionalities.
- Criteria for choosing a database service over running databases on EC2 instances.

## Task Statement 3.5: Identify AWS Network Services
- Insight into AWS network services, including their features and applications.

## Task Statement 3.6: Identify AWS Storage Services
- Detailed analysis of AWS storage options and their appropriate use cases.

## Task Statement 3.7: Identify AWS Artificial Intelligence, Machine Learning, and Analytics Services
- Exploration of AWS services in AI, machine learning, and analytics.
- Understanding their practical applications and benefits.

## Task Statement 3.8: Identify Other In-Scope AWS Service Categories
- Coverage of additional AWS services relevant to the exam.
- Understanding how these services integrate into broader AWS solutions.

## Course Structure
- Series of videos addressing each task statement.
- Aim to prepare for examination on in-depth AWS services and technology.

## Upcoming Topics
- Detailed exploration of AWS service categories: Compute, Storage, Networking, Database, AI/ML, Analytics.
- Discussion on service selection based on specific requirements and use cases.
- Analysis of subcategories within major AWS service categories.

# Task Statement 3.1: Define Methods of Deploying and Operating in the AWS Cloud

## Deployment and Operational Methods
- Various methods to communicate with AWS: APIs, SDKs, CLI, AWS Management Console, Infrastructure as Code.
- Understanding the strengths and limitations of each method.

## Cloud Deployment Models
- Distinction between cloud-native, hybrid, and on-premises deployments.
- Considerations for choosing different deployment types.

### Public Cloud
- Environment available to the public, meeting cloud computing criteria.
- Example: AWS, Azure, Google Cloud.

### Multi-Cloud Environments
- Utilizing more than one public cloud service.
- Combining services from different cloud providers.

### Private Cloud
- Dedicated services on-premises meeting cloud computing criteria.
- Example: AWS Outposts for private cloud services.

### Hybrid Cloud
- Combination of public and private cloud services.
- Understanding the distinction from hybrid environments (public cloud + on-premises data center).

## AWS Service Types: Public vs. Private
- Public services: Accessible from anywhere with internet connection (e.g., Amazon S3).
- Private services: Isolated within AWS private zone, no direct internet connection (e.g., Amazon VPC, EC2 instances).

## Connectivity Options
- Options: Virtual Private Network (VPN), AWS Direct Connect, public internet.
- Understanding advantages, limitations, and use cases for each connectivity type.
- Key concepts: Internet Gateway for public subnet connectivity, NAT Gateway for private subnet internet access.

## Practical Application
- Envisioning real-world applications and interactions of AWS components.
- Comprehending how different services and tools integrate within the AWS ecosystem.

## Next Steps
- Proceed to Task Statement 3.2: Dive Deeper into the AWS Global Infrastructure.

# Task Statement 3.2: Define the AWS Global Infrastructure

## Understanding AWS Global Infrastructure
- Importance of AWS global infrastructure in designing, deploying, and operating architectures.
- Components: Availability Zones, Regions, Edge Locations.

### Globally Resilient Services
- Services operating globally, replicating data across AWS Regions.
- Examples: IAM, CloudFront, Amazon Route 53.

### Regionally Resilient Services
- Operating within a single Region, replicating data across multiple Availability Zones.
- Examples: Amazon EFS, AWS Batch.

### Availability Zone Resilient Services
- Services run in a single Availability Zone.
- Example: Amazon EBS.

### Zonal Services
- Tied to a particular Availability Zone.
- Example: Amazon EC2.

## AWS Regions
- Geographical areas consisting of two or more Availability Zones.
- Data residency and compliance considerations for selecting Regions.
- Local Zones and AWS Wavelength for proximity to users.

## Availability Zones
- One or more data centers in separate facilities within a Region.
- Importance in building high availability and fault tolerance.
- Considerations for cross-AZ communication and failure points.

## Edge Locations
- Endpoints for AWS used for caching content.
- Services leveraging edge locations: CloudFront, AWS Global Accelerator.
- Benefits: Low latency, closer proximity to end-users.

### CloudFront vs. Global Accelerator
- CloudFront: Content caching, static and dynamic content delivery.
- Global Accelerator: Improves application performance over TCP/UDP, proxies packets from edge locations.

## Cloud Computing Models
- Infrastructure as a Service (IaaS), Platform as a Service (PaaS), Software as a Service (SaaS).
- Additional models: Database as a Service (DBaaS) and more.

## Exam Focus
- Understanding the significance of Regions, Availability Zones, and Edge Locations.
- Applications of these components in disaster recovery, business continuity, and compliance.
- Service-specific considerations related to global infrastructure components.

## Next Steps
- Proceed to Task Statement 3.3: Discuss AWS Compute Services.

# Task Statement 3.3: Identify AWS Compute Resources

## Amazon EC2 (Elastic Compute Cloud)
- Virtualization as a service, an example of Infrastructure as a Service (IaaS).
- Key Concepts:
  - Virtualization: Running multiple OS on a server.
  - EC2 Instances: Virtual machines running on EC2 hosts (physical servers).
  - EC2 Hosts: Either shared or dedicated.
  - Instance Store: Temporary storage on EC2 hosts.
  - Elastic Block Store (EBS): Persistent storage volumes for EC2 instances.

### EC2 Instance Types
- Categories: General Purpose, Compute Optimized, Memory Optimized, Accelerated Computing, Storage Optimized.
- Burstable instances for variable workloads.
- Selection based on workload requirements (CPU, memory, storage, network bandwidth).

### Amazon Machine Images (AMIs)
- Custom AMIs for specific configurations.
- Golden AMIs: Pre-configured with security patches, software, monitoring agents.

### EC2 Instance Metadata
- Accessing instance details like ID, public keys, IP addresses.
- Accessed via `http://169.254.169.254/latest/meta-data`.

## Container Services
- AWS Elastic Container Service (ECS): Managed container orchestration service.
- AWS Kubernetes Service (EKS): Managed Kubernetes service.

## AWS Lambda
- Function as a Service (FaaS) product.
- Event-driven, serverless computing.

## High Availability and Scalability
- Auto Scaling: Automatic EC2 instance scaling.
- Elastic Load Balancers (ELB): Distribution of incoming traffic across multiple instances.
- Types of Load Balancers: Classic, Application, Network, Gateway.

## Exam Focus
- Understanding different EC2 instance types and their use cases.
- Utilizing container services for specific requirements.
- Employing AWS Lambda for serverless computing.
- Integrating auto scaling and load balancing for enhanced availability and scalability.

## Next Steps
- Proceed to Task Statement 3.4: Discuss AWS Database Services.

# Task Statement 3.4: Identify AWS Database Resources

## Amazon RDS (Relational Database Service)
- Managed relational database instances.
- Supports MySQL, MariaDB, PostgreSQL, Oracle, Microsoft SQL Server, Amazon Aurora.
- Multi-AZ configurations for high availability.

### RDS Read Replicas
- Asynchronous replication for read operations and availability.
- Use cases: Performance improvements, query offloading.

## Amazon Aurora
- Cluster architecture compatible with MySQL and PostgreSQL.
- Features: Cluster volume storage, Aurora Serverless, Global Databases.
- Serverless clusters scale based on Aurora Capacity Units (ACUs).

## Amazon DynamoDB
- NoSQL Database as a Service.
- Options: Provisioned capacity or on-demand mode.
- Global tables for global resilience.

## In-Memory Databases: Amazon ElastiCache and DAX
- ElastiCache: Managed caching service with Redis and memcacheD support.
- DAX: In-memory cache specifically for DynamoDB.

## Amazon Redshift
- Petabyte-scale data warehousing solution.
- Column-based storage for OLAP (Online Analytical Processing).
- Cluster architecture, integration with S3, Kinesis, DMS.

## Database Migration Tools
- AWS Snow Family: Snowcone, Snowball, Snowmobile for large data migrations.
- AWS Database Migration Service (DMS): Data migration and schema conversion.
- AWS Schema Conversion Tool: Transforms between different database engines.

## AWS DataSync
- Fast data transfer between on-premises storage and AWS storage services.
- Automates tasks like copy jobs, transfer scheduling, data validation.

## Exam Focus
- Differentiating AWS database services for specific scenarios.
- Comparing managed services with self-managed databases on EC2.
- Understanding features, customization options, and use cases of each database service.

## Next Steps
- Proceed to Task Statement 3.5: Discuss AWS Network Services.

# Task Statement 3.5: Identify AWS Network Resources

## Amazon Virtual Private Cloud (VPC)
- Creates a logically isolated section of AWS.
- Control over virtual networking environment: IP address ranges, subnets, route tables, network gateways.
- Types of VPCs: Default and Custom.

### Subnets and Route Tables
- Dividing a VPC into subnets for high availability across Availability Zones.
- Route tables control traffic routing between subnets.

### Internet Gateways
- Connects VPC to the internet and AWS public zone.
- Allows traffic from VPC to access the internet.

### Network Access Control Lists (NACLs)
- Firewall at the subnet level.
- Stateless: Separate rules for inbound and outbound traffic.

### Security Groups
- Acts as a firewall for EC2 instances.
- Stateful: Inbound traffic automatically allows corresponding outbound traffic.

### Network Address Translation (NAT)
- Provides private resources outgoing access to the internet.
- NAT Gateways for enabling internet access to private subnets.

## VPC Peering and Endpoints
- VPC peering: Direct communication between VPCs.
- Gateway Endpoints: Connect VPC to AWS public services (S3, DynamoDB).
- Interface Endpoints: For other AWS services using DNS.

### AWS PrivateLink
- Connects VPC to services in other VPCs without VPC peering or gateways.

## AWS VPN and Direct Connect
- VPN: Encrypted connection over the internet between VPC and on-premises network.
- Direct Connect: Dedicated physical connection between on-premises and AWS.

## Amazon Route 53
- Managed DNS service.
- Domain registration and DNS hosting.
- Globally resilient service.

### Routing Policies
- Failover, Weighted, Latency routing policies for high availability.

## AWS Edge Services: CloudFront and Global Accelerator
- CloudFront: Content delivery network (CDN) for caching content.
- Global Accelerator: Improves application performance over TCP/UDP.

## Exam Focus
- Utilizing VPC features for privacy and security.
- Connectivity options: VPN, Direct Connect, Route 53.
- Choosing appropriate network services for different scenarios.

## Next Steps
- Proceed to Task Statement 3.6: Discuss AWS Storage Services.

# Task Statement 3.6: Identify AWS Storage Resources

## Cloud Storage Fundamentals
- Cloud storage model: Data stored via cloud computing provider.
- Benefits: On-demand capacity, performance, retention, and cost-effectiveness.
- Requirements: Durability, availability, security.

## Types of Cloud Storage
- Object storage: Amazon S3.
- File storage: Amazon EFS, Amazon FSx.
- Block storage: Amazon EBS.

### Amazon S3 (Simple Storage Service)
- Globally resilient object storage platform.
- Features: Buckets, objects, versioning, lifecycle policies.
- Storage classes: Varying costs, performance, retrieval speeds.
- Compliance considerations based on data residency and regional laws.

### Amazon EFS (Elastic File System)
- Network-based file system for Linux instances.
- Scalable and self-healing properties.
- Hybrid methods compatibility: VPN, Direct Connect, VPC Peering.

### Amazon FSx
- Windows file system share drive, supports SMB protocol.
- Active directory integration, ACLs, SSD-based storage.

### Amazon EBS (Elastic Block Store)
- Provides block-level storage for EC2 instances.
- Volume types: General Purpose SSD, Provisioned IOPS SSD, Throughput Optimized HDD, Cold HDD.
- Snapshot backups, Instance Store vs. EBS (ephemeral vs. persistent storage).

## AWS Storage Gateway
- Connects on-premises storage with AWS services.
- Types: File Gateway, Volume Gateway (Stored and Cached), Virtual Tape Library Gateway.
- Use cases: File sharing, data archiving, disaster recovery.

### Backup and Recovery Solutions
- Amazon S3 for backups: Lifecycle policies, Glacier, Glacier Deep Archive.
- AWS Backup: Centralized data protection across AWS services and on-premises.

## Exam Focus
- Understanding AWS storage service features, functionality, and use cases.
- Comparing services: S3, EFS, FSx, EBS, and Storage Gateway.
- Exploring how storage services fit into broader AWS solutions.

## Next Steps
- Proceed to Task Statement 3.7: Discuss AWS AI, Machine Learning, and Analytics Services.

# Task Statement 3.7: Identify AWS AI, ML and Analytics Services Resources

## Artificial Intelligence (AI) and Machine Learning (ML) Fundamentals
- Machine Learning: Developing algorithms for task execution without explicit instructions, based on patterns and inference.
- Artificial Intelligence: Solving cognitive problems associated with human intelligence, such as learning, problem solving, and pattern recognition.

## AWS AI and ML Services
### AI Services
- Fully managed services using API calls.
- Capabilities: Computer vision, speech, natural language, chatbots, predictions, and recommendations.
- Examples: Amazon Translate, Amazon Polly, Amazon Lex, Amazon Rekognition.

### ML Services
- Managed services for machine learning.
- Focus: Amazon SageMaker for building, training, and deploying machine learning models.
- New service: Amazon CodeWhisperer for code generation and security scanning.

### ML Frameworks and Infrastructure
- Open-source frameworks: TensorFlow, PyTorch, Apache MXNet.
- Deep Learning AMI and Containers: Pre-installed ML frameworks, optimized for performance.
- Compute infrastructure: Amazon EC2 P3 and P3dn instances.

## AWS Analytics Services
### Amazon Athena
- Interactive query service for data in Amazon S3.
- Serverless, pay-per-query model.
- Supports various data formats.

### Amazon Macie
- Security service using ML to protect sensitive data in Amazon S3.
- Focus: Personally Identifiable Information (PII) detection and protection.

### Amazon Redshift
- Petabyte-scale data warehousing solution.
- Column-based database for analytical workloads.
- Integration with S3, DynamoDB, Database Migration Service, Kinesis.

### Amazon Kinesis
- Real-time data processing and analysis at scale.
- Ingests data streams like video, audio, application logs, clickstreams.
- Supports analytics, machine learning, and other applications.

### AWS Glue
- Serverless data integration service.
- Enables discovery, preparation, and integration of data sources.
- Supports ETL pipelines for data lakes and analytics.

### Amazon QuickSight
- Business intelligence service for interactive dashboards.
- Integrates machine learning insights.
- Fully managed, supports data analysis and visualization.

## AWS Services for Data Transformation and Analytics
- Amazon Elastic MapReduce (EMR): Web service for big data processing using Apache Hadoop and Amazon EC2/S3.
- Supports various big data use cases and analytics tools like Apache Spark.

## Exam Focus
- Understanding the range and capabilities of AWS AI, ML, and analytics services.
- Differentiating between AI services and ML services.
- Recognizing suitable AWS services for specific AI/ML/analytics scenarios.

## Next Steps
- Proceed to Task Statement 3.8: Discuss Other In-Scope AWS Services for the Exam.

# Task Statement 3.8: Identify Services from other in-scope AWS Service Categories

## AWS Monitoring and Observability Services
- Importance: Essential for continual improvement of designs.
- Key Services:
  - Amazon CloudWatch: Monitor applications and infrastructure.
  - AWS X-Ray: Observe and debug distributed systems.
  - Amazon EventBridge: Respond to environment changes in near real-time.

## AWS Application Integration Services
- Suite of services for communication between decoupled components.
- Key Services:
  - Amazon EventBridge: Serverless event bus for application integration.
  - Amazon Simple Notification Service (SNS): Pub/sub messaging service.
  - Amazon Simple Queue Service (SQS): Managed message queue service.
  - Load Balancing: Decouple and scale workloads.

## AWS Business Application Services
- Enhance agility and reduce costs.
- Key Services:
  - Amazon Connect: Cloud-based contact center.
  - Amazon Simple Email Service (SES): Email sending service.

## AWS Customer Engagement Services
- Tools for customer lifecycle management.
- Key Services:
  - AWS Activate for Startups, AWS IQ, AWS Managed Services, AWS Support.

## AWS Developer Services
- Facilitate DevOps practices and efficient deployments.
- Key Services:
  - AWS CodeBuild, CodeCommit, CodeDeploy, CodePipeline, CodeStar, Cloud9, CloudShell, CodeArtifact, AppConfig, X-Ray.

## AWS End-User Computing Services
- Secure access to applications and desktops.
- Key Services:
  - Amazon AppStream 2.0: Application streaming service.
  - Amazon WorkSpaces: Managed virtual desktops.
  - Amazon WorkSpaces Web: Browser-based access to internal websites.

## AWS Front-End Web and Mobile Services
- Support for building and hosting full-stack applications.
- Key Services:
  - AWS Amplify: Full-stack development toolset.
  - AWS AppSync: GraphQL interface for app developers.

## AWS IoT Services
- Securely connect, manage, and analyze IoT device data.
- Key Services:
  - AWS IoT Core: Connect and manage IoT devices.
  - AWS IoT Greengrass: Extend cloud capabilities to local devices.

## Exam Preparation
- Focus on choosing appropriate AWS services for specific requirements and use cases.
- Understand support options available for different business needs.

## Next Steps
- Proceed to Walkthrough Question 5 for applied learning of these concepts.

# Walkthrough Question 5: AWS Deployment and Operation Methods

## Question Overview
- **Context**: Company requires a dedicated private connection to AWS from on-premises.
- **Keywords**: "Dedicated private connection".

## Answer Options Analysis
- **Option A: AWS VPN**
  - **Analysis**: Provides secure connections but not dedicated.
  - **Verdict**: Incorrect.

- **Option B: AWS PrivateLink**
  - **Analysis**: Used for secure VPC-to-VPC services within AWS, not for on-premises to AWS.
  - **Verdict**: Incorrect.

- **Option C: VPC endpoint**
  - **Analysis**: Enables private connections between VPC and AWS services, not on-premises to AWS.
  - **Verdict**: Incorrect.

- **Option D: AWS Direct Connect**
  - **Analysis**: Provides a dedicated private connection from on-premises to AWS.
  - **Keyword Match**: "Dedicated private connection".
  - **Verdict**: Correct.

## Correct Answer
- **Option D: AWS Direct Connect**
  - **Reasoning**: Direct Connect is designed specifically for dedicated private connections from on-premises to AWS, aligning perfectly with the requirement described in the question.

## Knowledge Gaps and Further Learning
- Understanding the distinction between AWS connectivity options:
  - **VPN vs. Direct Connect**: Recognize scenarios where a dedicated connection (Direct Connect) is preferable over a VPN.
  - **PrivateLink and VPC Endpoints**: Their usage within AWS environment, not for on-premises connections.

## Next Steps
- Proceed to Walkthrough Question 6 for continued practice and learning.

# Walkthrough Question 6: AWS Global Infrastructure

## Question Overview
- **Context**: Identifying which aspect of AWS infrastructure enables global deployment of compute and storage.
- **Keywords**: "Global deployment", "Compute", "Storage".

## Answer Options Analysis
- **Option A: Multiple Availability Zones in an AWS Region**
  - **Analysis**: Provides high availability within a single Region, not globally.
  - **Verdict**: Incorrect.

- **Option B: Multiple AWS Regions**
  - **Analysis**: Offers global deployment capabilities across different geographical areas.
  - **Keyword Match**: "Global deployment".
  - **Verdict**: Correct.

- **Option C: Tags**
  - **Analysis**: Used for organizing and managing resources, not for deployment.
  - **Verdict**: Incorrect.

- **Option D: Resource Groups**
  - **Analysis**: Helps in managing groups of resources, not in deploying them globally.
  - **Verdict**: Incorrect.

## Correct Answer
- **Option B: Multiple AWS Regions**
  - **Reasoning**: Multiple Regions are the correct choice for deploying infrastructure globally, aligning with the requirement for global deployment of compute and storage.

## Knowledge Gaps and Further Learning
- Understanding AWS Global Infrastructure components:
  - **Regions vs. Availability Zones**: Recognize their roles in global and regional deployments.
  - **Tags and Resource Groups**: Their purpose in resource management, not deployment.

## Next Steps
- Proceed to Domain 4: Billing, Pricing, and Support for comprehensive understanding of AWS financial and support aspects.
