# 167. Introduction to Random Cut Forest and Intuition Behind Anomaly Detection

## Introduction to RCF
- **Definition**: Random Cut Forest (RCF) is a SageMaker built-in algorithm designed for anomaly detection.
- **Unsupervised Algorithm**: Automatically differentiates outliers and anomalous data points without explicit labeling.
- **Applicability**: Suitable for time series data and adaptable to the evolving definition of normal behavior.

## Anomaly Definition and Detection
- **Anomaly**: Deviation from normal behavior.
- **Output**: Anomaly score for each input, with higher scores indicating potential anomalies.

## Use Cases
- **Traffic Analysis**: Distinguishing between normal rush hour traffic and anomalies like accidents.
- **Cybersecurity**: Identifying distributed denial of service attacks or unusual large-scale data transfers.

## Algorithm Explained
- **Decision Tree-Based Ensemble Method**: Utilizes a forest of trees for decision-making.
- **Anomaly Scoring**: Points closer to the root of the trees are considered more anomalous.
- **Overfitting Strategy**: Intentionally overfits to isolate anomalous points in fewer splits.
- **Handling New Data**: Allocates patterns to cover gaps, aiding in classifying new data points as normal or anomalous.

## Training and Inference
- **Training Data Formats**: Accepts CSV and RecordIO formats.
- **Inference Formats**: Supports JSON, CSV, or RecordIO.
- **Test Data Labels**: Optional. Uses labels (1 for anomalous, 0 for normal) to compute classification metrics.

## RCF Hyperparameters
- **Feature Dimension (`feature_dim`)**: Specifies the number of features in the dataset.
- **Number of Trees**: Determines the quantity of trees in the forest.
- **Samples per Tree**: Controls the number of random training samples provided to each tree.
- **Tunable Parameters**: Number of trees and samples per tree can be optimized using hyperparameter tuning.

## Understanding Anomaly Scores
- **Threshold Setting**: Based on application sensitivity, a threshold distinguishes normal from anomalous.
- **Three Sigma Rule**: A starting point for approximately normal datasets, considering scores above three standard deviations as anomalous.

## Conclusion
- RCF is an effective tool for anomaly detection in various scenarios, using a tree-based method to classify data points.
- The algorithm's effectiveness relies on its ability to isolate anomalies with minimal splits and overfitting to ensure accurate detection.
