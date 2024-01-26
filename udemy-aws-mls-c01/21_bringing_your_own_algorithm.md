# Bringing Your Own Algorithm to SageMaker

## Introduction and How Built-in Algorithms Work (Lesson 235)

### Built-in Algorithms
- Optimized for the AWS Cloud and straightforward to scale.
- Includes popular choices like XGBoost, DeepAR, PCA, FM.

### Pre-built Container Images
- Compatible with MxNet, TensorFlow, scikit-learn, PyTorch.
- A wide selection of algorithms and the ability to develop new ones.

### Extend Pre-built Container Images
- Tailor pre-built images to specific needs.

### Custom Container Images
- Ideal for proprietary algorithms or when using frameworks not supported by SageMaker.

## Training & Hosting with SageMaker (Lesson 236)

### Built-in Algorithms – Training
- **Data Storage**: Training and test data are securely stored in S3.
- **Configuration**: Includes the algorithm image, hyperparameters, and details about the instance type and count.
- **Training Process**: SageMaker manages the instance setup, data retrieval from ECR and S3, and stores the model back to S3.

### Custom Image – Training and Hosting
- **Container Requirements**: Must meet SageMaker specifications and stored in ECR.
- **Entry Points**: Containers need to define training and serving entry points.
- **Model Serialization**: Post-training, model artifacts are serialized to a directory for SageMaker to upload to S3.

### Built-in Algorithms – Hosting (Realtime, Batch)
- **Model Deployment**: Utilizes the same Docker image from training, with the option to select specific models for deployment.
- **Hosting Configuration**: Involves specifying the model's S3 location and configuring the instance details.

### Custom and Framework Images – Hosting
- **Framework Adaptation**: Use SageMaker's containers for popular frameworks for easier adaptation.
- **Local Hosting**: Option to host the model on a SageMaker notebook instance for development and testing.

## Container Folder Structure (Lesson 237)

### SageMaker Training and Hosting Requirements

- **Folder Structure**: A standard structure is used for data, code, model, and output.
- **Instrumentation and Logs**: Use standard output/error and CloudWatch for logging.
- **Metric Capture**: Metrics are logged and captured using regex patterns.
- **Image Strategy**: Single image for training and hosting, or separate images if needed.

### Training and Hosting Folder Structure

- `/opt/ml/` contains subfolders:
  - `input/` for configuration and data.
    - `config/` for hyperparameters.
      - `hyperparameters.json` for hyperparameters.
      - `resourceconfig.json` for instance type and count.
    - `data/` for training and test data.
      - `channels/` for multiple data channels.
  - `code/` for scripts.
  - `model/` for trained models.
  - `output/` for failure captures.
    - `failure/` for failure logs.


## Lab (Lecture 238 & 239)

- [Scikit-Learn Training and Serving Example](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/CustomAlgorithm/ScikitLearn/Iris/iris_scikit_learn_training_and_serving.ipynb)

    - I had an error about `numexpr` package. I fixed it with below command:

        ```python
        !pip install numexpr==2.8.0 --upgrade
        ```

- [Built Your Own Container](https://github.com/aws/amazon-sagemaker-examples/blob/main/advanced_functionality/scikit_bring_your_own/scikit_bring_your_own.ipynb)

    - I had an error in this line: (I think it's related to sagemaker versions)
    
        ```python
        from sagemaker.predictor import csv_serializer

        predictor = tree.deploy(1, "ml.m4.xlarge", serializer=csv_serializer)
        ```
    
    - I had to change it to:
    
        ```python
        from sagemaker.serializers import CSVSerializer

        csv_serializer = CSVSerializer()

        predictor = tree.deploy(1, "ml.m4.xlarge", serializer=csv_serializer)
        ```

    - I had another error in this line: 

        ```python
        transformer.transform(
            data_location, 
            content_type="text/csv", 
            split_type="Line", 
            input_filter="$[1:]"
        )
        transformer.wait()
        ```

        ```
        ResourceLimitExceeded: An error occurred (ResourceLimitExceeded) when calling the CreateTransformJob operation: The account-level service limit 'ml.m4.xlarge for transform job usage' is 0 Instances, with current utilization of 0 Instances and a request delta of 1 Instances. Please use AWS Service Quotas to request an increase for this quota. If AWS Service Quotas is not available, contact AWS support to request an increase for this quota.
        ```

    - I had to request an increase for `ml.m5.xlarge for transform job usage` quota. See [this link](https://repost.aws/knowledge-center/sagemaker-resource-limit-exceeded-error) for more details.

