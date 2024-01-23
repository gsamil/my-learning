# Endpoint Changes with Zero Downtime

## [Repeat] Endpoint Features, Monitoring and AutoScaling (Lesson 105)

- Model deployed to an endpoint with a single instance poses a risk of failure, impacting client applications.

#### Multi-Instance Configuration for Reliability
- **Load Balancing**: Requests are distributed across available instances for better reliability.
- **High Availability**: Instances spread across multiple Availability Zones to withstand zone-level failures.

#### Auto Scaling Based on Workload
- **Scaling Strategy**: 
  - **Scale-Out**: Add more instances during increased workload.
  - **Scale-In**: Reduce instances when workload decreases.
- **Metrics for Decision Making**: 
  - Number of requests per second, CPU utilization, etc.
  - Use CloudWatch metrics to inform scaling decisions.

#### Recommended Safety Factor
- **Safety Factor of 0.5**: Keep instance load at or below 50%.

#### Hosting Multiple Model Variants
- Distribute traffic between models (e.g., 90% to existing model, 10% to new version).
- Adjust traffic distribution based on new model performance.

## How to handle changes to production system? (Lesson 106)

1. **Single Model Endpoint**
   - **Structure**: Single serving container with a model on an instance.
   - **Fault Tolerance**: Replication for reliability, load balancing, and auto-scaling based on traffic.
   - **Limitation**: Single point of failure; one container per instance.

2. **Multiple Model/Production Variants**
   - **Setup**: New endpoint configuration with old and new models.
   - **Traffic Distribution**: Configure traffic weights (e.g., 70% old model, 30% new model).
   - **Advantages**: Zero downtime deployments, specific model variant targeting, separate auto-scaling rules.
   - **Drawback**: One serving container and model artifact per instance, leading to multiple server instances.

3. **Multimodal Endpoint**
   - **Usage**: Host multiple models with a shared serving container (same algorithm).
   - **Cost Efficiency**: Reduced infrastructure costs, better utilization of endpoint instances.

4. **Multi-Container Endpoint**
   - **Functionality**: Deploy multiple serving containers on a single endpoint.
   - **Use Cases**: Inference pipelines or direct invocation of different algorithm models.
   - **Advantages**: Host different algorithms on one instance, reduce infrastructure costs.
   - **Limitations**: Maximum of five containers co-hosted.

## Lab - A/B Testing Multiple Production Variants (Lesson 107)

1. **Prepare & Train Models**
   - Use [multiple_versions_training.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/xgboost/BikeSharingRegression/multiple_versions_training.ipynb) to create training jobs.

2. **Create SageMaker Models**
   - Use training jobs to create models.

3. **Create Endpoint Configuration**
   - Then go to `Inference -> Endpoint Configurations` and create a new endpoint configuration.
   - Choose `Create Production Variant` and add the first version of the model.
      - Choose `Edit`.
      - You can update Variant Name as `version-0-90-2`
      - You can select Instance Type as `ml.m5.large`
      - Initial Instance Count and Initial Weight can both stay `1`.
   - Repeat the same steps for the second version of the model, i.e. `version-1-2-2`
   - We've assigned equal initial weight (1) to each model for a 50/50 traffic distribution.

4. **Create Endpoint**
   - Go to `Inference -> Endpoints` and create a new endpoint.
   - You can update Endpoint Name as `xgboost-bikerental`
   - Choose the endpoint configuration you created in the previous step.

5. **Endpoint Management - Adjust Weights**
   - You can adjust weights if necessary from the endpoint configuration.

6. **Endpoint Management - Auto-Scaling**
   - You can also configure auto-scaling based on the variant invocation per instance metric.
   - Select one of the variants and choose `Configure Auto Scaling`.
   - You can set the minimum and maximum instance count and the target value for the metric.
   - We need a trigger for auto scaling to respond to traffic.
   - The default metric that is used for trigger is the `VariantInvocationsPerInstance` metric.
   - This metric tracks the number of requests per minute, per instance.

6. **Invoke Endpoint for A/B Testing**
   - Use the [multiple_versions_prediction.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/xgboost/BikeSharingRegression/multiple_versions_prediction.ipynb) notebook.
   - Set endpoint name, predictor instance, and optionally specify target variant.
   - Compare results for different versions.

7. **Analysis & Cleanup**
   - Don't forget to delete endpoint.

## Lab – Multi-model Endpoint (Lesson 108)

- Deploy two XGBoost models with different hyperparameters on a multimodal endpoint for flexibility and cost reduction.

1. **Prepare & Train Models**
   - Use [multiple_models_training.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/xgboost/BikeSharingRegression/multiple_models_training.ipynb) to train the models, which will create training jobs.

2. **Create SageMaker Model**
   - In SageMaker console, select the first training job (with `hyper1`).
   - Choose "Use multiple models" option.
   - Set model artifact location to the `model` folder in S3. (`s3://asamilg-sagemaker-mls-course/bikerental-hyper/model`)
   - Create the model.

3. **Create Endpoint Configuration**
   - Name: `xboost-bikerental-hyper`.
   - Select the created model.
   - Choose `ml.m5.large` instance type.

4. **Deploy Endpoint**
   - Name: `xgboost-bikerental-hyper`.
   - Use the created endpoint configuration.

5. **Invoke Multimodal Endpoint**
   - Open [multiple_models_prediction.ipynb](https://github.com/gsamil/AmazonSageMakerCourse/blob/master/xgboost/BikeSharingRegression/multiple_models_prediction.ipynb) notebook.
   - Update `target_models` list with model folder names in S3.

6. **Cleanup**
   - Delete the endpoint to avoid ongoing charges.

#### Summary
- Multimodal endpoints allow hosting multiple models with a shared serving container, reducing deployment costs and offering flexibility.
- Models must be trained using the same algorithm for compatibility with the shared container.
- Ideal for rapid deployment of new model versions without additional instance setup.
- Note: Increased latency on initial calls due to on-demand model artifact loading from S3.

## Run Models at the Edge (Lesson 109)

### SageMaker Neo
- **Purpose**: For latency-sensitive and streaming data analysis use cases, SageMaker Neo enables hosting ML models close to the data source.
- **Functionality**: Neo compiles a trained model into an executable for edge devices.
- **Hardware Compatibility**: Supports Intel, NVIDIA, ARM, Cadence, Qualcomm, and Xilinx architectures.
- **Supported Models**: Compatible with MXNet, TensorFlow, PyTorch, and XGBoost models trained via Amazon SageMaker.

### Benefits of SageMaker Neo
1. **Performance Improvement**: Up to 2X increase in performance without sacrificing accuracy.
2. **Framework Size Reduction**: Can achieve up to a 10X reduction. Neo compiles both the model and framework into a single executable for edge deployment.
3. **Cross-Platform Compatibility**: Run the same ML model across multiple hardware platforms.

### AWS IoT Greengrass
- **Role**: Extends AWS capabilities to edge devices, enabling local execution of functions, containers, and ML model predictions.
- **Key Features**: 
   - Runs Lambda functions and Docker containers locally.
   - Executes predictions using ML models offline.
- **Integration with Neo**: 
   - Models compiled with SageMaker Neo are placed in S3.
   - Install GreenGrass and DLR (Deep Learning Runtime) on the edge device.
   - Configure Greengrass to point to the model in S3.
   - Greengrass downloads and hosts the model locally for inference.
