# 6. SageMaker Service and SDK Changes

## Model Training using Console (Lesson 63)

### SageMaker and S3 Usage
- **S3 Integration**: Extensively used for storing data and trained model artifacts.
- **Data Structure**: Data sets are organized with subfolders for training, validation, test data, and model artifacts.
- **Checkpointing**: SageMaker can save the state of a trained model in S3 periodically.

### Creating a Training Job
- **Methods**: AWS CLI, SageMaker console, or programming.
- **SageMaker Console Steps**:
  1. **Job Name**: Specify a unique name.
  2. **IAM Role**: Assign a role with S3 access permissions.
  3. **Algorithm Selection**: Choose from available options (e.g., XGBoost, k-means).
  4. **Data Read Mode**:
     - **File Mode**: Copies entire dataset from S3 to instance.
     - **Pipe Mode**: Streams required data from S3.
  5. **Instance Selection**: Choose type and number of instances.
  6. **Storage Allocation**: Depends on dataset size and data read mode.
  7. **Algorithm Parameters**: Specific to the chosen algorithm.
  8. **Input Data (Channels)**: S3 paths for training, validation, test data.
  9. **Checkpointing**: Optional for saving model snapshots.
  10. **Output Path**: S3 path for storing trained model artifacts.

### Managed Spot Training
- **Cost-Effective**: Uses spare AWS capacity at up to 90% discount.
- **Considerations**:
  - **Availability**: Spot instances may not be immediately available.
  - **Interruptions**: Instances can be terminated anytime, SageMaker handles interruptions.
  - **Checkpointing**: Advised to enable for pause-resume capabilities.

### SageMaker SDK Updates
- **Integration with File Systems**: Supports S3, EFS, and FSx for Lustre.
- **Spot Instance Training**: Supports training and hyperparameter tuning with managed spot instances.
- **Checkpointing Benefits**:
  - Handles unexpected training interruptions.
  - Resumes training from existing checkpoints.
  - Allows intermediate model analysis.
  - Essential for managed spot training.

The lecture provides a detailed overview of recent updates in SageMaker, highlighting its integration with S3 for data management, the process of setting up a training job, and the cost-saving potential of managed spot training. Additionally, the importance of checkpointing in training jobs, especially when using spot instances, is emphasized. The lecture also outlines the enhancements in the SageMaker SDK, particularly in terms of its expanded integration with various file systems and support for spot instance training.

## Model Training using Python SDK (Lesson 64)

### Overview
- **SageMaker SDK**: Primary method for training in this course.
- **Code Examples**: Updated to use spot instances, offering savings on training costs.

### Training and Deployment Process
1. **Import Libraries**: Standard libraries and SageMaker SDK.
2. **Configure S3**: Set locations for model output, training, validation, and test data.
3. **Spot Instance Training**: Controlled by a flag; significantly reduces training costs.
4. **Training Job Configuration**:
   - Set `max_runtime_seconds` and `max_wait_time_seconds`.
   - Enable checkpointing for spot training.
   - Choose algorithm and specify version (e.g., XGBoost).
5. **Create Estimator**:
   - Provide job configuration.
   - Set hyperparameters.
   - Specify S3 data locations.
   - `fit` method initiates training.
6. **Job Output**: Includes total training time and billable seconds.
7. **Model Deployment**: Deploy model for real-time inference, which may take up to 5 minutes.

### Testing and Cleanup
1. **Testing**: Use a separate notebook for testing and verifying endpoint performance.
2. **Endpoint Verification**: Ensure the endpoint name matches in the SageMaker console.
3. **Batch Prediction**: Handle large datasets by sending data in smaller batches.
4. **Cleanup**: Terminate the endpoint to stop accruing charges.

### Cost Saving Tips
1. **SageMaker Trial Period**: Utilize the free trial for labs; turn off spot instances if on trial.
2. **Terminate Endpoints**: Always delete endpoints after use.
3. **Batch Transform Jobs**: Ideal for large datasets; handles deployment, prediction, and cleanup.
4. **Stop Notebook Instances**: Stop when not in use to avoid charges.
5. **Billing Alerts**: Set up billing and budget alerts to monitor charges.

### Summary
This overview provides a comprehensive guide on using the SageMaker SDK for training, including configuration, deployment, testing, and cleanup, with a focus on cost-saving practices. It emphasizes the use of spot instances and the importance of managing resources effectively to optimize training costs.

## Incremental Training (Lesson 65)

- **Purpose**: Enhances existing models with new data or improves performance without starting from scratch.
- **Benefits**:
  - Train with expanded datasets for unaccounted patterns.
  - Utilize artifacts from existing or public models.
  - Resume interrupted training jobs.
  - Experiment with model variants (different hyperparameters/datasets).
- **Functionality**: Use the `model` channel to provide the location of an existing model. SageMaker then uses these artifacts for the new training job.
- **Checkpoints vs. Incremental Training**:
  - Checkpoints: Resume training with the existing dataset, useful for interrupted jobs.
  - Incremental Training: Expand or enhance models with new data or configurations.
- **Supported Algorithms**: Specific algorithms like Object Detection, Image Classification, Semantic Segmentation, etc.
- **Documentation**: Refer to SageMaker documentation for detailed algorithm support and configurations.

[Incremental Training in SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/incremental-training.html)
