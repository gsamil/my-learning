# 111. Is AI Biased?

### Understanding the Complexities
- **Challenge of Defining Fairness**: Fairness varies contextually. What's fair for one group might not be fair for another. Example: Course promotions on a learning platform perceived differently by different instructors.
- **Building Fair Models**: Defining fairness and proving model impartiality is complex.
- **Where Bias Can Enter the AI Workflow**:
  1. **Data Bias**: Biased data preferences certain groups, leading to amplified bias in the model.
  2. **Model Bias**: Inconsistent predictions across various groups (age, gender, income, etc.) can introduce bias.
  3. **Inference Bias**: Occurs when training data distribution differs from real-world data. Example: A model trained on data with different interest rates may become biased in predicting current home prices.

### Real-Life Examples Highlighting AI Bias
1. **Lemonade Insurance**: Fast claim settlement using AI but raised privacy concerns over extensive data collection.
2. **Social Media and Fake News**: AI solutions for detecting fake news sometimes incorrectly tag content, showing algorithmic bias.
3. **Twitter's Image Cropping Algorithm**: Showed preference towards lighter skin tones and women, indicating bias.
4. **Credit Card Company Controversy**: Offered smaller credit lines to women despite not using gender as a model input, indicating indirect bias through proxies.

### Challenges and Observations
- **Algorithms Reflect and Magnify Biases**: AI can encode existing societal biases.
- **Optimizing Metrics Over Fairness**: Rush to market often leads to a focus on performance metrics, overlooking fairness.
- **Accountability Issues**: Difficulty in holding AI systems accountable for biased decisions.
- **Diverse Interpretations of Fairness**: Different stakeholders may have varying definitions of what's fair.

### Tools to Address AI Bias
- AWS provides tools to help quantify bias and explain decisions made by models.
- It's crucial to continuously monitor and adjust AI systems to ensure fairness.

### Conclusion
- Fairness in AI is a complex issue that requires careful consideration of data, model behavior, and real-world implications.
- As AI systems become more prevalent, addressing bias and ensuring fairness will be increasingly important.

# 112. Tools to Detect Bias - Clarify, Experiments, Model Monitor, Augmented AI

### AWS SageMaker Clarify
- **Functionality**: Detects potential bias during data preparation, post-model training, and in deployed models. It also explains model predictions.
- **Model Explanation**: Uses a model-agnostic feature attribution approach, employing game theory to derive Shapley values, assigning importance scores to each feature.
- **Application**: Helps answer questions about model decisions, feature influence, and prediction processes.
- **Consideration**: Easier to determine feature importance in linear/tree-based models than in neural networks. The correspondence of model-agnostic explanations to actual model actions in complex models like deep neural networks might be less straightforward.

### Assessing Fairness
- **Fairness Metrics**: Offers various metrics for data bias and post-training model bias.
- **Challenges**: Defining and measuring fairness is complex. A model may not conform to all fairness metrics simultaneously; appropriate metrics should be chosen based on specific use cases.

### SageMaker Experiments
- **Purpose**: Tracks the inputs, parameters, configurations, and results of machine learning iterations as trials.
- **Integration with Clarify**: Provides feature importance graphs to show the influence of each input on decision-making.

### SageMaker Model Monitor
- **Functionality**: Monitors production models for deviations in quality and bias drift, enabling alerts and corrective actions.
- **Integration with Clarify**: Notifies if model exceeds certain bias metric thresholds.

### Amazon Augmented AI
- **Overview**: Integrates human review into machine learning predictions, blending AI and human decision-making.
- **Use Cases**:
  - High confidence predictions are directly sent to clients.
  - Low confidence predictions are reviewed by humans.
  - Random sampling of predictions for auditing and quality assurance.
  - Multiple reviewers for consensus.
- **Outcome Storage**: Human-reviewed results are stored in S3 and can be used to refine models.
- **Workforce Options**:
  1. Amazon Mechanical Turk (public data).
  2. Private workforce (confidential data).
  3. Third-party labeling service providers (confidential data).

### Applications of AWS Tools
- **Regulatory Compliance**: Assists in meeting requirements of laws like the Equal Credit Opportunity Act or Fair Housing Act.
- **Internal Reporting and Compliance**: Justifies model decisions to internal stakeholders, auditors, and executives.
- **Customer Interactions**: Supports customer-facing employees in understanding AI-driven decisions.

### Summary
- SageMaker Clarify offers a comprehensive solution for detecting bias and explaining model behavior.
- Augmented AI combines machine and human decision-making for quality assurance and compliance.
- These tools are valuable for regulatory compliance, internal governance, and enhancing customer trust in AI systems.
