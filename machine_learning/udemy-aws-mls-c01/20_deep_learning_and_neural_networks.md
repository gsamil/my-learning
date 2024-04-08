# Deep Learning and Neural Networks

## Regression - Gradient Descent Batch, Mini-Batch, Stochastic, Loss, RMSProp, Adam (Lesson 209)

### Objective
- Explore how the linear regression algorithm trains a model and understand the role of gradient descent and loss functions.

### Concepts
1. **Linear Regression**:
   - Basic algorithm for predictive modeling.
   - Involves finding the best weights for input features to predict an output.

2. **Loss Function (Mean Squared Error)**:
   - Measures the difference between predicted values and actual values.
   - Lower loss indicates better predictions.

3. **Gradient Descent**:
   - A systematic approach to find optimal weights.
   - Uses the gradient of the loss function to adjust weights.
   - Moves weights in the direction that reduces the loss.

4. **Learning Rate**:
   - Controls the magnitude of weight adjustments.
   - Low learning rate: Many small steps to reach the optimal weight.
   - High learning rate: May overshoot the optimal weight.

5. **Variants of Gradient Descent**:
   - **Batch Gradient Descent**: Adjusts weights using all training examples in each iteration.
   - **Stochastic Gradient Descent (SGD)**: Adjusts weights based on each training example.
   - **Mini Batch Gradient Descent**: Combines batch and SGD, adjusting weights using small subsets of training data.

6. **Optimization Techniques**:
   - Adaptive learning rate algorithms (e.g., RMSProp, Adagrad, Adam) to improve convergence.
   - Momentum to reduce oscillations and speed up convergence.

### Process
1. **Training Linear Regression**:
   - Initialize random weights.
   - Calculate loss using loss function.
   - Adjust weights based on the gradient of the loss function.

2. **Gradient Descent in Action**:
   - Plot loss versus weight.
   - Start with a random weight.
   - Move weight in the direction that reduces the loss (opposite of the gradient).
   - Continue until reaching an optimal weight.

3. **Dealing with Multiple Features**:
   - Loss plot becomes multidimensional.
   - Adjust weights of all features simultaneously.

## Classification - Gradient Descent, Loss Function (Lesson 210)

### Objective
- Explore logistic regression as a classification algorithm and understand its functioning in predicting probabilities.

### Concepts
1. **Logistic Regression Overview**:
   - A classification algorithm, despite the name suggesting regression.
   - Similar to linear regression but predicts probabilities (0 to 1) using a sigmoid function.

2. **Sigmoid Function**:
   - Key component in logistic regression.
   - Converts any input to a value between 0 and 1, ideal for probability predictions.

3. **Model Training**:
   - Input features (X) with corresponding weights (W).
   - Model predicts the probability of belonging to a positive class.
   - Cutoff generally at 0.5 for classifying into positive or negative classes.

4. **Logistic Loss Function**:
   - Measures the quality of predictions.
   - Composed of two parts: one for positive and one for negative samples.
   - Loss is high for misclassifications and low for accurate predictions.

5. **Gradient Descent Optimization**:
   - Used to find the optimal weights that minimize the logistic loss.
   - Process involves adjusting weights based on the loss gradient.
   - Produces a loss curve (parabola) from which gradient and optimal weights are determined.

### Process
1. **Applying Sigmoid Function**:
   - Use linear model output as input to sigmoid function.
   - Predicts the probability of sample belonging to the positive class.

2. **Setting Cutoff for Classification**:
   - Default cutoff is 0.5.
   - Adjusting weights changes the criteria for classification.

3. **Computing Logistic Loss**:
   - Calculate logistic loss for a range of predicted probabilities.
   - Compare against actual labels to evaluate loss.

4. **Weight Optimization with Gradient Descent**:
   - Start with random weights.
   - Adjust weights iteratively to minimize logistic loss.

## Neural Networks and Deep Learning (Lesson 211)

### Objective
- Understand the structure and functioning of neural networks in deep learning.

### Neural Network Structure
1. **Basic Architecture**:
   - Comprises an input layer, hidden layers, and an output layer.
   - Appears similar to logistic regression but extends with multiple neurons in hidden layers.

2. **Neurons and Activation Functions**:
   - Neurons generate new features by blending existing features with different weights.
   - Activation functions introduce non-linearity, improving handling of complex datasets.

3. **Common Activation Functions**:
   - Sigmoid: Converts input to a range between 0 and 1.
   - Tanh (Hyperbolic Tangent): Output ranges from -1 to 1.
   - ReLU (Rectified Linear Unit): Outputs 0 for negative input, and raw input for positive values.

### Network Types and Applications
1. **General-Purpose Networks**:
   - Fully connected; each neuron in a layer connected to all neurons in the next layer.
   - Useful for diverse applications but may lead to overfitting.

2. **Convolutional Neural Networks (CNNs)**:
   - Specialized for image and video analysis.
   - Focuses on patterns around each pixel, not just the pixel itself.

3. **Recurrent Neural Networks (RNNs)**:
   - Ideal for time series forecasting and natural language processing.
   - Capable of remembering historical data, crucial for sequence-dependent predictions.

### Key Points
- **Benefits of Neural Networks**:
   - Can fit nonlinear datasets effectively.
   - Automatically generates new feature combinations.
   - Highly scalable and adaptable for various complex applications.

- **Challenges**:
   - Complexity in tuning and risk of overfitting.
   - Requires extensive computation, especially for large networks.

## Labs

1. Regression with SKLearn Neural Network (Lesson 213)
2. Regression with Keras and TensorFlow (Lesson 214)
3. Binary Classification - Customer Churn Prediction (Lesson 216 & 217)
4. Multiclass Classification - Iris (Lesson 218)

## Convolutional Neural Network (CNN) (Lesson 230)

### How CNNs Work
1. **Convolution Operation**:
   - CNNs break down images into smaller squares (patches) using a sliding window.
   - For instance, a 4x4 filter slides across the image, capturing each 4x4 patch.
   - Each neuron receives a patch rather than an individual pixel, preserving spatial context.

2. **Feature Learning**:
   - Neurons in CNNs learn to differentiate between different classes of image features (e.g., cars vs. faces).
   - They identify dominant characteristics specific to each image class.

### Advantages of CNNs
- **Preservation of Spatial Relationships**: By analyzing patches rather than individual pixels, CNNs maintain the spatial hierarchy of pixels, crucial for understanding image content.
- **Efficiency**: CNN models are generally smaller and more efficient compared to deep, general-purpose neural networks for image classification.
- **Improved Performance**: CNNs typically outperform traditional networks in image-related tasks due to their ability to capture and learn from spatial information in images.

### Reference
- MIT 6.S191 Lecture: "Convolutional Neural Networks" by Ava Soleimany.
  - Video Link: [MIT 6.S191: Convolutional Neural Networks](https://www.youtube.com/watch?v=H-HVZJ7kGI0)

## 231. Recurrent Neural Networks (RNN), LSTM

### Key Characteristics of RNNs
- **Sequential Processing**: Unlike general-purpose neural networks that process single inputs, RNNs handle sequences of inputs (e.g., series of words, stock prices over time).
- **Memory Mechanism**: RNNs maintain an internal state to remember past information, crucial for sequential decision-making.
- **Feedback Loops**: These loops allow RNNs to update and maintain their internal state based on new inputs and previously learned information.

### LSTM Networks
- **Long Term and Short Term Memory**: LSTMs are a special kind of RNN capable of learning long-term dependencies.
- **Selective Memory**: They excel in remembering important past information and forgetting irrelevant details, making them effective for complex sequential tasks.

### Reference
- MIT 6.S191 Lecture: "Recurrent Neural Networks" by Ava Soleimany.
  - Video Link: [MIT 6.S191: Recurrent Neural Networks](https://youtu.be/_h66BW-xNgk)

## Generative Adversarial Networks (GANs) (Lesson 232)

### Core Components
- **Two-Player Game Setup**: GANs consist of two key players – the Discriminator and the Generator.
  - **Discriminator Network**: Trained to distinguish between real images (assigning high probability to real ones).
  - **Generator Network**: Produces synthetic data, such as fake images.
  - **Learning Process**: The discriminator learns to assign low probabilities to these fake images.

### Game Dynamics
- **Concurrent Optimization**: The generator tries to create images that the discriminator will perceive as real.
- **Stable State Goal**: Achieving a state where the generator produces perfectly realistic images indistinguishable from actual data.

### Applications
- **Synthetic Data Generation**: Creating realistic synthetic images for training other models.
- **Diverse Object Creation**: Capable of producing a wide array of objects.
- **Practical Use Case**: Apple's utilization of GANs to merge text sources with smaller trajectory datasets to create new trajectories for expanding their dataset.

### Reference
- Presentation: "GANs for Good- A Virtual Expert Panel" by Ian Goodfellow.
- Video Link: [GANs for Good - DeepLearning.AI](https://youtu.be/9d4jmPmTWmc)
