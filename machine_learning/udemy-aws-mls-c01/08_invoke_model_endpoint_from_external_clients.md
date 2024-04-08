# Invoke Model Endpoint From External Clients

## Integration Overview (Lesson 96)

### 1. Python SDKs (Direct Client Interaction with SageMaker Endpoint)
   - **SageMaker SDK**: Specifically designed for SageMaker, offering high-level abstractions.
   - **Boto3 SDK**: General AWS SDK for Python, providing more control but requires detailed configuration.

### 2. AWS Lambda (Microservice-Based Integration)
   - Serverless compute service ideal for hosting endpoint integration logic.
   - Simplifies the architecture by abstracting server management and scaling.
   - Lambda functions can preprocess input data, invoke the SageMaker endpoint, and post-process the results.

### 3. API Gateway and Lambda (Exposing Endpoints as RESTful APIs)
   - Combining these services allows you to create RESTful APIs for your endpoints.
   - Platform-agnostic: Facilitates endpoint invocation regardless of the client's programming language.
   - Scalable and maintainable: Manages traffic, authorizes API calls, and monitors performance.

### 4. Data Transformations
   - Consistent data preprocessing is crucial both during training and prediction.
   - The same transformations (e.g., one-hot encoding, scaling) applied during model training should be replicated when preparing data for prediction.
   - This can be embedded in Lambda functions or within client applications.

## Labs - Client to Endpoint

### Using SageMaker SDK (Lesson 97)

- In this lab, we will invoke a SageMaker endpoint using the SageMaker SDK from **local environment**.
- We will use the XGBoost bike rental model, so chek Lesson 78 if you didn't create it yet.
- You can create the endpoint using `ml_admin` user.
- Use [invoke_using_sagemaker_sdk.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/IntegrationExamples/invoke_using_sagemaker_sdk.ipynb) notebook locally.
- This notebook uses the `ml_user_predict` credentials, so make sure you have configured it beforehand.
- Also check if your `~/.aws/credentials` and `~/.aws/config` files contains this user.

### Using Boto3 SDK (Lesson 98)

- Use [invoke_using_boto3.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/IntegrationExamples/invoke_using_boto3.ipynb) notebook locally.
- Refer to the previous lab for the setup.
- Boto3 also requires some work in the client side. Next lab implements this logic as a micro-service using lambda serverless infrastructure.

## Lab - Microservice - Lambda to Endpoint

### 1. Format Payload (Lesson 99)

- First we need to update our endpoint to accept JSON payloads.
- We will use [invoke_using_boto3_json.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/IntegrationExamples/invoke_using_boto3_json.ipynb) notebook locally.

### 2. Lambda to Endpoint (Lesson 101)

#### Setting up IAM Role for Lambda

- When lambda functions run our code, it needs permission to access services that are referenced.
- We can grant permission to a lambda function using an IAM role.

1. Use your `my_admin` account.
2. Select Roles and create a new role.
3. Role Configuration: 
   - Select AWS service as Lambda.
   - Assign `SageMakerInvokeEndpoint` policy for SageMaker endpoint invocation and `AWSLambdaBasicExecutionRole` for Lambda function logging.
   - Give name : `lambda_sagemaker_invoke_endpoint`

#### Creating a Lambda Function

1. Under Services, select `Lambda`. Then `Create Function`.

2. We can `Author from Scratch`:
   - Name: `bikerental_prediction`
   - Runtime: Python 3.6 or later.
   - Permissions: Use the role `lambda_sagemaker_invoke_endpoint`.

3. Implementing the Function:
   - Use the code from [invoke_using_boto3_lambda.py](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/IntegrationExamples/invoke_using_boto3_lambda.py) in the `IntegrationExamples` folder.
   - Define the entry point as `lambda_handler`.
   - Deploy changes.

4. Environment Variable:
   - Set `ENDPOINT_NAME` to your SageMaker endpoint name.

5. Save and Test the Function:
   - Create a test event using [LambdaTestEvent.txt](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/IntegrationExamples/LambdaTestEvent.txt) file.
   - First create an event for a single observation (`Bike Single Observation`)
   - Name the event as `BikeSingleObservation`
   - Click `Test` and check the results.

#### Monitoring and Logging

- All the messages that you print in the lambda function will be logged to CloudWatch.
- View logs under the Monitoring tab or directly in the CloudWatch service.

### 3. API Gateway, Lambda, Endpoint (Lesson 103)

- At this point we can expose the AWS Lambda function as is, or as a RESTful API using API Gateway. 
- API Gateway approach provides a clean interface for backend services, security management, and scalability.
- So client will have access to the `API Gateway`, which will forward the request to the `Lambda function`, which will invoke the `SageMaker endpoint`.

#### Setting up API Gateway
1. Login to AWS Management Console with `my_admin` account, navigate to API Gateway.
2. Create a new REST API named `BikeRentalPrediction`.
3. Select `Create Method` ans select `POST` method.
4. Select Integration Type as `Lambda Function`.

#### Testing Integration
- Copy and paste the same single observation (`Bike Single Observation`) in Lesson 101.

#### Deploying API Gateway
- Select `Deploy API` and create a new stage named `beta`.
- A URL will be generated for the API Gateway endpoint.

#### Invoking API from Various Clients
1. Using Browser Extension (e.g., RESTer):
   - Method: POST
   - URL: API Gateway URL
   - Body: JSON payload
   - Content Type: `application/json`
   - Send request and receive predictions.

2. Using Python Client
   - Use [invoke_api_gateway.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/IntegrationExamples/invoke_api_gateway.ipynb) notebook locally.
