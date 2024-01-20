# 148. Introduction to Hyperparameter Tuning

## Introduction to Hyperparameters
- **Definition**: Hyperparameters are tunable parameters that influence how a machine learning algorithm learns from data.
- **Objective**: Customize the algorithm to improve prediction quality.

## Examples and Impact
- **XGBoost's Max Depth**: Controls tree depth, affecting complexity and potential overfitting.
- **Epochs and Learning Rate**: Number of passes over data and learning rate's impact on learning patterns, especially with small datasets or learning rates.

## Challenges in Hyperparameter Tuning
- **Time-Consuming**: Requires training a new model for each hyperparameter combination.
- **Variety and Range**: Algorithms have multiple hyperparameters, each with a wide range of possible values.
- **Interdependencies**: Changing one hyperparameter might necessitate adjustments in others.
- **Systematic Approach Requirement**: Essential for converging to an optimal set for a given dataset.

## SageMaker's Automatic Hyperparameter Tuning
- **Process**:
  1. **Input**: Provide dataset and select the machine learning algorithm.
  2. **Hyperparameter Range**: Define the hyperparameters and their value ranges to be searched.
  3. **Optimization Objective**: Set a goal, such as minimizing test RMSE for regression or improving AUC for classification.
  4. **Training Jobs**: SageMaker runs multiple jobs with varied hyperparameter combinations.
  5. **Selection**: Chooses the best-performing hyperparameter configuration.

- **Search Strategies**:
  - **Random Search**: Picks random combinations within specified ranges.
  - **Bayesian Search**: Treats tuning as a regression problem, using results from initial jobs to inform subsequent selections.

## Conclusion
- Hyperparameter tuning is critical for building optimized models.
- Manual tuning is time-consuming and complex.
- SageMaker offers an efficient, systematic approach for finding optimal hyperparameters.

# 149. Lab: Tuning Movie Rating Factorization Machine Recommender System

## Introduction
- **Objective**: Improve ratings predictions using the Factorization Machine algorithm on the movie ratings dataset.

## Context and Challenges
- **Dataset Change Impact**: With the updated movie dataset, the test RMSE score increased from 0.8 to 1.9, indicating degraded model performance.
- **Focus**: Tuning hyperparameters to enhance model performance.
- **Black Box Approach**: Treating the algorithm as a black box to focus on predictive quality improvement.

## Key Hyperparameters in Factorization Machines
- **Feature Dimension**: Number of features in the dataset.
- **Number of Factors**: Dimensionality of factorization; a non-tunable parameter, often set as per documentation.
- **Predictor Type**: 'Regressor' for predicting a movie rating.
- **Mini Batch Size & Epochs**: Affects the training process; initial values are 1000 and 100, respectively.
- **Learning Rates**: Three different learning rate parameters (`bias`, `factors`, `linear`), with a wide range of potential values.

## Tuning Process on SageMaker
1. **Initial Exploration**:
   - Set ranges for learning rate parameters and other hyperparameters.
   - Download and prepare the latest movie dataset.
   - Use SageMaker Notebook for dataset preparation and uploading to S3.
2. **Creating a Hyperparameter Tuning Job**:
   - Set up the job on AWS Console with SageMaker.
   - Choose algorithm, specify metric extraction patterns, and set training/test data paths.
   - Define search strategy (Bayesian) and optimization objective (minimize test RMSE score).
   - Configure hyperparameter search space, input data channels, and output path.
   - Set resource limits (instance type, storage size) and job parameters (number of jobs, parallel jobs).

## Results and Observations
- **Improved Performance**: Best training job achieved an RMSE score of 1.079, significantly better than the previous score of 1.9.
- **Sensitivity to Hyperparameters**: The algorithm showed sensitivity to learning rate parameters.
- **Stochastic Nature**: SageMaker's hyperparameter tuning is stochastic, leading to slightly different results in repeated runs.

## Conclusion
- Hyperparameter tuning in SageMaker offers an efficient way to improve model performance.
- Further improvement can be explored by adjusting the search space based on initial results.

## Next Steps
- The next lecture will delve into further tuning and adjustments based on the outcomes of this initial tuning exercise.

# 150. Lab: Step 2 Tuning Movie Rating Recommender System

## Recap of Previous Lab Results
- **Achievement**: Improved test RMSE score to 1.07 using hyperparameter tuning.
- **Objective**: Use best training job hyperparameters to refine the search space.

## Strategy for Refinement
- **Fixed Parameters**: Keep dataset-tied parameters constant (feature dimension, batch size, epochs, number of factors, predictor type).
- **Learning Rate Parameters**:
  - **Bias Parameter**: Search between 0.001 to 1.
  - **Linear and Factors Parameters**: Explore a range with lower values (ten times lower for the lowest value, and 100 times less for the highest value).

## Execution of Refined Tuning Job
- **Cloning Previous Job**: Adjust parameters from the previous job for the new tuning job.
- **Duration**: Approximately 2 hours for completion.

## Results of Refined Tuning
- **Improved RMSE Score**: Achieved a score of 0.93, indicating further improvement.
- **Smaller Learning Rates**: Indicative of the algorithm's sensitivity to these parameters.

## Deployment of the Refined Model
- **Model Creation**: Use the parameters from the best training job.
- **Endpoint Deployment**: Create and configure an endpoint for the model.
- **Endpoint Name**: e.g., `fm-movie-v5`.
- **Testing**: Verification using the prediction template showed a consistent RMSE of 0.93 and balanced residual histograms.

## Comparison with Random Search Strategy
- **Experiment**: Conducted a test using the same hyperparameter space with a random search strategy.
- **Outcome**: Best model produced a score of 2.35 with random search versus 1.07 with Bayesian search, suggesting the latter's systematic effectiveness.

## Conclusion
- Hyperparameter tuning for complex algorithms like Factorization Machines is challenging but crucial.
- SageMaker's hyperparameter tuning provides a systematic and automated approach to optimize hyperparameters.

# 151. HyperParameter, Bias-Variance, Regularization (L1, L2) [Repeat from XGBoost]

## Introduction
- **Purpose**: Hyperparameters fine-tune the learning process based on dataset complexity.
- **Defaults**: Algorithms usually have sensible default values as a starting point.

## Key Hyperparameters
- **Objective Hyperparameter**:
  - `reg:linear` for linear regression.
  - `binary:logistic` for binary classification.
  - `multi:softmax` for multiclass classification.
- **Number of Rounds**: Controls tree count. Too many can lead to overfitting.
- **Early Stopping**: Prevents overfitting by stopping training when validation loss stops improving.

## Bias and Variance
- **Bias**: Indicates underfitting when predictions don't match reality (high training and validation errors).
- **Variance**: High variance or overfitting occurs when training error is low, but validation error is high.

## Handling Bias and Variance
- **High Bias (Underfitting)**: Add/combine features, create complex/higher-order features, train longer, reduce regularization.
- **High Variance (Overfitting)**: Simplify model, use fewer features, reduce iterations, increase regularization.

## Regularization
- **Role**: Balances feature dependence, preventing over-reliance on specific features.
- **Types**:
  - **L1 Regularization**: Aggressively eliminates non-important features. Useful for reducing feature dimensions in large datasets.
  - **L2 Regularization**: Reduces dominant feature weights, allowing for a balanced feature influence. Often recommended.

## XGBoost Specifics
- **Alpha (L1 Regularization)**: Default is 0; increasing value makes the model more conservative.
- **Lambda (L2 Regularization)**: Default is 1; increasing value also makes the model more conservative.

## Automated Hyperparameter Tuning
- **Grid Search**: Exhaustive search over a specified parameter range.
- **Random Search**: Random selection of parameters within bounds.
- **SageMaker's Approach**: Treats tuning as a supervised learning problem, learning from parameter changes to optimize search.

## Summary
- Bias and variance give insights into model performance with new data.
- Regularization ensures no single feature dominates the model.
- Hyperparameters customize the learning process, with automatic tuning tools often used for efficiency.

# 152. Nuts and Bolts of Optimization

The Nuts and Bolts of Optimization is an important topic for the certification exam and optimizing your models.

## Common Strategies When Model Performance is Suboptimal
- Collect more data.
- Train longer.
- Hyperparameter optimization.
- Use a different algorithm or architecture.
- Implement regularization.
- Utilize a bigger model.

## Example: Human-Level Speech Recognition System
- **Goal**: Achieve human-level performance.
- **Dataset Management**: 70% for training, 15% each for validation and testing.
- **Metrics**: Human-level error, training error, validation error.

## Scenarios and Solutions

### Scenario 1: High Bias
- **Metrics**: Human-level error = 1%, Training error = 5%, Validation error = 6%.
- **Problem**: Model underperforms compared to human-level (high-bias, underfitting).
- **Solutions**: Train a bigger model, train longer, try new model architecture.

### Scenario 2: High Variance
- **Metrics**: Human-level error = 1%, Training error = 2%, Validation error = 6%.
- **Problem**: Overfitting (high-variance).
- **Solutions**: Add regularization, implement early stopping, get more data, try new model architecture.

### Scenario 3: High Bias and High Variance
- **Metrics**: Human-level error = 1%, Training error = 5%, Validation error = 10%.
- **Problem**: Model underperforms significantly, showing both high bias and variance.

### Scenario 4: Training/Test Data Distribution Mismatch
- **Metrics**: Human-level error = 1%, Training error = 5%, Validation error = 6%, Test error = 10%.
- **Problem**: Performance discrepancy due to different data distributions.
- **Solution**: Ensure validation and test sets come from the same distribution.

## Human-Level Performance
- **Medical Example**: Error rates from typical human to a team of expert doctors.
- **Optimal Error Rate**: Team of expert doctors as a benchmark for human-level performance.

## Workflow
- Implement a systematic workflow to address various performance issues.

## Data Synthesis
- **OCR System Example**: Generating synthetic data using random pictures and software like MS Word.
- **Speech Recognition Example**: Mixing clean audio with random background sounds for new data.

## Unified Data Warehouse/Data Lake
- Facilitates smoother data access and efficient progress.
- Consider user access rights and privacy.

## Key Takeaways
- Selection of the right optimization strategy is crucial for rapid progress.
- Balancing high bias and high variance is key to building effective models.
- Data synthesis can be a powerful tool in improving model performance.
- Unified data management systems enhance team efficiency and data accessibility.
