# Principal Component Analysis (PCA)

## Introduction to Principal Component Analysis (PCA) (Lesson 129)

- PCA transforms a dataset with many features into a dataset with fewer, new features.
- PCA components are less interpretable compared to original features.
-  Only works with numeric continuous data, not suitable for categorical values.
-  Data should be normalized for PCA to be effective.

### SageMaker PCA Details
- **Modes in SageMaker**:
  - **Regular Mode**: For sparse and moderate-sized datasets.
  - **Random Mode**: For very large datasets, using an approximation algorithm.
- **Data Formats**:
  - **Training Data**: CSV and protobuf RecordIO.
  - **Inference Data**: CSV, JSON, protobuf RecordIO.
