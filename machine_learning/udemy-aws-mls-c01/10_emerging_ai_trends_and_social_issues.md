# Emerging AI Trends and Social Issues

## Is AI Biased? (Lesson 111)

### Understanding the Complexities
- Defining fairness and proving model impartiality is complex.
    - Rush to market often leads to a focus on performance metrics, overlooking fairness.
- Where Bias Can Enter the AI Workflow:
    - **Data Bias**: Biased data preferences certain groups, leading to amplified bias in the model.
    - **Model Bias**: Inconsistent predictions across various groups (age, gender, income, etc.) can introduce bias.
    - **Inference Bias**: Occurs when training data distribution differs from real-world data.
- Difficulty in holding AI systems accountable for biased decisions
    - Different stakeholders may have varying definitions of what's fair

## Tools to Detect Bias - Clarify, Experiments, Model Monitor, Augmented AI (Lesson 112)

### AWS SageMaker Clarify
- Detects potential bias during data preparation, post-model training, and in deployed models. It also explains model predictions.
- Uses a model-agnostic feature attribution approach, employing game theory to derive Shapley values, assigning importance scores to each feature.
- Helps answer questions about model decisions, feature influence, and prediction processes.
- Note that it's easier to determine feature importance in linear/tree-based models than in neural networks. The correspondence of model-agnostic explanations to actual model actions in complex models like deep neural networks might be less straightforward.
- Provides feature importance graphs to show the influence of each input on decision-making.

### SageMaker Model Monitor
- Monitors production models for deviations in quality and bias drift, enabling alerts and corrective actions.
- Integration with Clarify: Notifies if model exceeds certain bias metric thresholds.

### Amazon Augmented AI
- Integrates human review into machine learning predictions, blending AI and human decision-making.
- **Use Cases**:
  - High confidence predictions are directly sent to clients.
  - Low confidence predictions are reviewed by humans.
  - Random sampling of predictions for auditing and quality assurance.
  - Multiple reviewers for consensus.
- Human-reviewed results are stored in S3 and can be used to refine models.
- **Workforce Options**:
  1. Amazon Mechanical Turk (public data).
  2. Private workforce & Third-party labeling service providers (confidential data).
