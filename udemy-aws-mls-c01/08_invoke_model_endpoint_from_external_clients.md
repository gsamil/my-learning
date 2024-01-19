# 96. Integration Overview

Integrating SageMaker endpoints into applications is a crucial aspect of deploying machine learning models. AWS offers various SDKs for different programming languages, facilitating this integration. This section focuses on Python examples and gradually explores solutions suitable for any programming language.

#### 1. Direct Client Interaction with SageMaker Endpoint
   - **SDKs for Python**: 
     - **SageMaker SDK**: Specifically designed for SageMaker, offering high-level abstractions.
     - **Boto3 SDK**: General AWS SDK for Python, providing more control but requires detailed configuration.

#### 2. Microservice-Based Integration with AWS Lambda
   - **Lambda Functions**: Serverless compute service ideal for hosting endpoint integration logic.
   - **Benefits**: Simplifies the architecture by abstracting server management and scaling.
   - **Usage**: Lambda functions can preprocess input data, invoke the SageMaker endpoint, and post-process the results.

#### 3. Exposing Endpoints as RESTful APIs
   - **API Gateway and Lambda**: Combining these services allows you to create RESTful APIs for your endpoints.
   - **Advantages**: 
     - Platform-agnostic: Facilitates endpoint invocation regardless of the client's programming language.
     - Scalable and maintainable: Manages traffic, authorizes API calls, and monitors performance.

#### 4. Data Transformations
   - **Importance**: Consistent data preprocessing is crucial both during training and prediction.
   - **Considerations**: The same transformations (e.g., one-hot encoding, scaling) applied during model training should be replicated when preparing data for prediction.
   - **Implementation**: This can be embedded in Lambda functions or within client applications.

#### 5. Setting Up Development Environment
   - **Recommended Tools**: 
     - **Anaconda Python Distribution**: Provides a comprehensive Python environment suitable for data science and machine learning.
     - **Local Python Setup**: Essential for testing and developing client-side code that interacts with SageMaker endpoints.

#### Summary
Integrating SageMaker endpoints into applications can vary from direct SDK usage to more complex microservices architectures using AWS Lambda and API Gateway. The choice depends on the specific use case, desired level of abstraction, and the client's programming environment. Consistency in data preprocessing is vital across all stages, from training to prediction.

# 97. Lab - Client to Endpoint using SageMaker SDK

In this lab, we will invoke a SageMaker endpoint using the SageMaker SDK. This example demonstrates a client directly interacting with a SageMaker endpoint, specifically using the XGBoost bike rental model. We'll start by deploying an endpoint, and then use a Jupyter notebook to invoke the endpoint.

#### Steps to Deploy an Endpoint:

1. **Sign in to AWS Management Console** with your admin account.
2. **Choose the appropriate region** (e.g., US East N. Virginia or the region where you trained your model).
3. In SageMaker Management Console, navigate to **Endpoints**.
4. **Create a new endpoint**:
   - Endpoint Name: `xgboost-bike-train-v1`.
   - Configuration: Search for `xgboost` and select `xgboost-biketrain-v1` configuration.
   - If the configuration doesn't exist, refer back to your XGBoost notebook for the correct name or region.
5. **Wait for the endpoint to be ready** (approximately 5 minutes).

#### Invoke Endpoint Using SageMaker SDK:

1. **Open Command Prompt** and navigate to your SageMaker course folder.
2. **Launch Jupyter Notebook**.
3. Open `IntegrationExamples` and then the `invoke_using_sagemaker_sdk` notebook file.
4. **Establish a session** using the `ml_user_predict` credentials and specify the region.
5. **Acquire a real-time predictor** for the endpoint.
6. **Set content type and serializer** as XGBoost expects data in CSV format.
7. **Perform data transformations**:
   - Use the `transform_data` function to transform new data similarly to how it was done during model training.
   - Ensure the data is in the correct sequence for XGBoost.
8. **Invoke the prediction**:
   - Use `predict` method and handle any errors or transformations needed (e.g., applying the inverse transformation for log of count).
   - For multiple observations, pass them in a single predict call.
9. **Apply inverse transformations** to get the actual count from predictions.
10. Use `run_predictions` method to handle batching and transformations.
11. **Test the method** with multiple samples.
12. **Predict for all observations** in the test dataset and analyze the response time for different batch sizes.

#### Issues and Considerations:

- **Integration Logic**: Managing data transformation logic in the client application can be challenging for ongoing maintenance.
- **SDK Limitation**: SageMaker SDK is specific to Python. If clients are using other languages, you would need to use a standard AWS SDK like Boto3.

# 98. Lab - Client to Endpoint using Boto3 SDK

In this lab, we will use the Boto3 library, a Python version of AWS SDK, to interact with a SageMaker endpoint. This example demonstrates a client directly interacting with a SageMaker endpoint.

#### Using Boto3 for Endpoint Invocation

1. **Open `invoke_using_boto3 SDK` Notebook**: Locate this file in the IntegrationExamples directory.

2. **Import and Setup Boto3**:
   - Import the Boto3 module.
   - Establish a session with AWS using `ml_user_predict` credentials.
   - Boto3 is organized by AWS services, with Sagemaker and SageMaker runtime being two of the available services.

3. **SageMaker Runtime Client**:
   - Since this example focuses on invoking an endpoint, create a client of type SageMaker runtime.

4. **Data Transformation**:
   - The code for data transformation remains similar to the previous demo.

5. **Invoke Endpoint**:
   - Use the `invoke_endpoint` method by specifying the endpoint name and payload data.
   - Set the content type as CSV for payload data.
   - The HTTP response code of 200 indicates a successful call.
   - Retrieve the prediction results from the response body.

6. **Handling Multiple Observations**:
   - Multiple observations can be sent in a single call, separated by newline characters.
   - A convenience method is defined to encapsulate the logic for invoking the endpoint and applying the inverse transformation.

#### Advantages of Using Boto3 SDK

- **Flexibility**: Boto3 offers a more flexible approach for integration with SageMaker and other AWS services.
- **Wide Support**: Being a part of the standard AWS SDK, Boto3 supports various AWS services, making it ideal for broader applications.

# 99. Microservice - Lambda to Endpoint - Payload

In this lab, we explore how to invoke a SageMaker endpoint from a client outside of AWS, focusing on handling JSON payloads. This approach is a precursor to moving integration logic to a microservice using AWS Lambda.

#### Modifying Code to Accept JSON Payloads

1. **JSON Payload Structure**: 
   - The client application sends observations in a standard JSON format.
   - The payload structure consists of an `attribute` that contains a list of instances, each with its `features`.

2. **Adapting to XGBoost Format**: 
   - XGBoost supports CSV and LIBSVM formats for inference. 
   - The Lambda function will internally convert from JSON to CSV when invoking XGBoost predictions.

3. **Sample Code Execution**: 
   - Open `invoke_using_boto3_json` notebook in IntegrationExamples.
   - Sample data now is in the form of a list, converted to a JSON payload.
   - The `transform` method accepts a list of features, adds derived features, and returns observations in CSV format.

4. **Testing with Sample Data**: 
   - Test the setup with a sample observation to confirm the transformation to CSV format.
   - Invoke the endpoint with the JSON payload to get predictions.

5. **Handling Multiple Observations**: 
   - You can send multiple observations in the JSON payload and receive predictions for each.

#### Preparing for Lambda Integration

- The code demonstrated here can be adapted into a Lambda function.
- In the upcoming lecture, we will convert this logic into a Lambda function, which will offer a centralized place for model integration logic.

#### Advantages of Lambda Integration

- **Centralized Logic**: Maintaining model integration logic in one place simplifies updates and maintenance.
- **Flexibility**: The client application is insulated from model-specific changes, offering more flexibility in integrating different models or features.
- **Serverless Approach**: AWS Lambda, as a serverless function, provides an efficient and scalable way to handle model integration and invocation.

# 101. Lab - Microservice - Lambda to Endpoint

### Invoking SageMaker Endpoint with AWS Lambda

In this lab, we'll use AWS Lambda, a serverless compute infrastructure, to invoke our SageMaker endpoint. This approach centralizes the model integration logic, providing a scalable and efficient solution for handling model invocations.

#### Setting up IAM Role for Lambda

1. **Login to AWS Management Console**: Use your `my_admin` account.
2. **Open IAM Console**: Select Roles and create a new role.
3. **Role Configuration**: 
   - Select AWS service as Lambda.
   - Assign `SageMakerInvokeEndpoint` policy for SageMaker endpoint invocation.
   - Assign `AWSLambdaBasicExecutionRole` for Lambda function logging.

#### Creating a Lambda Function

1. **Navigate to Lambda Service**: Create a new function.
2. **Function Configuration**:
   - Name: `bikerental_prediction`.
   - Runtime: Python 3.6 or later.
   - Permissions: Use the role `lambda_sagemaker_invoke_endpoint`.

3. **Implementing the Function**:
   - Use the code from `invoke_using_boto3_lambda.py` in the Integration Examples folder.
   - Define the entry point as `lambda_handler`.
   - Parse the event data, transform it, invoke the SageMaker endpoint, and return predictions.

4. **Environment Variable**:
   - Set `ENDPOINT_NAME` to your SageMaker endpoint name.

5. **Save and Test the Function**:
   - Create a test event using `BikeSingleObservation` payload.
   - Test and observe the result.

#### Monitoring and Logging

- **CloudWatch Logs**: 
  - View logs under the Monitoring tab or directly in the CloudWatch service.
  - Inspect input payloads and predicted results.

#### Benefits of Lambda Integration

- **Centralized Logic**: Update the endpoint and modify code in one place, simplifying maintenance.
- **Scalability**: Lambda automatically scales to support concurrent invocations.
- **Flexibility**: Easily adapt to different models or changes in integration logic.

# 103. Lab - API Gateway, Lambda, Endpoint

#### Overview
In this lab, we'll expose the AWS Lambda function, which integrates with our SageMaker endpoint, as a RESTful API using API Gateway. This approach provides a clean interface for backend services, security management, and scalability.

#### Architecture
- **Client Applications**: Apps, browsers, etc., sending requests.
- **API Gateway**: Forwards requests to Lambda.
- **AWS Lambda**: Submits requests to SageMaker endpoint.
- **SageMaker Endpoint**: Processes requests and returns responses.

#### Setting up API Gateway
1. **Login to AWS Management Console**: Use `my_admin` account.
2. **Navigate to API Gateway**: Create a new API named `bike_rental_prediction`.
3. **Define HTTP Actions and Resources**: Set up a POST method for JSON payloads.
4. **Integration with Lambda Function**: Forward requests to the `bikerental_prediction` Lambda function.

#### Testing Integration
- **Test API in Console**: Send JSON payloads with observations.
- **Deploy API**: Create a new stage (e.g., beta) and deploy the API to generate a URL.

#### Invoking API from Various Clients
1. **Using Browser Extension (e.g., RESTer)**:
   - Method: POST
   - URL: API Gateway URL
   - Body: JSON payload
   - Content Type: `application/json`
   - Send request and receive predictions.

2. **Using Python Client**:
   - Use `requests` and `json` modules.
   - Construct JSON payload.
   - POST request to API Gateway URL.
   - Receive and process the response.

#### Benefits of Using API Gateway
- **Simplified Client Logic**: No need for clients to know about model specifics or transformations.
- **Security and Management**: API Gateway can enforce security policies and manage traffic.
- **Serverless Architecture**: Both Lambda and API Gateway are serverless, ensuring scalability and reducing maintenance.

#### Summary
- **Direct Client-SageMaker Endpoint Integration**: Initially explored with SageMaker SDK and Boto3.
- **Lambda Function-Based Microservice**: Centralized model-related complexity and transformation logic.
- **RESTful API via API Gateway**: Recommended approach for simplicity, security, and scalability.
- **Serverless Benefits**: Automated scaling and management by AWS.
