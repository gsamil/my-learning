# Model Optimization and Hyperparameter Tuning

## Introduction to Hyperparameter Tuning (Lesson 148)

- Hyperparameters are tunable parameters that influence how a machine learning algorithm learns from data.

### Challenges in Hyperparameter Tuning
- Requires training a new model for each hyperparameter combination.
- Algorithms have multiple hyperparameters, each with a wide range of possible values.
- Changing one hyperparameter might necessitate adjustments in others.

### SageMaker's Automatic Hyperparameter Tuning
- **Process**:
  1. **Input**: Provide dataset and select the machine learning algorithm.
  2. **Hyperparameter Range**: Define the hyperparameters and their value ranges to be searched.
  3. **Optimization Objective**: Set a goal, such as minimizing test RMSE for regression or improving AUC for classification.
  4. **Training Jobs**: SageMaker runs multiple jobs with varied hyperparameter combinations.
  5. **Selection**: Chooses the best-performing hyperparameter configuration.

- **Search Strategies**:
  - **Random Search**: Picks random combinations within specified ranges.
  - **Bayesian Search**: Treats tuning as a regression problem, using results from initial jobs to inform subsequent selections.

- **Sagemaker Hyperparameter tuning jobs**
- You can clone a previous job and change the hyperparameters to refine the search space.

## Nuts and Bolts of Optimization (Lesson 152)

The Nuts and Bolts of Optimization is an important topic for the certification exam and optimizing your models.

### Common Strategies When Model Performance is Suboptimal
- Collect more data.
- Train longer.
- Hyperparameter optimization.
- Use a different algorithm or architecture.
- Implement regularization.
- Utilize a bigger model.

### Example: Human-Level Speech Recognition System
- **Goal**: Achieve human-level performance.
- **Dataset Management**: 70% for training, 15% each for validation and testing.
- **Metrics**: Human-level error, training error, validation error.

### Scenarios and Solutions

#### Scenario 1: High Bias
- **Metrics**: Human-level error = 1%, Training error = 5%, Validation error = 6%.
- **Problem**: Model underperforms compared to human-level (high-bias, underfitting).
- **Solutions**: Train a bigger model, train longer, try new model architecture.

#### Scenario 2: High Variance
- **Metrics**: Human-level error = 1%, Training error = 2%, Validation error = 6%.
- **Problem**: Overfitting (high-variance).
- **Solutions**: Add regularization, implement early stopping, get more data, try new model architecture.

#### Scenario 3: High Bias and High Variance
- **Metrics**: Human-level error = 1%, Training error = 5%, Validation error = 10%.
- **Problem**: Model underperforms significantly, showing both high bias and variance.

#### Scenario 4: Training/Test Data Distribution Mismatch
- **Metrics**: Human-level error = 1%, Training error = 5%, Validation error = 6%, Test error = 10%.
- **Problem**: Performance discrepancy due to different data distributions.
- **Solution**: Ensure validation and test sets come from the same distribution.

### Human-Level Performance
- **Medical Example**: Error rates from typical human to a team of expert doctors.
- **Optimal Error Rate**: Team of expert doctors as a benchmark for human-level performance.

### Workflow
- Implement a systematic workflow to address various performance issues.

### Data Synthesis
- **OCR System Example**: Generating synthetic data using random pictures and software like MS Word.
- **Speech Recognition Example**: Mixing clean audio with random background sounds for new data.

### Unified Data Warehouse/Data Lake
- Facilitates smoother data access and efficient progress.
- Consider user access rights and privacy.

### Key Takeaways
- Selection of the right optimization strategy is crucial for rapid progress.
- Balancing high bias and high variance is key to building effective models.
- Data synthesis can be a powerful tool in improving model performance.
- Unified data management systems enhance team efficiency and data accessibility.
