# SageMaker Housekeeping

## S3 Bucket Setup (Lesson 17)

### Purpose

- Store data files for model training.
- Save trained models and artifacts post-training.

### Steps for Bucket Creation

1. **Sign-In**:
    - Log in to AWS console using `my_admin` account.
    - Ensure using the N. Virginia region.

2. **Access S3 Service**:
    - In AWS Services, search and open the S3 Management Console.

3. **Create Bucket**:
    - Click on `Create bucket`.
    - Choose a globally unique name following the convention: `prefix-ml-sagemaker`.
    - If name conflict occurs, adjust the prefix for uniqueness.
    - Select N. Virginia as the region.

4. **Bucket Creation Complete**:
    - Click on `Create` to finalize the bucket setup.
    - The bucket will automatically replicate data across multiple Availability Zones in N. Virginia.

## Setup SageMaker Notebook Instance (Lesson 18)

### Steps for Setup

1. **Sign-In**:
    - Log in with the `my_admin` account to AWS Management Console.

2. **Access SageMaker Service**:
    - Find SageMaker service and select `Notebook instances`.

3. **Select Region**:
    - Choose N. Virginia or a region close to you. Use the same region throughout the course.

4. **Create Notebook Instance**:
    - Click on `Create notebook instance`.
    - Name the instance (e.g., `SageMakerCourse`).
    - Select `T3 medium` for the server configuration.

5. **IAM Role Configuration**:
    - Create a new IAM role during instance setup.
    - Grant access to any S3 bucket or specific ones as needed.

6. **Instance Creation and Access**:
    - Once the instance status is 'In service', access it by clicking `Open Jupyter`.
    - The homepage of the Jupyter notebook environment will appear.

### Key Benefits

- AWS manages patching and maintenance of the notebook instance.
- Stop the instance when not in use to avoid charges and restart as needed.
