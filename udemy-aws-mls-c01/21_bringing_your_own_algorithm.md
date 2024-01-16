# Bringing Your Own Algorithm to SageMaker

## Options for Building Models with SageMaker

### Built-in Algorithms
- **Ease of Use**: Optimized for the AWS Cloud and straightforward to scale.
- **Algorithms**: Includes popular choices like XGBoost, DeepAR, PCA, FM.

### Pre-built Container Images
- **Framework Support**: Compatible with MxNet, TensorFlow, scikit-learn, PyTorch.
- **Flexibility**: A wide selection of algorithms and the ability to develop new ones.

### Extend Pre-built Container Images
- **Customization**: Tailor pre-built images to specific needs.

### Custom Container Images
- **Versatility**: Ideal for proprietary algorithms or when using frameworks not supported by SageMaker.

## Training with SageMaker

### Built-in Algorithms – Training
- **Data Storage**: Training and test data are securely stored in S3.
- **Configuration**: Includes the algorithm image, hyperparameters, and details about the instance type and count.
- **Training Process**: SageMaker manages the instance setup, data retrieval from ECR and S3, and stores the model back to S3.

### Custom Image – Training and Hosting
- **Container Requirements**: Must meet SageMaker specifications and stored in ECR.
- **Entry Points**: Containers need to define training and serving entry points.
- **Model Serialization**: Post-training, model artifacts are serialized to a directory for SageMaker to upload to S3.

## Hosting with SageMaker

### Built-in Algorithms – Hosting (Realtime, Batch)
- **Model Deployment**: Utilizes the same Docker image from training, with the option to select specific models for deployment.
- **Hosting Configuration**: Involves specifying the model's S3 location and configuring the instance details.

### Custom and Framework Images – Hosting
- **Framework Adaptation**: Use SageMaker's containers for popular frameworks for easier adaptation.
- **Local Hosting**: Option to host the model on a SageMaker notebook instance for development and testing.

## SageMaker Training and Hosting Requirements

- **Folder Structure**: A standard structure is used for data, code, model, and output.
- **Instrumentation and Logs**: Use standard output/error and CloudWatch for logging.
- **Metric Capture**: Metrics are logged and captured using regex patterns.
- **Image Strategy**: Single image for training and hosting, or separate images if needed.

## Container Folder Structure

- `/opt/ml/` contains subfolders:
  - `input/` for configuration and data.
  - `code/` for scripts.
  - `model/` for trained models.
  - `output/` for failure captures.

## Summary

SageMaker facilitates a streamlined process for training and hosting machine learning models by providing a standardized environment. Custom containers can easily integrate into this environment, provided they conform to SageMaker's specifications. This approach simplifies the development and deployment of machine learning workflows, allowing for scalability and ease of use within the AWS ecosystem.
