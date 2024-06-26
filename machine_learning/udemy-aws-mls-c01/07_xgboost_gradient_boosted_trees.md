# XGBoost

## Introduction to XGBoost (Lesson 68)

### XGBoost in Machine Learning
- **XGBoost (eXtreme Gradient Boosting)**: Highly regarded in ML competitions for handling complex datasets.
- **Boosting Technique**: Builds an ensemble of trees sequentially, focusing on correcting previous errors.

### Linear Models
- **Working Principle**: Assigns weights to features; sums weighted features to predict target.
- **Example Weights**: Temperature (0.3), Humidity (-0.1), Wind Speed (0.2).
- **Pros**: Fast, easy to understand, clear feature importance.
- **Cons**: Requires features on similar scales; needs one-hot encoding for categorical data; struggles with non-linear data unless extensive feature engineering is done.

### Tree-Based Models
- **Function**: Splits data using a series of questions; handles non-linear relationships well.
- **Classification**: Pure leaf nodes for single classes.
- **Regression**: Groups similar instances; predicts average target in a leaf node.
- **Pros**: Manages non-linear and mixed scale data; doesn't require one-hot encoding.
- **Cons**: Single trees prone to overfitting; balancing depth to prevent over/underfitting is challenging.

### Ensemble Methods
- **Random Forest**: Combines multiple trees to improve predictions.
- **Diversity in Trees**: Created by varying training data or features.
- **Bagging**: Random sampling of training data for each tree.
- **Boosting (Used by XGBoost)**: Focuses on correcting previous tree's errors; iterative improvement.

### XGBoost vs. Linear Models
- **Linear Models**: Suitable for simpler, linearly separable datasets; require scaled, encoded data.
- **XGBoost**: Effective for complex, non-linear datasets; robust to various data scales and types.

### Conclusion
- **Linear Models**: Preferred for speed and simplicity but limited by data complexity.
- **XGBoost and Tree-Based Models**: Better for complex, non-linear data but require careful tuning to prevent overfitting. Ensemble methods like XGBoost offer enhanced predictive power.

## Labs - Local Mode

- Note that these examples are not specific to sagemaker, they are general XGBoost examples.

### 1. Data Preparation and Training  Simple Regression (Lesson 69&70)

- Use [linear_data_preparation.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/xgboost/LinearAndQuadraticFunctionRegression/linear_data_preparation.ipynb) to generate data.

- Use [linear_xgboost_localmode.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/xgboost/LinearAndQuadraticFunctionRegression/linear_xgboost_localmode.ipynb) to train XGBoost and Linear Regression models.

```
! Sagemaker resets the notebook each time we stop and start the notebook instance.
```

### 2. Data Preparation and Training Non-linear Data set (Lesson 71&72)

- Use [quadratic_data_preparation.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/xgboost/LinearAndQuadraticFunctionRegression/quadratic_data_preparation.ipynb) to generate data and [quadratic_xgboost_localmode.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/xgboost/LinearAndQuadraticFunctionRegression/quadratic_xgboost_localmode.ipynb) to train models.

### 3. Data Preparation and Training for Bike Rental Regression (Lesson 74&75)

- Use [bikerental_data_preparation_rev1.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/xgboost/BikeSharingRegression/bikerental_data_preparation_rev1.ipynb) to generate data and [bikerental_xgboost_localmode_rev1.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/xgboost/BikeSharingRegression/bikerental_xgboost_localmode_rev1.ipynb) to train models.

### 4. Train using Log of Count (Lesson 76)

- Use [bikerental_data_preparation_rev3.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/xgboost/BikeSharingRegression/bikerental_data_preparation_rev3.ipynb) to generate data and [bikerental_xgboost_localmode_rev3.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/xgboost/BikeSharingRegression/bikerental_xgboost_localmode_rev3.ipynb) to train models.

```
! The last 3 example are same with Lab 1 regarding the Sagemaker knowledge.
```

## How to increase quota limit (Lesson 77)

If you encounter a `ResourceLimitExceeded Error`, follow these steps to request a quota increase:

### Steps to Request Quota Increase
1. **Navigate to Service Quota Console**: Go to [Service Quota Console](https://console.aws.amazon.com/servicequotas/home/services/sagemaker/quotas).
2. **Search for Quota Names**: Look for the following quotas:
   - `ml.m5.xlarge for notebook instance usage`
   - `ml.m5.xlarge for training job usage`
   - `ml.m5.xlarge for spot training job usage`
   - `ml.m5.xlarge for endpoint usage`
3. **Request Quota Increase**:
   - Click on the quota name to view its detail page.
   - Scroll to the "Request Quota Increase" section.
   - If the current quota value is 0, request an increase to 1.

### Additional Resources
- Detailed instructions are available at [Requesting a Quota Increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html).
- For more information, visit the [SageMaker Service Quotas Page](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html).

## Labs - Using SageMaker Provided Algorithms

There are four steps when you use SageMaker cloud: 

1. You need to store your training and validation files in S3
2. Specify the training algorithm and hyperparameters
3. Configure the type of server and number of of servers to use for training
4. Create a realtime endpoint for the trained model.

### How to train using SageMaker's built-in XGBoost Algorithm (Lesson 78)

- Use [xgboost_cloud_training_template.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/xgboost/BikeSharingRegression/xgboost_cloud_training_template.ipynb)
- Make sure to set the correct `bucket_name` for your S3 bucket.
- AZ of the notebook instance and the S3 bucket should be the same.
- Sagemaker maintains all algorithms as container, which are mainteined in ECR.

### Q&A: How does SageMaker built-in know the target variable? (Lesson 79)

- During training, the first column in the CSV file is the target variable
- During inference, you need to provide only the features (i.e. target variable should not be provided)
- [Here](https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost.html) is the relevant notes.
   - For CSV training, the algorithm assumes that the target variable is in the first column and that the CSV does not have a header record.
   - For CSV inference, the algorithm assumes that CSV input does not have the label column.
   - For libsvm training, the algorithm assumes that the label is in the first column. - - Subsequent columns contain the zero-based index value pairs for features. So each row has the format: `<label> <index0>:<value0> <index1>:<value1> ...` Inference requests for libsvm might not have labels in the libsvm format

### How to run predictions against an existing SageMaker Endpoint (Lesson 80)

TODOs in this lab:
- Invoke endpoint for interactive use cases
- Connect to an existing endpoint
- Endpoint security
- How to send multiple observations in a single call

Let's go:
- Use [xgboost_cloud_prediction_template.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/xgboost/BikeSharingRegression/xgboost_cloud_prediction_template.ipynb)

   ```
   ! Notice that this notebook doesn't define any role/permissions; it's because AWS uses the permissions of the notebook instance to access the endpoint.
   ```

## SageMaker Endpoint Features (Lesson 82)

### Integration with CloudWatch and Auto Scaling
- AWS integrates with CloudWatch and Auto Scaling for monitoring and automated scaling. 
- Here's an overview of how SageMaker manages your model endpoints:
   - **CloudWatch**: AWS's monitoring service that continuously tracks instance and endpoint performance. You can set alarms based on specific metrics.
   - **Auto Scaling**:
      - **Replacement Instances**: Automatically launches a replacement if an instance becomes unhealthy.
      - **Scaling Based on Workload**: Configurable to scale infrastructure depending on the workload, like increasing or decreasing the number of servers.

### High Availability and Load Balancing
- **Multiple Instances**: Deploying your model on multiple instances can prevent a single point of failure. If one instance fails, the endpoint routes traffic to healthy instances.
- **Load Balancing**: Requests to the endpoint are automatically balanced across available instances.
- **Availability Zones**: Instances are distributed across multiple Availability Zones to survive zone-level failures.

### Metrics for Monitoring and Scaling
- **CloudWatch Metrics**: Tracks errors, invocations, CPU, memory, and GPU utilization, etc.
- **SageMaker Variant Invocations Per Instance**: Tracks average requests per minute per instance. Useful for scaling decisions.
- **Safety Factor**: SageMaker suggests starting with a factor of 0.5 (keeping instance load at 50% or less).

### Handling Different Versions of Models
- **Multiple Variants**: Deploy multiple versions of a model to the same endpoint.
- **Traffic Distribution**: Configure endpoints to distribute traffic among different model versions, useful for testing new models in production.
- **Version Rollback**: Easily shift traffic back to a previous version if a new version underperforms.

## SageMaker Spot Instances - Save up to 90% for training jobs (Lesson 83)

Spot instances in AWS SageMaker can significantly reduce the cost of training machine learning models, offering discounts of up to 90% compared to on-demand instances. 

### Advantages of Using Spot Instances
1. **Cost-Effective**: Huge discounts (over 80%, varies by instance type and size).
2. **Flexibility**: Better chances of obtaining an instance when flexible with type and size.
3. **Resumption of Training**: SageMaker handles spot-interruptions and resumes training when capacity is available.

### Considerations and Best Practices
- **Termination by AWS**: Spot instances can be terminated by AWS at any time, usually with a two-minute notice.
- **Use Case**: Ideal when training time is flexible and cost-saving is a priority.
- **Configuration in SageMaker**:
  - Set `use_spot_instance` flag to `true` in the estimator.
  - Enable checkpointing to save model artifacts periodically, allowing training to resume from the last checkpoint if the instance is terminated.
  - Specify `maximum wait time` for the training job, considering spot instances are not guaranteed.
  - Define `maximum run time` to limit the duration of the training job.

### Understanding Job Output Metrics
- **Training Seconds**: Total duration of the training job.
- **Billable Seconds**: Actual time billed after applying spot discounts (significantly lower than training seconds for spot instances).

### Useful Resources
- **Example of Using Spot Instances**: [Amazon SageMaker Managed Spot Training Example](https://github.com/aws-samples/amazon-sagemaker-managed-spot-training/blob/main/xgboost_built_in_managed_spot_training_checkpointing/xgboost_built_in_managed_spot_training_checkpointing.ipynb)
- **AWS Documentation**: [Managed Spot Training in SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html)

## More Labs

### Lab - Multi-class Classification (Lesson 84)

- Use [iris_data_preparation.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/xgboost/IrisClassification/iris_data_preparation.ipynb) to generate data 
- Use [iris_xgboost_localmode.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/xgboost/IrisClassification/iris_xgboost_localmode.ipynb) to train model.

### Lab - Binary Classification (Lesson 85)

- Use [diabetes_data_preparation.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/xgboost/DiabetesClassification/diabetes_data_preparation.ipynb) to generate data
- Use [diabetes_xgboost_localmode.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/xgboost/DiabetesClassification/diabetes_xgboost_localmode.ipynb) for training.

## Data Leakage (Lesson 89)

- Data leakage is a critical issue in machine learning that can lead to overly optimistic model performance during training, but poor results in production.
- It occurs when information from the target variable is inadvertently included in the input features.

### Common Sources of Data Leakage
1. **Using Whole Data Statistics for Feature Engineering:** Don’t apply normalization, standardization, or imputation using statistics from the entire dataset, as it includes test data information.

2. **Duplicate Data Points:** Don’t Allow duplicates in your test data, as the same data points might appear in both training and testing sets.

3. **Handling Time Series Data:** Don’t Split time series data randomly. It can lead to future information leaking into the training set due to the sequential nature of the data.

## HyperParameter Tuning, Bias-Variance, Regularization (Lesson 90)

### Key Hyperparameters in XGBoost
1. **Objective**: Sets the learning objective. Common options include:
   - `reg:linear` for linear regression.
   - `binary:logistic` for binary classification.
   - `multi:softmax` for multiclass classification.

2. **Number of Rounds**: Determines the number of trees for learning. More trees can lead to overfitting.

3. **Early Stopping Rounds**: Helps prevent overfitting by stopping the training when the validation loss doesn't decrease for a specified number of rounds.

### Bias and Variance in Machine Learning
- **High Bias (Underfitting)**: Indicates that the model hasn’t learned enough from the training data, leading to high training and validation errors. To reduce high bias, add more features, combine features, create higher-order features, train longer, or decrease regularization.
- **High Variance (Overfitting)**: Occurs when the model memorizes the training data too well, failing to generalize to new, unseen data. To reduce high variance, simplify the model, reduce the number of iterations, or increase regularization.

### Understanding Regularization
- Regularization reduces the model's dependence on specific features, encouraging it to learn from all relevant features.
- **Types of Regularization**:
  - **L1 Regularization (Alpha)**: Aggressively eliminates less important features.
  - **L2 Regularization (Lambda)**: Reduces the weight of dominant features.

### Hyperparameter Tuning
- **Manual vs. Automated Tuning**: While manual tuning allows for granular control, automated tuning (like grid search, random search, or SageMaker's automatic tuning) saves time and often yields better results.
- **SageMaker's Approach**: Treats tuning as a supervised learning problem, optimizing the search for hyperparameters.
