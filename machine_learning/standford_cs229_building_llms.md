### Reference Video

[Stanford CS229 I Machine Learning I Building Large Language Models (LLMs)](https://youtu.be/9vM4p9NN0Ts)

# Lecture Notes: Building Large Language Models (LLMs)

## Introduction

This lecture provides an in-depth overview of how Large Language Models (LLMs) are built, covering key components such as pretraining, post-training (alignment), data handling, evaluation methods, and systems optimization. The focus is on understanding the practical aspects of developing LLMs like ChatGPT, Claude, Gemini, and Llama, highlighting the importance of data, evaluation, and systems over architectural tweaks.

---

## Overview of LLMs

### What are LLMs?

- **Definition**: Large Language Models are neural networks trained on vast amounts of textual data to understand and generate human-like language.
- **Examples**: ChatGPT (OpenAI), Claude (Anthropic), Gemini (Google), Llama (Meta).

### Key Components in Training LLMs

1. **Architecture**: The neural network structure (e.g., Transformers).
2. **Training Loss and Algorithm**: Methods used to optimize the model.
3. **Data**: The textual information used for training.
4. **Evaluation**: Metrics and methods to assess performance.
5. **Systems**: Hardware and software optimizations for efficient training.

**Important Takeaway**: While architecture is crucial, **data quality**, **evaluation methods**, and **systems optimizations** play a more significant role in the practical performance of LLMs.

---

## Pretraining

### Language Modeling Task

- **Objective**: Model the probability distribution over sequences of tokens (e.g., words or subwords).
- **Autoregressive Models**: Predict the next token based on previous tokens using the chain rule of probability.
  
  \[
  P(x_1, x_2, ..., x_L) = \prod_{i=1}^{L} P(x_i | x_{<i})
  \]

- **Example**:
  - Input: "She likely prefers"
  - Model predicts: "dogs" (or other plausible continuations).

### Loss Function

- **Cross-Entropy Loss**: Used to compare the predicted token probabilities against the actual tokens.
- **Maximizing Log Likelihood**: Equivalent to minimizing cross-entropy loss.

**Important Takeaway**: The core of pretraining involves teaching the model to predict the next token, thereby learning language patterns and structures.

---

### Tokenization

**Purpose**: Convert raw text into tokens that the model can process.

#### Why Not Just Use Words or Characters?

- **Words**:
  - Issues with typos, rare words, and languages without clear word boundaries.
- **Characters**:
  - Results in very long sequences, increasing computational cost.

#### Byte Pair Encoding (BPE)

- **Algorithm**:
  1. Start with all characters as tokens.
  2. Merge the most frequent pairs of tokens iteratively.
  3. Build a vocabulary of subword tokens.

- **Advantages**:
  - Handles rare words and subwords.
  - Balances vocabulary size and sequence length.

**Important Takeaway**: **Tokenization significantly impacts model performance and efficiency**. Proper tokenization ensures the model effectively handles a variety of linguistic inputs while keeping computational costs manageable.

---

### Evaluation of Pretrained LLMs

#### Perplexity

- **Definition**: A measure of how well a probability model predicts a sample.
- **Calculation**:

  \[
  \text{Perplexity} = 2^{\text{Cross-Entropy Loss}}
  \]

- **Interpretation**:
  - Lower perplexity indicates better performance.
  - Represents the effective "number of choices" the model predicts at each step.

- **Limitations**:
  - Depends on tokenizer and data.
  - Not widely used in academic benchmarks due to inconsistencies.

#### Academic Benchmarks

- **HELM (Holistic Evaluation of Language Models)** and **Hugging Face Open Leaderboard**: Collections of tasks to evaluate LLM performance.
- **MMLU (Massive Multitask Language Understanding)**: Tests models on diverse subjects, resembling a challenging exam.

**Evaluation Challenges**:

- **Inconsistencies**: Different evaluation methods can yield varying results.
- **Train-Test Contamination**: Ensuring test data wasn't seen during training is critical but difficult.

**Important Takeaway**: **Evaluating LLMs is complex** and requires careful consideration to ensure meaningful comparisons.

---

### Data Collection and Processing

#### Data Sources

- **Common Crawl**: A web crawler that collects vast amounts of internet data (~250 billion pages).

#### Processing Steps

1. **Text Extraction**: Remove HTML and extract meaningful text.
2. **Content Filtering**:
   - **Undesirable Content**: Filter out NSFW, harmful, or private information.
   - **Blacklist**: Use lists of disallowed sites.
3. **Deduplication**: Remove duplicate content to avoid overrepresentation.
4. **Heuristic Filtering**: Apply rules-based methods to filter low-quality content (e.g., unusual token distributions).
5. **Model-Based Filtering**: Train classifiers to select high-quality data.
6. **Domain Classification and Balancing**:
   - Classify data into domains (e.g., code, books).
   - Adjust the proportions to emphasize high-quality domains.
7. **Final Fine-Tuning**:
   - Focus on high-quality data like Wikipedia.
   - Overfit slightly to improve language understanding.

**Important Takeaway**: **Data quality is paramount**. Extensive cleaning and filtering are required to ensure the model learns useful and accurate information.

---

### Scaling Laws

- **Observation**: Model performance improves predictably with increased data, model size, and compute.
- **Empirical Findings**:
  - Loss scales as a power-law with model size and data.
  - There's an optimal balance between model size and training data for a fixed compute budget.

#### Chinchilla Scaling Laws

- **Optimal Ratio**: Approximately **20 tokens per parameter**.
- **Implications**:
  - Underlines the importance of training both large models and providing them with sufficient data.
  - Guides resource allocation for model training.

**Important Takeaway**: **Scaling laws help predict and optimize model performance**, highlighting the need for balance among model size, data quantity, and compute resources.

---

## Post-Training (Alignment)

### Motivation

- **Pretrained LLMs** may not follow user instructions or could generate undesirable outputs.
- **Alignment** aims to make LLMs helpful, safe, and aligned with human values.

**Important Takeaway**: **Alignment transforms general LLMs into effective AI assistants**, improving their utility and safety in real-world applications.

---

### Supervised Fine-Tuning (SFT)

#### Method

- **Data Collection**: Human experts create instruction-response pairs.
- **Fine-Tuning**: The pretrained model is further trained on this data using the same language modeling loss.

#### Characteristics

- **Data Quantity**: Surprisingly small datasets (e.g., 2,000 examples) can significantly influence the model.
- **Limitations**:
  - Quality depends on human-generated data.
  - Does not generalize beyond provided examples.

**Important Takeaway**: **SFT adjusts the model's behavior** to better align with desired responses but is limited by the scope and quality of the fine-tuning data.

---

### Reinforcement Learning from Human Feedback (RLHF)

#### Motivation

- **Challenges with SFT**:
  - **Human Limitations**: Humans may not produce the best possible answers but can judge quality effectively.
  - **Hallucinations**: The model might generate plausible but incorrect information.
  - **Cost**: Generating high-quality responses is expensive.

#### Process

1. **Collect Comparisons**: Humans compare multiple model outputs for the same prompt, indicating preferences.
2. **Train a Reward Model**: Learn to predict human preferences.
3. **Fine-Tune the LLM**:
   - **PPO (Proximal Policy Optimization)**: An RL algorithm used to optimize the policy (the LLM) to maximize the reward model's score.

#### Direct Preference Optimization (DPO)

- **Alternative to PPO**.
- **Simpler Implementation**: Uses standard supervised learning to prefer better responses over worse ones.
- **Comparable Performance**: Achieves similar results without complex RL algorithms.

**Important Takeaway**: **RLHF enables models to learn from preferences rather than correct answers**, leading to higher-quality and more aligned outputs.

---

### Data Collection for RLHF

#### Human Feedback

- **Quality**: Essential for aligning the model.
- **Challenges**:
  - **Cost**: Collecting extensive human preference data is expensive.
  - **Consistency**: Humans may have varying opinions on quality.

#### Synthetic Feedback

- **Using LLMs**: Models generate preferences to augment human data.
- **Benefits**:
  - **Scalability**: Can produce much larger datasets.
  - **Consistency**: Reduces variance in preferences.

- **Limitations**:
  - **Biases**: Models may reinforce undesirable biases.
  - **Over-Optimization**: Risk of model exploiting patterns in synthetic data.

**Important Takeaway**: **Leveraging LLMs for data collection can scale RLHF**, but care must be taken to mitigate biases and ensure data quality.

---

### Evaluation of Post-Trained LLMs

#### Challenges

- **Open-Ended Outputs**: Hard to evaluate correctness and quality.
- **Lack of Perplexity Usefulness**: Post-training alters the model's output distribution, making perplexity less meaningful.
- **Diversity of Tasks**: Models are expected to perform well across a broad range of tasks.

#### Evaluation Methods

1. **Human Evaluation**:
   - **Blind Comparisons**: Humans compare outputs from different models.
   - **Challenges**: Time-consuming and expensive.

2. **Automated Evaluation**:
   - **LLMs as Evaluators**: Use models to assess other models' outputs.
   - **Benefits**: Scalable and cost-effective.
   - **Limitations**:
     - **Biases**: Models may have inherent biases (e.g., favoring longer responses).
     - **Agreement with Humans**: Must ensure evaluations correlate well with human judgments.

**Important Takeaway**: **Evaluating aligned LLMs requires innovative approaches** to accurately measure performance across diverse and open-ended tasks.

---

## Systems Optimization

### Importance

- **Compute Constraints**: Training LLMs is resource-intensive.
- **Cost and Scarcity**: Access to large numbers of GPUs is limited.
- **Efficiency**: Optimizations can significantly reduce training time and cost.

**Important Takeaway**: **Systems optimizations are crucial** to make training large models feasible and efficient.

---

### Low Precision Training

- **Concept**: Use reduced numerical precision (e.g., 16-bit floating points) during training.
- **Advantages**:
  - **Speed**: Lower precision arithmetic is faster on GPUs.
  - **Memory**: Reduced memory usage allows for larger batch sizes or models.
- **Techniques**:
  - **Mixed Precision Training**: Combines low-precision calculations with higher-precision updates where necessary.

**Important Takeaway**: **Low precision training improves computational efficiency** without significantly affecting model performance.

---

### Operator Fusion

- **Problem**: Separate operations can cause unnecessary data movement and underutilize GPU capabilities.
- **Solution**: Combine multiple sequential operations into a single operation (kernel) to reduce overhead.
- **Implementation**:
  - **Fused Kernels**: Custom GPU operations that perform multiple computations in one pass.
  - **Libraries and Tools**: Use frameworks like PyTorch's `torch.compile` to automate fusion.

**Important Takeaway**: **Operator fusion reduces data movement overhead**, leading to better GPU utilization and faster training.

---

## Conclusion

Building LLMs involves a complex interplay of data processing, model training, alignment techniques, evaluation methods, and systems optimizations. Key takeaways include:

- **Data Quality is Critical**: Effective data collection and filtering directly impact model performance.
- **Scaling Laws Inform Strategy**: Understanding how model size and data affect performance helps allocate resources efficiently.
- **Alignment Enhances Usability**: Techniques like SFT and RLHF make models more helpful and safer for users.
- **Systems Optimizations are Essential**: Efficient use of hardware accelerates training and reduces costs.

---

## Further Reading

For more in-depth knowledge and practical experience in building and understanding LLMs, consider the following courses:

- **CS224N**: Natural Language Processing with Deep Learning
- **CS324**: Large Language Models
- **CS336**: Large Language Models from Scratch

---

**Note**: This lecture underscores that while neural network architecture is important, **the practical success of LLMs hinges more on data quality, effective alignment, robust evaluation, and systems-level optimizations**.

