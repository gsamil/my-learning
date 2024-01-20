# 105. [Repeat] Endpoint Features, Monitoring and AutoScaling

#### Single Instance Endpoint and Its Limitations
- **Initial Setup**: Model deployed to an endpoint with a single instance.
- **Issue**: Single instance hosting poses a risk of failure, impacting client applications.

#### Integration with CloudWatch and Auto Scaling
1. **CloudWatch**: AWS's monitoring service.
   - Monitors instances and endpoints continuously.
   - Allows setting up of alarms based on specific configurations.

2. **Auto Scaling**: Responds to alarms with automated actions.
   - Can launch replacement instances if one becomes unhealthy.
   - Replacement process might take time, affecting client applications temporarily.

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
- **Example Calculation**: 
  - Maximum requests per second (e.g., 100 requests).
  - Compute capacity needed at 50% load over a minute (3000 requests per minute).

#### Hosting Multiple Model Variants
- **Use Case**: Testing new model versions in production.
- **Configuration**: 
  - Distribute traffic between models (e.g., 90% to existing model, 10% to new version).
  - Adjust traffic distribution based on new model performance.

#### Summary of SageMaker Managed Endpoints
- **Automatic Instance Replacement**: Unhealthy instances are replaced automatically.
- **Scalable Infrastructure**: Adjusts server count according to workload.
- **Support for Multiple Model Variants**: Facilitates A/B testing of models in a single endpoint.

# 106. How to handle changes to production system?

#### Understanding the Workflow
- **Fit Method**: Trains the model and stores artifacts in S3.
- **Deploy Method**: Creates a SageMaker model, endpoint configuration, and endpoint from S3 artifacts.
- **Flexibility**: These steps increase deployment flexibility, allowing for model improvements, A/B testing, and algorithm changes.

#### Deployment Scenarios

1. **Single Model Endpoint**
   - **Structure**: Single serving container with a model on an instance.
   - **Fault Tolerance**: Replication for reliability, load balancing, and auto-scaling based on traffic.
   - **Limitation**: Single point of failure; one container per instance.

2. **Multiple Model Variants (Production Variants)**
   - **Setup**: New endpoint configuration with old and new models.
   - **Traffic Distribution**: Configure traffic weights (e.g., 70% old model, 30% new model).
   - **Advantages**: Zero downtime deployments, specific model variant targeting, separate auto-scaling rules.
   - **Drawback**: One serving container and model artifact per instance, leading to multiple server instances.

3. **Multimodal Endpoint**
   - **Usage**: Host multiple models with a shared serving container (same algorithm).
   - **Cost Efficiency**: Reduced infrastructure costs, better utilization of endpoint instances.
   - **Drawbacks**: 
     - Cold start delays.
     - Limited to compatible models (same algorithm).
     - Requires model tracking and S3 location specification.

4. **Multi-Container Endpoint**
   - **Functionality**: Deploy multiple serving containers on a single endpoint.
   - **Use Cases**: Inference pipelines or direct invocation of different algorithm models.
   - **Advantages**: Host different algorithms on one instance, reduce infrastructure costs.
   - **Limitations**: 
     - Shared resources among containers.
     - Possible cross interference.
     - Instance type considerations.
     - Maximum of five containers co-hosted.

#### Summary
- **Customizable Deployment**: Options cater to various use cases.
- **Single Model Endpoint**: Simple but with potential single point of failure.
- **Multiple Production Variants**: Good for A/B testing, with traffic control.
- **Multimodal Endpoint**: Cost-efficient for models using the same algorithm.
- **Multi-Container Endpoint**: Versatile, suitable for diverse algorithms and inference pipelines.
- **Certification Relevance**: Understanding these options is crucial for certification exams.

# 107. Lab - A/B Testing Multiple Production Variants

#### Scenario
- **Objective**: Compare XGBoost versions 0.9 and 1.2 for migration consideration.
- **Approach**: Deploy both models to the same endpoint for A/B testing with a 50/50 traffic split.

#### Steps

1. **Prepare & Train Models**
   - Download code from GitHub (`XGBoost` folder, `bike sharing regression` notebook).
   - Import libraries, upload data to S3.
   - Use spot instances for cost efficiency (toggle off if still on SageMaker trial).
   - Run `fit model` method for each XGBoost version (0.9 and 1.2) and compare RMSE scores.

2. **Create SageMaker Models**
   - Go to SageMaker console → Training jobs.
   - Select job for each version and create models (ensure correct XGBoost versions and S3 paths).

3. **Create Endpoint Configuration**
   - Add both models to the configuration.
   - Set initial instance type to `m5.large`.
   - Assign equal initial weight (1) to each model for a 50/50 traffic distribution.

4. **Deploy Endpoint**
   - Create an endpoint using the new configuration.
   - Monitor for 'In Service' status.

5. **Endpoint Management**
   - Review production variants, adjust weights if necessary.
   - Configure auto-scaling based on the variant invocation per instance metric.

6. **Invoke Endpoint for A/B Testing**
   - Use the `multi version predictions` notebook.
   - Set endpoint name, predictor instance, and optionally specify target variant.
   - Compare results for different versions.

7. **Analysis & Cleanup**
   - Predict rentals for all test rows, compare descriptive statistics.
   - Delete endpoint to avoid ongoing charges.

#### Observations
- Predicted values are identical across both XGBoost versions, indicating no impact on predictive quality with version migration.

#### Additional Notes
- The lab demonstrates the deployment of different algorithm versions.
- Can be extended to mix and match other algorithms (e.g., Linear Model, DeepAR).
- Each algorithm/model runs in its own instance, allowing for diverse combinations.

# 108. Lab – Multi-model Endpoint

#### Scenario
- **Objective**: Efficiently utilize instances by deploying multiple models using a shared container.
- **Context**: Deploy two XGBoost models with different hyperparameters on a multimodal endpoint for flexibility and cost reduction.

#### Steps

1. **Prepare & Train Models**
   - Navigate to `XGBoost` folder and open `bike sharing regression` notebook.
   - Import libraries, upload data to S3.
   - Define `fit model` method with job suffix and hyperparameters.
   - Train two models with different hyperparameters (more complex model with increased depth and rounds).

2. **Compare RMSE Metrics**
   - Model 1: Train RMSE = 0.23, Validation RMSE = 0.28.
   - Model 2: Train RMSE = 0.12, Validation RMSE = 0.28.

3. **Create SageMaker Model**
   - In SageMaker console, select the first training job (with `hyper1`).
   - Choose "Use multiple models" option.
   - Set model artifact location to the `model` folder in S3.
   - Create the model.

4. **Create Endpoint Configuration**
   - Name: `xboost-bikerental-hyper`.
   - Select the created model.
   - Choose `ml.m5.large` instance type.

5. **Deploy Endpoint**
   - Name: `xgboost-bikerental-hyper`.
   - Use the created endpoint configuration.
   - Wait until the endpoint status is 'In Service'.

6. **Invoke Multimodal Endpoint**
   - Open `multiple model prediction` notebook.
   - Update `target_models` list with model folder names in S3.
   - Create a predictor instance.
   - Specify target model in `predict` method.
   - Observe increased latency on first calls to each model (due to model artifact loading).

7. **Generate Predictions & Compare**
   - Run predictions for the entire test dataset.
   - Compare descriptive statistics to see differences in predicted values.
   - Determine model performance based on metrics like RMSE or RMSLE.

8. **Cleanup**
   - Delete the endpoint to avoid ongoing charges.

#### Summary
- Multimodal endpoints allow hosting multiple models with a shared serving container, reducing deployment costs and offering flexibility.
- Models must be trained using the same algorithm for compatibility with the shared container.
- Ideal for rapid deployment of new model versions without additional instance setup.
- Note: Increased latency on initial calls due to on-demand model artifact loading from S3.

# 109. Run Models at the Edge

#### SageMaker Neo
- **Purpose**: For latency-sensitive and streaming data analysis use cases, SageMaker Neo enables hosting ML models close to the data source.
- **Supported Use Cases**: Ideal for scenarios like issue detection in manufacturing plants, processing sensor data in autonomous vehicles, etc.
- **Functionality**: Neo compiles a trained model into an executable for edge devices.
- **Hardware Compatibility**: Supports Intel, NVIDIA, ARM, Cadence, Qualcomm, and Xilinx architectures.
- **Supported Models**: Compatible with MXNet, TensorFlow, PyTorch, and XGBoost models trained via Amazon SageMaker.

#### Benefits of SageMaker Neo
1. **Performance Improvement**: Up to 2X increase in performance without sacrificing accuracy.
2. **Framework Size Reduction**: Can achieve up to a 10X reduction. Neo compiles both the model and framework into a single executable for edge deployment.
3. **Cross-Platform Compatibility**: Run the same ML model across multiple hardware platforms.

#### AWS IoT Greengrass
- **Role**: Extends AWS capabilities to edge devices, enabling local execution of functions, containers, and ML model predictions.
- **Key Features**: 
   - Runs Lambda functions and Docker containers locally.
   - Executes predictions using ML models offline.
- **Integration with Neo**: 
   - Models compiled with SageMaker Neo are placed in S3.
   - Install GreenGrass and DLR (Deep Learning Runtime) on the edge device.
   - Configure Greengrass to point to the model in S3.
   - Greengrass downloads and hosts the model locally for inference.
