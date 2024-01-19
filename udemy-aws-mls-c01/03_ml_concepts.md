# 23. Introduction to Machine Learning, Concepts, Terminologies

### 1. Types of Learning Algorithms

   - **Supervised Learning**: 
     - Input data and correct answers are provided.
     - Example: Classifying Iris plant types based on measurements.
   - **Unsupervised Learning**: 
     - No specific target for prediction.
     - Used for grouping, anomaly detection, and dimensionality reduction.
   - **Reinforcement Learning**: 
     - Decision-making under uncertainty, using rewards or penalties.
     - Supported by SageMaker.

### 2. Supervised Learning

   - **Data Splitting**:
     - Labeled data is split into a training set (70%) and a test set (30%).
     - Shuffling data before splitting is crucial.
   - **Algorithm Types**:
     - **Regression**: Predicts a numeric output.
     - **Binary Classification**: Predicts one of two possible outcomes.
     - **Multi-class Classification**: Predicts one of several possible outcomes.

### 3. Unsupervised Learning

   - **Applications**:
     - Grouping similar observations.
     - Anomaly detection.
     - Feature reduction (e.g., PCA).
     - Finding similar words (e.g., BlazingText, FastText).

### 4. Reinforcement Learning
   - Used for scenarios like autonomous driving and strategy games.
   - Involves learning from a mix of examples and uncertainties.

# 24. Data Types - How to handle mixed data types

### Categorical Values
- **Encoding**: Convert text-based categories to numeric form for tree-based algorithms like XGBoost.
- **One-hot Encoding**: Used for algorithms like Linear Regression, converting categories into separate columns.
- **Feature Combination**: Combine features to form new ones for capturing non-linear relationships.

### Text Data
- **Bag-of-Words**: Tokenize text into words; each word becomes a feature.
- **NGram Transformation**: Capture contiguous sequences of words to better represent meaning.
- **OSB Transformation**: Similar to NGrams, but includes non-contiguous word combinations.
- **Stemming**: Reduce words to their root form for consistency.
- **Case Uniformity**: Convert all text to either lowercase or uppercase.
- **Punctuation Removal**: Improve signal by removing punctuations.

### Numeric Data
- **As-is Usage**: Suitable for linear relationships.
- **Normalization**: Adjust features to similar scales to prevent dominance of larger scale features.
- **Binning**: Segment numeric values into bins for capturing non-linearity.

