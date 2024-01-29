# Domain 2: Security and Compliance

## Task Statement 2.1: Understand the AWS Shared Responsibility Model
- Focus on differentiating security responsibilities between AWS and the customer.
- Recognize when and to what extent customers need to secure AWS resources.

## Task Statement 2.2: Understand AWS Cloud Security, Governance, and Compliance Concepts
- Emphasis on understanding the key concepts of security, governance, and compliance in AWS.

## Task Statement 2.3: Identify AWS Access Management Capabilities
- Focus on customer's responsibility for access management in AWS.
- Understanding the tools and mechanisms for managing access to AWS environments.

## Task Statement 2.4: Identify Components and Resources for Security
- Knowledge of various security features available in AWS.
- Understanding customer's role in enabling and managing these security features.

## Course Structure
- Series of videos, each addressing individual task statements.
- Aim to prepare for examination on AWS security and compliance concepts.

## Upcoming Topics
- Detailed exploration of the AWS Shared Responsibility Model.
- Examination of security features within AWS and customer's role in their activation.
- Analysis of access management and security best practices in AWS.

# Task Statement 2.1: Understand the AWS Shared Responsibility Model

## Overview of the AWS Shared Responsibility Model
- Delineates responsibilities of AWS and the customer regarding system security.
- AWS: Responsible for security of the cloud.
- Customer: Responsible for security in the cloud (data, applications, etc.).

## AWS Responsibilities
- Management of global infrastructure: Regions, Availability Zones, edge locations.
- Security and management of underlying hardware, network, compute, storage, databases.
- Software required to run and manage these services.

## Customer Responsibilities
- Management of operating system and upwards:
  - Client-side data encryption, integrity, authentication.
  - Server-side encryption, network traffic protection (e.g., SSL certificates).
  - Operating system, network, and firewall configurations.
  - Application security and identity access management.
  - Security and backup of customer data.

## Variability of Responsibilities Based on Services
- Customers' security responsibilities vary depending on whether the service is managed or unmanaged.
- **Managed Services (e.g., Amazon RDS)**: AWS handles more security and management tasks.
- **Unmanaged Services (e.g., Amazon EC2)**: Customers have more control and hence more security responsibilities.

## Specific Service Responsibility Examples
- **Amazon RDS**: AWS responsible for database engine patching.
- **Amazon EC2**: Customer responsible for patching.

## Exam Focus
- Differentiating responsibilities between AWS and the customer for various services.
- Understanding how responsibilities shift with managed vs. unmanaged services.

## Next Steps
- Proceed to Task Statement 2.2: Cloud Security, Governance, and Compliance.

# Task Statement 2.2: Understand AWS Cloud Security, Governance, and Compliance Concepts

## Compliance on AWS
- Importance of considering security and compliance in AWS designs.
- Awareness of AWS compliance programs and where to find compliance information.
- AWS Artifact: On-demand access to AWS security and compliance documents.

## Compliance Variability Across Services
- Compliance requirements vary from service to service.
- Understanding where to find compliance information, not memorization of compliance details for each service.

## Security Measures on AWS
- Protecting systems and information as the primary goal.
- Additional security options beyond security groups and NACLs:
  - AWS WAF: Web application firewall.
  - Amazon GuardDuty: Threat detection service.
  - AWS Shield: DDoS protection.

## Encryption Fundamentals
- Differentiating between data encryption in transit and at rest.
- Understanding responsibility for enabling encryption per service.

## Logging, Auditing, and Reporting
- Importance of logs for troubleshooting and auditing AWS account activity.
- Key services:
  - Amazon CloudWatch: Monitoring and operational data collection.
  - AWS CloudTrail: Logging AWS resource creation and management.
  - AWS Config: Inventory and configuration auditing.

## Specific Use Case: Identifying User Actions
- AWS CloudTrail for auditing actions like EC2 instance deletion.
- AWS Audit Manager for broader audit management.

## Least Privilege Access
- Following the principle of least privilege for AWS account access.

## Next Steps
- Proceed to Task Statement 2.3: Access Management in AWS.

# Task Statement 2.3: Identify AWS Access Management Capabilities

## User and Identity Management
- Importance of user access control in AWS.
- Principle of least privilege: Granting minimal necessary access.
- AWS IAM (Identity and Access Management) for user and access management.

## AWS Account Fundamentals
- AWS accounts as the basis for provisioning services and logging usage.
- Importance of securing the AWS account root user.
- Recommendations for root user protection: multi-factor authentication, secure credential storage, access key rotation.

## Root User Management
- Understanding tasks requiring root user access.
- Differentiating between root user and other user types in terms of access and permissions.
- Best practices for root user security.

## IAM Features
- IAM Users: Username/password, access keys, MFA, password policies.
- IAM Groups: Organizing users and managing group-level permissions.
- IAM Roles: Temporary credentials for various use cases (e.g., cross-account access, AWS service permissions).

## Amazon Cognito
- Amazon Cognito Identity Pool for temporary AWS credentials.
- Use of Amazon Cognito for authenticated and unauthenticated users.

## IAM Policies
- Managed Policies: Created and managed by AWS.
- Regular IAM Policies: Created and managed by customers.
- IAM Policy Simulator for policy testing and troubleshooting.

## S3 Security
- Bucket Policies vs. IAM User Policies for Amazon S3 access control.
- Resource-based vs. identity-based policies.
- MFA Delete for enhanced S3 object protection.

## Next Steps
- Proceed to Task Statement 2.4: Components and Resources for Security in AWS.

# Task Statement 2.4: Identify Components and Resources for Security Support

## Network Security in AWS
- Basic functionality of AWS security services: Security Groups, Network ACLs, AWS WAF.
- Understanding use cases and differences between these services.

### Network Access Control Lists (NACLs)
- Function as a firewall at the subnet level in an Amazon VPC.
- Stateless: Separate rules for inbound and outbound traffic.

### Security Groups
- Operate at the resource level (e.g., EC2, RDS).
- Stateful: Inbound traffic automatically allows corresponding outbound traffic.
- Implicit deny for unspecified traffic.
- Can recognize AWS resources and security group IDs.

### AWS WAF
- Web application firewall to filter web traffic based on specific conditions.
- Use cases: Blocking SQL injections, cross-site scripting attacks.

## Security Assessments and Penetration Testing
- Permission to conduct security assessments for certain AWS services.
- Awareness of AWS services like AWS Trusted Advisor and Amazon Inspector for security recommendations.

## Third-Party Software and Tools
- AWS Marketplace for deploying third-party software in AWS accounts.
- Differentiating AWS services from third-party solutions.

## Research and Information Resources
- AWS Knowledge Center and Security Center for specific queries.
- AWS Security Blogs and Forums for community-driven insights.
- AWS documentation and whitepapers for best practices and detailed information.

## Next Steps
- Proceed to third walkthrough question on cloud security and compliance.

# Walkthrough Question 3: AWS Shared Responsibility Model

## Question Analysis
- **Topic**: AWS Shared Responsibility Model.
- **Keywords**: Shared responsibility model, customer responsibility.

## Question
- "Which task is the responsibility of the customer according to the AWS shared responsibility model?"

## Options Analysis
- **Option A: Install patches on an Amazon RDS database instance**
  - Incorrect. AWS manages Amazon RDS engine patches.
- **Option B: Patch the operating system of Amazon RDS database instances**
  - Incorrect. AWS is responsible for the operating system patches in Amazon RDS.
- **Option C: Determine which services have access to an Amazon DynamoDB table**
  - Correct. Customer determines access permissions for services within the cloud.
- **Option D: Patch the Amazon VPC network devices**
  - Incorrect. AWS manages and patches network devices in AWS infrastructure.

## Correct Answer
- **Option C: Determine which services have access to an Amazon DynamoDB table**
  - Aligns with customer's responsibility for managing access permissions within their AWS environment.

## Takeaways
- Understanding of customer-specific responsibilities in the AWS Shared Responsibility Model.
- Recognition of the division of responsibilities between AWS and its customers.
- Identification of knowledge gaps for further study, particularly in AWS service management responsibilities.

# Walkthrough Question 4: AWS Access Management Capabilities

## Question Analysis
- **Topic**: Access management for AWS services.
- **Keywords**: EC2 instance, private S3 bucket, access requirement.

## Question
- "A company has an application server that runs on an Amazon EC2 instance. The application server needs to access contents within a private Amazon S3 bucket. What is the recommended approach to meet this requirement?"

## Options Analysis
- **Option A: Create an IAM Role and Associate with EC2 Instance**
  - Correct. IAM roles provide temporary, secure access to AWS resources.
- **Option B: Configure a VPC Peering Connection**
  - Incorrect. VPC peering is for networking between VPCs, not for S3 bucket access.
- **Option C: Create a Shared Access Key**
  - Incorrect. Using shared keys reduces security and isn't a recommended practice.
- **Option D: Configure Application to Read Access Key**
  - Incorrect. Embedding long-term access keys is not secure compared to using IAM roles.

## Correct Answer
- **Option A: Create an IAM Role and Associate with EC2 Instance**
  - Provides a secure, recommended method for granting EC2 instances access to S3 resources.

## Takeaways
- Understanding of IAM roles as a secure way to manage access to AWS resources.
- Recognition of best practices in AWS access management and security.
- Identification of knowledge gaps for further study, particularly in AWS identity and access management.
