# AWS Certified Machine Learning Specialty (MLS-C01)

### Useful Starter Links

- [AWS Certified Machine Learning - Specialty](https://aws.amazon.com/certification/certified-machine-learning-specialty/?c=sec&sec=resources) : exam guide, sample questions

- [Machine Learning: Exam Preparation](https://aws.amazon.com/training/learning-paths/machine-learning/exam-preparation/)

- [AWS Training and Certification](https://www.aws.training)

- [AWS Skill Builder](https://www.amazon.com/gp/f.html?C=L6EVD0079TVR&M=urn:rtn:msg:202301151903416e3ad4f6ff0949a98951e3ba58e0p0na&R=36S58368GRRDW&T=C&U=https%3A%2F%2Fexplore.skillbuilder.aws%2Flearn&H=53I6ASQQWC3ZBZ0SJ1IYLWBVMFSA)

### AWS Whitepapers & Guides

- [AWS Whitepapers & Guides](https://aws.amazon.com/whitepapers/?whitepapers-main.sort-by=item.additionalFields.sortDate&whitepapers-main.sort-order=desc&awsf.whitepapers-content-type=*all&awsf.whitepapers-global-methodology=*all&awsf.whitepapers-tech-category=*all&awsf.whitepapers-industries=*all&awsf.whitepapers-business-category=*all)
- [Overview of Amazon Web Services](https://d0.awsstatic.com/whitepapers/aws-overview.pdf)
- [Architecting for the Cloud: AWS Best Practices](https://d1.awsstatic.com/whitepapers/AWS_Cloud_Best_Practices.pdf)
- [How AWS Pricing Works](https://d0.awsstatic.com/whitepapers/aws_pricing_overview.pdf)
- [Cost Management in the AWS Cloud](https://d1.awsstatic.com/whitepapers/aws-tco-2-cost-management.pdf)
- [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/)

### Other Links

- [Couse github page](https://github.com/ChandraLingam/AmazonSageMakerCourse)
- [Total Cost of Ownership](https://www.youtube.com/watch?v=aXMih9jQIec)

## 1.7 - AWS Account Setup

### Free Tier Offers, Billing, Support, Billing Alerts

#### Enable authorized users to access billing data

Account → IAM User and Role Access to Billing Information → Edit (on the right) → Activate IAM Access → Update

#### Enable billing alerts

Billing Dashboard → Billing Preferences → CHECK “Receive Free Tier Usage Alerts” AND “Receive Billing Alerts” → Save preferences

#### Set alarm to inform charges : Services → CloudWatch

To monitor billing data, make sure region is “N. Virginia”

- Go to Alarms → Billing → Create Alarm → Select Metric → Search for “Billing” then select “Total Estimated Charge” → Select Metric
- Set a threshold (5 USD) → Create Alarm

#### Create a budget : Services → Billing Console

Go to Budgets from left navigation pane → Create a budget

### Configure IAM Users, Setup CLI

#### Creating Users under your root account : Services → IAM

**IAM :** Identity Access Management

This is where we manage “access” and “authorization”

**Create admin user**

ml_user : Access Management → Users → Add Users → Next → Attach Policies Directly → AdministratorAccess

**Setup a custom policy**

Policies → Create Policy → search for sagemaker → Read Access → Resources : All resources → Name this as SageMakerInvokeEndPoint

ml_user_predict : give both SageMakerInvokeEndPoint and AmazonS3ReadOnlyAccess permissions

#### Setup CLI

**CLI Access for ml_user_predict**

`aws configure --profile ml_user_predict`

enter “Access key ID” and “Secret access key” for this user

region : us-east-1 (N. Virginia)

List S3 buckets in your account:

`aws s3 ls --profile ml_user_predict`

## 2.17 - S3 Bucket Setup

### Create a new S3 bucket

login with my_admin → Search “S3” → Create Bucket

Data needs to be in the same region where we train the model

Give a unique name : “mls-sagemaker” → Create Bucket

### Setup Sagemaker Notebook Instance

Search for “Sagemaker” from the AWS Management Console

From navigation pane → Notebook → Notebook Instances → “Create Notebook Instance”

Notebook Instance Type → ml.t3.medium (part of the sagemaker 2 month free tier)

Permissions and Encryption → IAM role → Create a new role

Finally create notebook

    💡 Don’t forget to stop this service when you are not using it

## 6.64 - Model Training Using Python SDK

Use `xgboost/xgboost_cloud_training_template.ipynb` for training & deploying of the model.

Use `xgboost/xgboost_cloud_prediction_template.ipynb` for testing the model.

**IntegrationExamples →** invoke_using_sagemaker_sdk.ipynb

## 7.77 - ResourceLimitExceeded Error - How to Increase Resource Limit

Some of the accounts are running into the `ResourceLimitExceeded` when creating a SageMaker Endpoint.

Here is an example of error:

```
1. ResourceLimitExceeded: An error occurred (ResourceLimitExceeded) when calling the CreateEndpoint operation: The account-level service limit 'ml.m4.xlarge for endpoint usage' is 0 Instances, with current utilization of 0 Instances and a request delta of 1 Instances. Please contact AWS support to request an increase for this limit.
```

You may have to submit a request to AWS support for increasing limits.

Here are the steps to open a support ticket to increase limit.

1. Login with your my_admin account
2. Under Support (right top corner), select Support Center
3. Create Case for Service Limit Increase and explain the issue.
4. For Service, specify **SageMaker service** limit increase, do submit a request for "**SageMaker Hosting**" and "**SageMaker Training**".

Specify appropriate **instance type and new limit.**

You can specify **5** as the new limit

## 7.79 - **Q&A: How does SageMaker built-in know the target variable?**

During training, the first column in the CSV file is the target variable

During inference, you need to provide only the features (i.e. target variable should not be provided)

[Here](https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost.html) is the relevant notes.

For CSV training, the algorithm assumes that the target variable is in the first column and that the CSV does not have a header record. For CSV inference, the algorithm assumes that CSV input does not have the label column. For libsvm training, the algorithm assumes that the label is in the first column. Subsequent columns contain the zero-based index value pairs for features. So each row has the format: `<label> <index0>:<value0> <index1>:<value1> ...` Inference requests for libsvm might not have labels in the libsvm format

## 7.82 - SageMaker Endpoint Features

- Cloudwatch
- Autoscaling
- Model hosting : Variants of Algorithms

## 7.83 - SageMaker Spot Instances - Save up to 90% for training jobs

**Spot Instances - Save up to 90% over on-demand instances for training**

Thanks to William Tsunomachi for posting the query on spot-instances in the course Q&A forum

https://www.udemy.com/course/aws-machine-learning-a-complete-guide-with-python/learn/#questions/13387612/

My response:

Great question! Instead of on-demand instances, you can opt for spot instances and save quite a bit of money

According to AWS, with massive growth in Cloud Compute, the unused capacity is pretty substantial, and as customers, we should take advantage of it.

AWS offers this unused capacity as spot-capacity at a steep discount (over 80% - actual discount varies slightly based on instance type and size). So, you can get a current instance type for a discount, or you can opt for a much bigger instance type (3-4 times larger)

One drawback with spot instances is that it can be terminated anytime by AWS with a two-minute notice. That’s because if there is more need for on-demand instances, AWS will terminate spot instances and make the capacity available for on-demand use (just one example, there are other scenarios where AWS may step-in and terminate spot).

In general, with a spot, you have a better chance of getting an instance when you are flexible about instance type and size.

The nice thing is SageMaker does handle spot-interruptions and can resume the training when capacity is available

Couple of things to note when using spot instances:

- You need to set the use_spot_instance flag to true in the estimator

- It is a good idea to configure checkpointing. With checkpointing, the model artifacts are periodically saved during the training process. So, your training state is saved when the spot instance is terminated. When the spot capacity becomes available, a new instance can resume training from where it was stopped earlier

- You also need to specify maximum wait time for training job – spot is not guaranteed. So, you can specify how long to wait before aborting the job. Max run time is configurable that tells how long the training job can run

- In the job output, training seconds tell you how long the job took. Billable seconds is the time you are billed for after applying spot discounts. For an on-demand instance, training seconds and billable seconds will almost be the same. For spot instance, you would see a much smaller number for billable seconds.

[Here](https://github.com/aws-samples/amazon-sagemaker-managed-spot-training/blob/main/xgboost_built_in_managed_spot_training_checkpointing/xgboost_built_in_managed_spot_training_checkpointing.ipynb) is a good example of using spot instances.

Also see [Use Managed Spot Training in Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html)

## Sections to Review

The following sections in the course are essential for the exam – please do review them

- Model Performance Evaluation
- SageMaker Service and SDK Changes
- Endpoint Changes with Zero Downtime
- Emerging AI Trends and Social Issues
- Model Optimization and HyperParameter Tuning
- Bring Your Own Algorithm
- Nuts and Bolts of Optimization
- SageMaker FAQ - https://aws.amazon.com/sagemaker/faqs/

## AWS Exam Readiness

### Official Practice Question Sets [FREE]

AWS official practice question sets are now FREE [earlier, we had to pay USD 20-40]. Do go through these questions and the exam readiness videos

- [Practice Question Set](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/9153/aws-certification-official-practice-question-sets-english)

-  [Exam Readiness](https://explore.skillbuilder.aws/learn/global-search/exam%20readiness)

## How to Access Discount Vouchers

### Exam Tip

*Consider going to a test center! You will get access to paper and a pencil. You can visualize the question and answer more accurately! I am confident this can help improve your score by 40 points (or more).*

If you like the convenience of taking the test from home! Go for it!

### How to Access Discount Vouchers

The 50% discount vouchers are issued once you appear and pass any AWS certification exam. You can then use the vouchers for the subsequent exams.

1. To access vouchers, you need to login to the training website https://www.aws.training/

2. Select **Certification** Tab

3. Click **Go To Your Account** button to open the certification website

4. The above button will redirect to https://www.certmetrics.com/amazon/

5. Select **Benefits**

6. All Active Benefits are listed on the benefits page

    a. Look for **50% Discount on your next Exam**

    b. Click on the **Claim Benefit link**

    c. A code is issued and displayed on page

    d. You can use the code when registering for the exam