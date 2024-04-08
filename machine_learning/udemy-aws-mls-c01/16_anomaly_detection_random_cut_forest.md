# Anomaly Detection with Random Cut Forest

## Introduction to Random Cut Forest and Intuition Behind Anomaly Detection (Lesson 167)

- Random Cut Forest (RCF) is a SageMaker built-in algorithm designed for anomaly detection.
- It's an unsupervised Algorithm. Automatically differentiates outliers and anomalous data points without explicit labeling.
- Also Suitable for time series data and adaptable to the evolving definition of normal behavior.
- Output is an anomaly score for each input, with higher scores indicating potential anomalies.

### Use Cases
- **Traffic Analysis**: Distinguishing between normal rush hour traffic and anomalies like accidents.
- **Cybersecurity**: Identifying distributed denial of service (DDoS) attacks or unusual large-scale data transfers.

### Algorithm Explained
- It's very similar to the Isolation Forest algorithm.
- **Decision Tree-Based Ensemble Method**: Utilizes a forest of trees for decision-making.
- **Anomaly Scoring**: Points closer to the root of the trees are considered more anomalous.
- **Overfitting Strategy**: Intentionally overfits to isolate anomalous points in fewer splits.
- **Handling New Data**: Allocates patterns to cover gaps, aiding in classifying new data points as normal or anomalous.
- RCF uses reservoir sampling to draw random samples from large datasets.

### Training and Inference
- **Training Data Formats**: Accepts CSV and RecordIO formats.
- **Inference Formats**: Supports JSON, CSV, or RecordIO.
- **Test Data Labels**: Optional. Uses labels (1 for anomalous, 0 for normal) to compute classification metrics.

### RCF Hyperparameters
- **feature_dim**: Specifies the number of features in the dataset.
- **num_trees**: Determines the quantity of trees in the forest.
- **num_samples_per_tree**: Controls the number of random training samples provided to each tree.
- **eval_metrics**: Test data evaluation metrics, including precision, recall, and F1 score.
- **Tunable Parameters**: Number of trees and samples per tree can be optimized using hyperparameter tuning.

### Understanding Anomaly Scores
- **Threshold Setting**: Based on application sensitivity, a threshold distinguishes normal from anomalous.
- **Three Sigma Rule**: A starting point for approximately normal datasets, considering scores above three standard deviations as anomalous.
