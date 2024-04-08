# Introduction and Housekeeping

## AWS ML Specialty Certification Exam Overview (Lesson 4)

### Exam Purpose
- Validates the ability to build, train, tune, and deploy ML models using AWS.
- Translates business problems into ML solutions with justifications.
- Identifies appropriate AWS services for implementing solutions.
- Designs and implements scalable, cost-optimized, reliable, and secure ML solutions.

### Candidate Profile
- 1-2 years of AWS experience developing ML solutions.
- Understanding of ML algorithms and hyperparameter optimization.
- Hands-on experience with ML frameworks like scikit-learn and TensorFlow.
- Knowledge of model training and deployment best practices.

### Exam Guide Highlights
- **Exam Resources**: AWS provides an exam guide and sample questions.
- **Question Format**: Multiple choice and multiple response questions.
- **Scoring**: Range between 100 to 1000 with a minimum passing score of 750.
- **Domains**: Data Engineering, Exploratory Data Analysis, Modeling, Implementation and Operations.
- **Section Level Feedback**: Given post-exam to indicate performance in each domain.

### Domains and Weights
- **Data Engineering**: Data repositories creation, data ingestion, and transformation.
- **Exploratory Data Analysis**: Cleaning and preparing data for modeling.
- **Feature Engineering**: Adding and creating relevant features.
- **Modeling**: Framing business problems as ML problems, selecting algorithms, training, and evaluating models.
- **Implementation and Operations**: Deploying solutions, ensuring availability, scaling, fault tolerance, security, and monitoring.

### Preparation Tips
- **Real Complexity**: Actual exam complexity may be underrepresented by listed resources.
- **AWS Knowledge**: Approximately 15% of questions focus on general AWS knowledge.
- **Machine Learning Concepts**: About 50-60% of questions test ML concepts that are not AWS-specific.
- **AWS ML Offerings**: Around 25-35% of questions pertain to AWS-specific ML services and best practices.
- **Sample Questions**: AWS provides a sample question PDF to identify strengths and improvement areas.

### Exam Format
- Duration: 170 minutes.
- Number of Questions: Approximately 65.
- Time Allocation: Roughly 2.5 minutes per question.

### Conclusion
- The exam is focused on developing professionals capable of solving business problems with ML on the AWS cloud.
- It assesses not just AWS-specific knowledge but also a deeper understanding of machine learning concepts and their practical application.

### References

- [AWS Certified Machine Learning - Specialty](https://aws.amazon.com/certification/certified-machine-learning-specialty/) (Look at the Exam Guide and Sample Questions!)

## AWS Machine Learning Specialty Exam Preparation (Lesson 6)

### For AWS Beginners
- **Course Requirement**: No prior AWS experience needed.
- **Follow Course**: Complete all lectures and labs in sequence.

### Starting Certification
- **Recommended First Step**: AWS Cloud Practitioner certification for AWS basics.

### Cost Benefits
- **Cost Savings**: Cloud Practitioner exam can lead to discounts on the ML Specialty exam.

### Machine Learning Knowledge
- **Framework Proficiency**: Get familiar with scikit-learn.
- **Reference Book**: "Introduction to Machine Learning with Python" by Andreas Müller.

### AWS Resources
- **Free Training**: Utilize AWS's "Machine Learning Basics" video and other free resources.

### Practice Exams
- **Course Practice Exam**: Take the full-length timed exam included in the course.
- **AWS Practice Exam**: Available for purchase or free with a voucher.

### Final Steps
- **Exam Registration**: Use any vouchers for discounts on the ML Specialty exam.
- **Final Review**: Address any gaps identified in practice exams.

## AWS Account Setup, Free Tier Offers, Billing, Support (Lesson 7)

### AWS Account Setup
- Sign up at [aws.amazon.com](https://aws.amazon.com).
- AWS provides hands-on experience with three types of free offers: always free, 12 months free, and trials.

### Free Tier Offers
- **12 Months Free**: Access to certain AWS services like EC2 (T2/T3 micro), 5GB S3 storage, and 750 hours/month of RDS.
- **Free Trials**: Short-term trials for services like Amazon SageMaker (2 months free).
- **Always Free**: Services like DynamoDB offer a perpetual free tier up to a certain limit.

### Post-Free Tier
- Usage exceeding free tier limits or post-expiration incurs standard rates.

### Root Account
- The initial account created is the root account, with the highest privileges.

### Billing and Charges
- AWS automatically charges the payment method based on monthly usage.
- Use the billing dashboard for a consolidated view of charges.
- View detailed statements for an itemized list of charges.
- Contact AWS support for billing inquiries or to dispute charges.

### AWS Support
- **Billing Support**: Available to all customers for billing-related queries.
- **Technical Support**: Requires enrollment in a paid plan. Free support is available for account and billing support.

### Service Quotas
- AWS imposes service quotas (formerly service limits) to prevent unexpected charges.
- Default quotas can be increased upon request if you hit a service limit error.

## Billing Alerts, Delegate Access (Lesson 8)

### Enabling Billing Dashboard Access
- Billing dashboard is initially only accessible by the root account.
- To delegate access, activate IAM user and role access to billing information in account settings.

### Setting Up Billing Alerts
- Navigate to **Billing Preferences**.
- Enable alerts for approaching free tier limits and for billing alerts.

### Creating a Billing Alarm with CloudWatch
- Use CloudWatch in the North Virginia region to set up billing alarms.
- Create an alarm for when estimated charges exceed a set threshold (e.g., $5).

### Email Notifications
- Set an action to email when the alarm triggers.
- Create a new topic in Simple Notification Service (SNS) and add email addresses for alerts.

### Using AWS Budgets for Tracking
- AWS Budgets can track actual charges and forecast trends.
- Set a monthly budget and receive alerts at specified thresholds (e.g., 50% of the budget).

## Instructions - Configure IAM Users, Setup CLI (Lesson 9)

### Step 1: IAM User Setup

1. **Root Login**: Use root credentials to log in.
2. **IAM Service**: Locate IAM Service in the AWS console.
3. **Account Alias**:
    - Create an Account Alias for easier user sign-in.
    - Note down the IAM Users sign-in URL.
4. **Root Account MFA**: Set up Multi-Factor Authentication for the root account.

### Step 2: Create `my_admin` User

1. **User Creation**:
    - Go to IAM Users.
    - Click `Add Users`.
    - User details:
        - Name: `my_admin`
        - Access type: Management Console
        - Password: Choose a custom password.
        - Uncheck "User must create a new password at next sign-in".
2. **Permissions**:
    - Attach the `AdministratorAccess` policy directly.
3. **Finalize**:
    - Create the user.
    - Securely save the sign-in credentials.

### Step 3: Sign-out of Root Account

- Log out from the root account.

### Step 4: Sign-in as `my_admin`

- Use the previously saved sign-in URL and credentials to log in as `my_admin`.

### Step 5: Setup `prediction_only` User Permissions

- **Create Policy for SageMaker**:
    - Navigate to IAM Policies.
    - Click `Create policy`.
    - Service: Choose SageMaker.
    - Permissions: Select "All read actions" under Read.
    - Resources: Select "All resources".
    - Name the policy `SageMakerInvokeEndpoint`.

### Step 6: Create `ml_user_predict`

1. **User Creation**:
    - In IAM, select `Users` then `Add users`.
    - User details:
        - Name: `ml_user_predict`.
2. **Attach Policies**:
    - Attach `SageMakerInvokeEndpoint`.
    - Attach `AmazonS3ReadOnlyAccess`.

### Step 7: Configure CLI for `ml_user_predict`

1. **Access Keys**:
    - In the `ml_user_predict` user details, go to the Security Credentials tab.
    - Create an access key under the Access keys section.
2. **CLI Configuration**:
    - Use the access key to configure the AWS CLI.
    - Follow video instructions [8:54 onwards] for CLI setup.
3. **Download Credentials**:
    - Download the `.csv` file containing the access key for the `ml_user_predict`.

## Benefits of Cloud Computing (Lesson 12)

1. **Cost Savings**: Cloud offers a pay-as-you-go model, eliminating upfront capital investment.

2. **Visibility and Control**: AWS provides tools like AWS Bills, Budgets, Cost Explorer, Cost and Usage Reports, and Cost Allocation Tags for monitoring and managing costs.

3. **Bulk Purchasing and Shared Infrastructure**: Cloud providers negotiate better terms due to bulk purchases and shared customer infrastructure, reducing costs.

4. **Capacity Flexibility**: The cloud allows for scaling resources based on actual demand, avoiding over or under capacity.

5. **Increased Speed and Agility**: Resources can be spun up in minutes, fostering rapid experimentation and innovation at a lower cost.

6. **Eliminate Data Center Operations**: Outsourcing infrastructure management to the cloud saves money and allows businesses to focus on differentiating activities.

7. **Global Reach**: AWS's global data center network enables businesses to deploy applications close to customers worldwide, quickly and efficiently.

## AWS Global Infrastructure Overview (Lesson 13)

### AWS Cloud Types
1. **Public Cloud**: Accessible at aws.amazon.com.
2. **US Gov Cloud**: For US entities meeting specific security and compliance standards.
3. **China Cloud**: Complies with China's legal and regulatory requirements.

### AWS Global Presence
- **Regions**: AWS has multiple isolated regions worldwide.
- **Benefits**:
  - Proximity to customers for faster response times.
  - Compliance with data locality laws in different countries.

### Data Storage and Transfer
- Data stored in the selected AWS region.
- Customer-initiated data replication across regions is possible.

### Availability Zones (AZs)
- Each region contains multiple AZs, each a collection of data centers.
- AZs are physically separate but interconnected for redundancy.
- Spreading applications across AZs enhances availability and protection.

### Region and AZ Failures
- AWS design ensures regional outages don't impact other regions.
- Example strategies:
  - S3 copies data across AZs.
  - Elastic Load Balancer distributes traffic among healthy web servers in different AZs.
  - RDS uses primary and standby servers in different AZs for databases.

### Multi-Region Deployment
- Companies like Netflix deploy in multiple regions for higher availability.

### Edge Locations
- Over 200 Edge locations support CloudFront for low-latency content delivery.

### AWS Outpost
- Brings AWS services to on-premises data centers for low latency and critical use cases.

### AWS Service Health Dashboard
- Provides global and personalized health status of AWS services and resources.

### Best Practice

- Deploy applications across multiple AZs for enhanced reliability.
