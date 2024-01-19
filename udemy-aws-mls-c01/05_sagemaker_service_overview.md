# 49. How is AWS SageMaker different from other ML frameworks?

### Overview of SageMaker
- SageMaker is a cloud service that leverages AWS resources for training and hosting machine learning models.

### Key Differences from Direct Framework Usage
1. **Framework Installation**:
   - Traditional ML frameworks like SKLearn, TensorFlow, or PyTorch can be installed and used locally on a laptop.
   - SageMaker, being cloud-based, requires the use of AWS resources.

2. **Production Application**:
   - Converting local ML models into production applications often requires additional tools or cloud services.
   - SageMaker simplifies this process, making it more straightforward to transition models to production.

3. **Cost and Trial Period**:
   - Using SageMaker involves some cost, but it offers a two-month free trial for getting started.

4. **Containers and Built-in Algorithms**:
   - SageMaker utilizes containers to encapsulate algorithms and frameworks.
   - Provides containers for built-in algorithms (XGBoost, DeepAR, FM, etc.) and popular frameworks (PyTorch, SKLearn, TensorFlow).

5. **Training Parameters**:
   - Requires specifying training parameters like data location (S3 or EFS), hyperparameters, server type for training, and storage location for trained artifacts.

6. **Script File for Frameworks**:
   - In addition to training parameters, frameworks on SageMaker require a script file.
   - This script includes the model-building code specific to PyTorch, TensorFlow, or SKLearn.

7. **Hosting Models**:
   - Post-training, models can be hosted on SageMaker for deployment.
   - SageMaker's containerized approach offers a standardized interface for building and deploying models across different algorithms and frameworks.

### Conclusion
- SageMaker stands out in its ability to streamline the transition from model training to production deployment, backed by AWS's robust cloud infrastructure.

# 50. Introduction to SageMaker

### Key Capabilities
1. **Jupyter Notebook Environment**:
   - Managed Jupyter notebook instances for development and data preparation.
   - Automated Python installation and patch application.
   - Custom Python packages installation supported.

2. **Machine Learning Algorithm Support**:
   - Wide variety of optimized ML algorithms for AWS Cloud.
   - Optimized environments for frameworks like TensorFlow, Apache MxNet.
   - Custom algorithm deployment capability.

3. **Training Infrastructure**:
   - Scalable training on one or multiple compute instances.
   - Handles large datasets, with trained model artifacts stored in S3.

4. **Model Deployment**:
   - Real-time prediction support with load-balanced compute instances.
   - Auto-scaling for instance management and workload adaptation.
   - Batch transform for non-interactive, large-scale inference tasks.

### Deployment Options
- **Real-time Prediction**:
  - Persistent endpoint for client application model invocations.
  - Auto-replacement of instances in case of hardware/system issues.
  - Customizable scaling policies based on workload.

- **Batch Transform**:
  - Ideal for non-interactive, large dataset inference.
  - Manages resource allocation, dataset processing, and results storage.
  - Terminates instances post-processing, enhancing cost-effectiveness.

### Summary
- SageMaker offers a comprehensive suite of services for building, training, and deploying ML models in the cloud.
- Features include a fully managed development environment, extensive algorithm and framework support, scalable training infrastructure, and flexible deployment options for real-time and batch processing.

# 51. Instance Type and Pricing

### Instance Families
1. **Standard Instances**:
   - Low-cost, balanced performance and memory.
   - T2, T3 (occasional burst utilization), M5 (sustained load) instances.

2. **Compute Optimized Instances**:
   - High-performance CPUs for CPU-intensive tasks.
   - C4, C5 instance types.

3. **Accelerated Computing Instances**:
   - Powerful GPUs for GPU-optimized algorithms.
   - P2, P3 instances for faster training and GPU-enabled hosting.

4. **Inference Acceleration**:
   - Fractional GPU capabilities as an add-on to other instances.
   - Suitable for models needing partial GPU support in inference.

### Choosing Instances
- Based on algorithm requirements: CPU-bound or GPU-bound.
- Experiment with instance sizes for optimal performance and cost.
- Instance naming: `ML.<instance type>.<generation>.<size>` (e.g., ML.C5.2xlarge).

### Pricing Components
- **Instance Cost**: Varies by type and size.
- **Variable Costs**: Depends on fractional GPUs, storage allocated, and data transfer.
- **Region-Specific Pricing**: Slight variations between AWS regions.

### Free-Tier Offer (for New Users)
- **Development**: T2/T3 medium notebook instances - 250 hours/month.
- **Training**: M4/M5 extra-large instances - 50 hours/month.
- **Hosting**: M4/M5 extra-large instances - 125 hours/month.

### Beyond Free-Tier
- **Development (Example)**:
  - T3 extra-large instance: $0.23/hour.
  - Storage: $0.14/GB/month.
  - Data Transfer: $0.016/GB (in/out).
- **Training Costs**: Based on instance runtime and storage during training.
- **Hosting Options**:
  - **Real-time Hosting**: Cost depends on instance type, GPUs, storage, data transfer.
  - **Batch Transform**: Charges for job duration, suitable for non-interactive tasks.

### Summary
SageMaker provides a range of instance options catering to various ML requirements, with pricing involving multiple components. Users can choose instances based on their algorithm's needs and manage costs effectively by right-sizing and using the free-tier benefits.

# 52. Save Money on SageMaker Usage

### 1. SageMaker Savings Plan
- **Overview**: Offers up to 64% discount over on-demand pricing for consistent usage.
- **Commitment**: Choose a 1-year or 3-year term with a fixed $/hour usage.
- **Applicability**: Applies to SageMaker Notebook, Studio, Training, Real-time Inference, Batch Transform, Data Wrangler, etc.
- **Global Benefit**: Discounts apply across regions, instance families, and sizes.
- **Challenges**:
  - Determining steady-state usage: Use AWS Cost Explorer to analyze and recommend plans.
  - Fluctuating Usage: Billing based on hourly usage, not monthly aggregate. Unused hours may not carry over.
- **Example**: Convert a $10/hour steady-state usage to a $4/hour savings plan to reduce monthly charges from $7,200 to $2,880.
- **Resource**: [SageMaker Savings Plan Announcement](https://aws.amazon.com/about-aws/whats-new/2021/04/amazon-sagemaker-announces-a-price-reduction-in-instances-and-sagemaker-savings-plan/)

### 2. Managed Spot Training
- **Discounts**: Up to 90% off on AWS's unused capacity.
- **Use Case**: Ideal for training and automatic model tuning jobs (not for inference).
- **Handling Interruptions**: SageMaker automatically manages spot instance interruptions and resumes training when capacity is available.
- **No Long-term Commitment**: Flexible and cost-effective for training and tuning.
- **Resource**: [Managed Spot Training Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html)

### 3. Learning with SageMaker
- **Two-Month Trial**: Ideal for learners, providing free-tier instance types.
- **Beyond Free-Tier**: Managed spot training is recommended for cost savings.
- **Multiple Accounts for Extended Trial**: Sign up with different email IDs for additional two-month trial periods (albeit cumbersome).

By utilizing these methods, users can significantly reduce their AWS SageMaker costs while maintaining efficient machine learning operations.

Also refer to the [CloudPractitionerReview-InfraPricingSupport.pdf](./CloudPractitionerReview-InfraPricingSupport.pdf). This review material provides a quick overview of important concepts related to infrastructure, pricing, support plans, and shared responsibility model in the cloud

# 53. Data Format

### Supported Data Formats
- **Common Formats**: CSV and RecordIO (protobuf)
- **Other Formats**: Some SageMaker algorithms also support LibSVM, JSON, and Parquet formats.

### Storage and Retrieval
- **Storage Location**: Data for training and validation must be stored in an Amazon S3 bucket.
- **Data Access**:
  - Single File: If a single file in S3 is specified, its contents are used for training.
  - Folder: If a folder is specified, all data within that folder is used for training.

### Usage of Channels
- **Train Channel**: For the training dataset.
- **Test Channel**: For the evaluation dataset.

### Data Transfer Modes
1. **File Mode**:
   - Entire data from S3 is copied to training instance volumes.
   - Requires enough disk space on training instances for the full dataset and model artifacts.
2. **Pipe Mode**:
   - Streams data from S3 to training instances.
   - Faster start times and better throughput.
   - Reduces storage needs on training instances.

### Hands-On Lab: Data Format Exploration
- **Objective**: Create a dataset in CSV and RecordIO formats, upload to S3, and download from S3.
- **Tools Used**: Pandas, NumPy, Boto3, SageMaker library.
- **Process**:
  - Create a dataset with 3 input features (X1, X2, X3) and a binary target variable (Y).
  - Convert the dataset to CSV using Pandas `to_csv` method.
  - Upload the CSV file to S3 using the `write_to_s3` helper function.
  - Use `write_numpy_to_dense_tensor` method from SageMaker library to create a RecordIO formatted file.
  - Upload and download RecordIO file to/from S3.

### Summary
- SageMaker supports multiple data formats for efficient training and prediction.
- The choice of data format (CSV, RecordIO, others) depends on algorithm compatibility and dataset size.
- Data must be stored in S3, with training and validation data distinguished via channels.
- File and Pipe modes offer different approaches to data transfer from S3 to training instances.
- Practically, users can create, upload, and manage these data formats using SageMaker's integrated tools and AWS libraries.

# 54. SageMaker Built-in Algorithms

AWS SageMaker provides a range of built-in algorithms optimized for cloud-based machine learning. These algorithms can be broadly categorized based on their applications:

### Text Data Algorithms
1. **BlazingText**:
   - Modes: Unsupervised (Word2Vec) and supervised.
   - Use: Converts text to vector, grouping semantically similar words. Useful for text classification.

2. **Object2Vec**:
   - Type: Supervised.
   - Use: Converts text to vector while capturing sentence structure. Suitable for associating customers with products, movies with ratings, etc.

### Recommender Systems and Collaborative Filtering
1. **Factorization Machines**:
   - Type: Suitable for high-dimensional sparse datasets.
   - Use: Popular for building recommender systems and collaborative filtering.

### Classification and Regression
1. **K-Nearest Neighbor (KNN)**:
   - Use: Simple, effective for classification (majority class of k-nearest neighbors) and regression (average value of k-nearest neighbors).

2. **Linear Models**:
   - Types: Linear regression, logistic regression, multinomial logistic regression.

3. **XGBoost**:
   - Use: Gradient boosted tree algorithm for both regression and classification.

### Time Series Forecasting
1. **DeepAR**:
   - Use: Trains on multiple time series, predicts new similar series.

### Image Analysis
1. **Object Detection**:
   - Use: Detects and classifies objects in images, provides bounding boxes.

2. **ImageClassification**:
   - Use: Multi-label classification of images.

3. **Semantic Segmentation**:
   - Use: Tags each pixel in an image with a class label, useful in computer vision.

### Language Processing
1. **Sequence to Sequence**:
   - Use: Useful for text summarization, language translation, speech to text.

### Clustering and Topic Modeling
1. **K Means**:
   - Type: Unsupervised clustering algorithm.

2. **LDA (Latent Dirichlet Allocation)**:
   - Use: Groups documents based on topics.

3. **Neural Topic Modeling**:
   - Use: Similar to LDA, for document grouping by topics.

### Dimensionality Reduction
1. **PCA (Principal Component Analysis)**:
   - Use: Reduces dataset dimensions while retaining information.

### Anomaly Detection
1. **Random Cut Forest**:
   - Use: Detects anomalies in data, assigns scores to points.

2. **IP Insights**:
   - Use: Detects unusual network activity, useful for security applications.

### Summary
- SageMaker's built-in algorithms cover a wide range of ML applications.
- They are optimized for AWS cloud, offering scalability and GPU training advantages.
- Users can choose the appropriate algorithm based on their data and use case requirements.

# 55. Popular Frameworks and Bring Your Own Algorithm

### SageMaker Ground Truth
- **Purpose**: Assists in labeling data for machine learning.
- **Capabilities**:
  1. **Automatic Labeling**: Uses provided examples to label remaining data.
  2. **Human Labeling**: Distributes labeling tasks to human labelers via integration with Mechanical Turk, managing the workflow.

### SageMaker Neo
- **Functionality**: Optimizes machine learning models for deployment across cloud and edge locations.
- **Key Features**:
  - **Cross-Compilation**: Converts and optimizes models for various hardware like Intel, Nvidia, ARM.
  - **Use Case**: Suitable for applications where low latency is crucial, allowing deployment at edge locations.

### Developing Models with Other Frameworks
- **Container-Based Architecture**: Utilizes Docker containers for training and deploying models.
- **Pre-Built Docker Images**: Available for built-in algorithms and popular frameworks like TensorFlow, Apache MxNet, etc.
- **Integration with Apache Spark**: 
  - Provides a library for Python and Scala.
  - Directly consumes data frames in Spark clusters, converting them to protobuf and uploading to S3.
- **Framework Support**: Offers support for TensorFlow, Apache MxNet, Scikit-learn, PyTorch, Chainer, etc.
- **Custom Algorithm Development**:
  - Option to extend SageMaker Docker images or use custom container images.
  - Suitable for unique runtime or language requirements.
- **Advanced Use with Deep Learning AMIs**: 
  - For modifying or extending frameworks.
  - Ideal for users contributing to code or debugging at the framework level.

### Summary
SageMaker provides a flexible environment for machine learning, offering:
- Built-in algorithms for ease of use and scalability.
- Support for popular frameworks via pre-built container images.
- Options to extend or bring custom container images for unique requirements.
- Ground Truth for data labeling and Neo for optimizing model deployment.

