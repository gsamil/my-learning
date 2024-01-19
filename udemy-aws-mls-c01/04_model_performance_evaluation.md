# 34. Introduction

### Overview
- AWS documentation provides concise information on model performance evaluation.
- Understanding model evaluation is crucial for improving predictive quality.

### Supervised Learning: Data Split
- **Training Set**: Used for model training.
- **Test Set**: Used for verifying model performance with unseen data.

### Objective
- Determine if the model is underfitting, overfitting, or well-balanced.

### Model Issues
- **Underfitting**: 
  - Poor performance on both training and test sets.
  - Solved by adding features, examples, or optimizing hyperparameters.
- **Overfitting**: 
  - Good performance on training but poor on test set.
  - Solved by simplifying model or optimizing hyperparameters.

### Performance Metrics
- Vary based on output type: continuous (regression), binary, or categorical (classification).

# 35. Regression Model Performance

### Techniques for Comparison
- **Visual Comparison**: Using plots to compare actual and predicted values.
- **Residual Distribution**: Histograms showing the difference between actual and predicted values.
- **Root Mean Square Error (RMSE)**: Common metric for assessing accuracy.

### Hands-On Exercise
- **Dataset**: Airline passenger data set from the World Bank.
- **Objective**: Compare performance of four different prediction models.
- **Data Attributes**: Year, GDP, population (input), passengers (target), model predictions.

### Steps for Evaluation
1. **Plot Data**: Visualize actual vs. predicted values for each model.
2. **Compute RMSE**: 
   - Square the difference between actual and predicted values.
   - Calculate the mean of these squared differences.
   - Find the square root of this mean to get RMSE.
3. **Analyze Residual Histogram**:
   - Residual is actual minus predicted value.
   - Balanced models should have residuals centered around zero.
   - Skewed distributions indicate over or under-prediction.

### RMSE Calculation
- Use `mean_squared_error` method from SKLearn and compute square root for RMSE.
- Compare RMSE values across models to assess accuracy.

# 36. Binary Classifier Performance

### Understanding Positive and Negative Classes
- **Positive Class**: Condition algorithm aims to detect.
- **Negative Class**: Normal or default condition.
- **Examples**:
  - College Admission: Positive = Admitted, Negative = Not-Admitted.
  - Heart Disease Risk: Positive = At Risk, Negative = Normal.
  - Email Spam: Positive = Spam, Negative = Normal Email.

### Binary Output vs. Raw Score
- Some classifiers directly produce binary output.
- Others give a probability score, requiring a cutoff threshold for classification.

### Evaluation Techniques - Part 1
- **Visual Comparison**: Plots comparing actual vs. predicted binary values.
- **Confusion Matrix**: Visual tool to assess model performance.
- **Metrics**: Recall, precision, accuracy, etc., for quantitative assessment.

### Hands-On Exercise
- **Dataset**: Exam result dataset correlating study hours with pass/fail outcome.
- **Objective**: Compare performance of four models predicting exam outcomes.
- **Plots for Comparison**:
  - **Model 1**: Misclassifies fails as passes based on study hours.
  - **Model 2**: Classifies all as fails.
  - **Model 3**: Pass for >= 3 hours of study, else fail.
  - **Model 4**: Classifies all as passes.
- **Initial Observations**:
  - Model 2 and 4 show extreme bias.
  - Model 1 and 3 need further evaluation for better model selection.

## Building a Confusion Matrix for Classifier Performance

### Example: Building the Matrix
- **Data Attributes**: Hours, actual pass/fail, and model predictions.
- **Counts**:
  - Total samples: 20 (10 pass, 10 fail).
  - Model Predictions: 15 pass, 5 fail.

### Confusion Matrix Categories
1. **True Positive (TP)**: Positives correctly predicted.
2. **True Negative (TN)**: Negatives correctly predicted.
3. **False Negative (FN)**: Positives misclassified as negative.
4. **False Positive (FP)**: Negatives misclassified as positive.

### Calculating Categories
- **TP**: Count of actual = 1 and predicted = 1.
- **TN**: Count of actual = 0 and predicted = 0.
- **FN**: Count of actual = 1 and predicted = 0.
- **FP**: Count of actual = 0 and predicted = 1.

### Sample Calculation
- For a given model:
  - TP = 10 (correctly classified all positives).
  - TN = 5.
  - FN = 0 (no misclassification of positives).
  - FP = 5 (misclassified 5 negatives).

### Summary
- **Rows**: Actual labels.
- **Columns**: Predicted labels.
- **Fractional View**: Divide row count by actual class count for rates (e.g., true positive rate).

### Interpretation
- Model correctly classifies 100% positives and 50% negatives.
- Misclassifies 50% negatives as positives.

# 39. Binary Classifier - Metrics Definition

### Definitions of Key Metrics
1. **True Positive Rate (TPR)**:
   - Also known as **Recall** or **Probability of Detection**.
   - Measures correctly classified positives.
   - Closer to 1 indicates better performance.

2. **True Negative Rate (TNR)**:
   - Probability of correctly classifying negatives.
   - Higher values indicate better performance.

3. **False Positive Rate (FPR)**:
   - Also known as **Probability of False Alarm**.
   - Measures negatives misclassified as positives.
   - Should be close to 0 for good performance.

4. **False Negative Rate (FNR)**:
   - Probability of misclassifying positives as negative.
   - Lower values indicate better performance.

5. **Precision**:
   - Measures the accuracy of positive predictions.
   - Higher precision means fewer false positives.

6. **Accuracy**:
   - Overall performance metric.
   - Measures both positives and negatives correctly classified.

7. **F1 Score**:
   - Harmonic mean of precision and recall.
   - Balances the trade-off between precision and recall.

### Interpretation
- **Recall (TPR)**: Good at identifying actual positives.
- **Precision**: Effectiveness in classifying positives while avoiding misclassifying negatives.
- **Accuracy**: General effectiveness across all classifications.
- **F1 Score**: Balance between precision and recall, useful for uneven class distribution.

# 42. Binary Classifier - Area Under Curve Metrics

### Understanding Cutoff Threshold
- Models produce raw scores between 0 and 1, requiring a cutoff for classification.
- Common to use 0.5 as a threshold.
- Threshold can be adjusted based on specific problem requirements.

### Evaluating with Raw Scores
- **Visual Observation**: Plot raw scores and observe classification at different thresholds.
- **Area Under Curve (AUC)**: Measures model performance across various thresholds.
  - Higher AUC indicates superior performance.
  - AUC close to 0.5 suggests random guessing.

# 43. Lab - Multiclass Classifier

### Multi-Class Classification
- Predicts one of many possible outcomes (e.g., grades A, B, C, etc.).

### Evaluation Techniques
- **Visual Observation**: Plots to compare actual and predicted values.
- **Confusion Matrix**: Extended to accommodate multiple classes.
- **Metrics**: Recall, precision, and F1 score for each class, averaged for overall model performance.

### Hands-On Exercise
- **Dataset**: Iris classification dataset with three plant types.
- **Objective**: Compare four models’ performance in classifying plant types.
- **Confusion Matrix Construction**:
  - Rows for actual labels (Setosa, Versicolor, Virginica).
  - Columns for predicted labels.
  - Fractional representation for class-wise classification rates.

### Model Metrics Comparison
- **Precision**: Measure of correctly identified positives in each class.
- **Recall**: True positive rate for each class.
- **F1 Score**: Harmonic mean of precision and recall for each class.
- **Averaging Strategies**:
  - **Macro Average**: Simple average, may not account for class imbalance.
  - **Weighted Average**: Accounts for the number of samples in each class.

