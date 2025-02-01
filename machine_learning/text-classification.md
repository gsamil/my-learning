# Text Classification Using Class Information

## Problem Statement

We are used to working on text classification problem. It's generally very straightforward. However, there are cases where classes also contain some information and we may feel like we should also use this information. For example, we may want to understand user intent in a chatbot, or we may want to categorize a product given its description. In these cases, categories also have semantic meaning, i.e. some categories are related to each other, so we can also create embedding vectors for the categories.

Let's work on a concrete example. We have product descriptions for some products in an e-commerce website, and we have their corresponding categories. We want to train a model that will predict the category of a given product description to help the sellers identify the correct category for their product. I will explain step-by-step how we can train a model for such a scenario.

## Initial Data Exploration

We want to make sure everything is good with our data:

1. Are the categories in the training and evaluation files same?
    i. Are there any categories in the eval file which are not in the training data? We want to remove these categories if any.
    ii. Are there any categories in the train file which are not in the eval data? We may want to put some of these samples into eval data or remove these categories.
2. Does all samples have categories? If not, we want to remove them.
3. After pre-processing if any input text becomes empty text, i.e. `""`, then we don't want to use these as well.

## Pre-Processing

There are a number of pre-processings we can apply to text data. I will not explain them as there are already a lot of resources available and it's not my main focus.

Because of the reasons I will explain later, we don't need much pre-processing with the data. What I did is:

- Use the lowercase text (if uppercase characters have additional information, you may want to keep them)
- Remove characters that are repeated too few in the training data, and remove the ones that are not have any information regarding training.
- If your training data has inbalanced number of samples between classes, you may want to select a subset of training data which is more balanced. In my case, I selected 100 samples from each category.

## Feature Extraction

Most of the times, we need a method to convert the text into a set of numbers with fixed dimension, i.e. features/embedding vectors. Because these features will be representatives of their corresponding texts, we need to have a good feature extractor model, which is either costly (if we don't want to deploy the model to our own servers, we would use some external embedding API such as OpenAI embeddings) or we need to increase our memory requirements (because current model that generate quality embeddings are generally BERT based models, and they are large models).

TF-IDFs are less costly alternative to convert text into numerical features. However, they are generally quite large, as they keep n-grams.

If we create a dictionary of characters vs indexes, we can easily convert any text into numerical values. Then we can train an embedding layer using these indexes. This method has a number of advatages:

- We don't need to keep the weights for TF-IDF model, we only need to keep a simple dictionary.
- We can remove any character that we don't neew/want from the dictionary, which means automatic pre-processing of text.
- We can use a small dimensional vector. I selected the dimesion by checking the number of characters in each product description, then I choosed the longest one. One drawback is out text input needs to be limited to this value, however this wouldn't be a big problem.

## 1st Solution - Use Distances

The simplest solution would be to extract the $e$ dimensional embeddings for each category ($v_\{c_1\}, v_\{c_2\}, ... v_\{c_n\}$) and construct an $e \times n$ dimensional matrix where $n$ is the number of categories. Then for each product description, all we need to do is first extract the $e$ dimensional embedding of product description, then do a matrix multiplication to get the distances, and choose the category with minimum distance.

This procedure requires no training, and requires a minimal memory, because all we need to store is the $e \times n$ dimensional category embeddings matrix.

I will not implement this method because I want to do some trainings :)

## 2nd Solution - Train a Classifier

If we want to train a model, then the simplest option is to train a classifier, that generates $n$ dimensional output logits. Then we can use this classifier to predict the category of a given product description.

### Data Preparation

We decided to use character indexes as embedding vectors. First we need to decide the feature dimension, i.e. how many characters we want to use as input to our model. We can do this by looking at all of the product description text lengths, and choosing somewhere near max. We will be cutting the text from the end if it's longer than this length.

For my case, max length text in the training data has 100 chars, so I selected 100 as my feature dimension.

We can define a PyTorch `Dataset` class for this:

```python
class ClassificationDataset(Dataset):
    def __init__(
        self,
        data: list[ClassificationSample],
        vocab: dict[str, int],
        category_to_idx: dict[str, int],
        feature_size: int,
    ):
        self.data: list[ClassificationSample] = data
        self.vocab: dict[str, int] = vocab
        self.feature_size: int = feature_size
        self.category_to_idx: dict[str, int] = category_to_idx

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, idx) -> Tuple[torch.Tensor, int]:
        example = self.data[idx]
        return (
            torch.LongTensor(
                set_feature_dimension(
                    [self.vocab[token] for token in example.product_text],
                    self.feature_size,
                )
            ),
            self.category_to_idx[example.category],
        )
```

Notice that we convert the characters into numbers in `__getitem__()` method. We have `set_feature_dimension()` function to limit the text feature vector dimension to a constant value. See [ClassificationDataset](https://github.com/gsamil/text-classification/blob/main/classifier/dataset.py)

### Model

Model is same for both classifier and recommender, only difference being classifier has output dimension of `len(categories)`, and recommender has output dimension of 2. See [TextClassifier](https://github.com/gsamil/text-classification/blob/main/model.py#L65).

```python
class TextClassifier(nn.Module):
    def __init__(self, hparameters: HyperParameters):
        super(TextClassifier, self).__init__()
        self.hyper_parameters = hparameters
        self.embedding = nn.Embedding(hparameters.vocab_size, hparameters.embedding_dim)
        self.rnn = nn.LSTM(
            hparameters.embedding_dim, hparameters.hidden_dim, batch_first=True
        )
        self.fc = nn.Linear(hparameters.hidden_dim, hparameters.num_classes)

    def forward(self, x):
        embedded = self.embedding(x)
        output, _ = self.rnn(embedded)
        last_hidden = output[:, -1, :]
        logits = self.fc(last_hidden)
        return logits
```

### Training

My model has input dimension of 100 and starts with an embedding layer with dimension 8 and RNN hidden dimension of 128. I didn't want to increase these numbers because of my computaional resources.

Pipeline will be like:

```python
product_description_text --> product_description_vector ($v_1$ dimensional vector) --> model --> $n$ dimensional output logits
```

See [training code here](https://github.com/gsamil/text-classification/blob/main/classifier/train.py) to understand the training pipeline. (It's a usual PyTorch model training.)

### Inference

Inference in this case is same with training, we will just choose the logit index with max value as the predicted category. See [here](https://github.com/gsamil/text-classification/blob/main/classifier/evaluate.py)

## 3rd Solution - Train a Recommender

If we want to train a model, a 2nd solution is to include the vector represantations of categories into the input feature as well. We would want to do this in case category text are also semantically meaningful. (For example for product description -> category pair `iphone 13 mini -> mobile phones` both of them are semantically meaningful, so we can utilize embeddings for both of them). Take a look at the below chart to understand how we can train such a model and run inference on them.

Obvious advantage of this method is we are actively including more information into the training. However, one disadvantage is because this time model outputs are binary, we need to run this model for each category, so it is computationally more expensive compared to the 2nd solution.

### Data Preparation

In this case, we will also include the category texts to the input, so we need to consider text length of our categories as well.

For my case, max length text in the training data & category combination has around 135 chars, but these counts of these samples are not much, so I selected 100 as my feature dimension.

Another consideration here we are training with product text - category pairs. So for each product text - category pair, we will have `len(categories)` training samples, 1 with class 1 and others with class 0. So number of training samples in our data will be `number of training samples X number of categories`, which is a lot for my computational resources. So I subsampled 99 negative classes for each text - category pair, so number of training samples in my data is `number of training samples X 100`. Note that this value dramatically changes the training loss, which means if I subsample to few negative samples, then my performance will decrease drastically.

```python
class ClassificationDataset(Dataset):
    def __init__(
        self,
        samples: list[ClassificationSample],
        vocab: dict[str, int],
        categories: list[str],
        category_to_idx: dict[str, int],
        feature_size: int,
        sample_negatives: int | None,
        shuffle: bool,
    ):
        self.data: list[ClassificationSample] = samples
        self.vocab: dict[str, int] = vocab
        self.categories: list[str] = categories
        self.category_to_idx: dict[str, int] = category_to_idx
        self.feature_size: int = feature_size
        self.sample_negatives: int | None = sample_negatives
        self.shuffle: bool = shuffle

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, idx) -> Tuple[torch.LongTensor, list[int], int]:
        example = self.data[idx]
        combined_features_positive = []
        combined_features_negative = []
        for category in self.categories:
            # this is the part where we convert product text and category to indexes
            product_text_tokens = [self.vocab[token] for token in example.product_text]
            category_tokens = [self.vocab[token] for token in category]
            product_text_token_indexes = set_feature_dimension(
                product_text_tokens,
                self.feature_size - len(category_tokens),
            )
            token_indexes = product_text_token_indexes + category_tokens

            if example.category == category:
                combined_features_positive.append(token_indexes)
            else:
                combined_features_negative.append(token_indexes)

        if self.sample_negatives is not None:
            combined_features_negative = random.sample(
                combined_features_negative, self.sample_negatives
            )
        combined_features_with_labels = [
            (feature, 1) for feature in combined_features_positive
        ] + [(feature, 0) for feature in combined_features_negative]

        if self.shuffle:
            random.shuffle(combined_features_with_labels)
        return (
            torch.LongTensor([f for f, _ in combined_features_with_labels]),
            [l for _, l in combined_features_with_labels],
            [i for i, (_, l) in enumerate(combined_features_with_labels) if l == 1][0],
        )
```

### Model

Model is same for both classifier and recommender.

### Training

My model has input dimension of 100 and starts with an embedding layer with dimension 8 and RNN hidden dimension of 128.

Pipeline will be like:

```python
product_description_text -> product_description_vector ->  ($v_2$ dimensional vector) -> model -> $2$ dimensional output logits
                                                      /
category_text ------------> category_vector ---------/
```

See [here](https://github.com/gsamil/text-classification/blob/main/recommender/train.py) for training pipeline.

### Inference

Inference in this case is different, because now our trained model just compares a text - category pair and decides if text belongs to the category or not (0-1).
So I need to run my model `len(categories)` times with batch inference, obtain the probabilities for the text belonging to the category for each category, and use these probabilities as my logits.
Then I can just choose the logit index with max value as the predicted category as before.

Pipeline will be like:

```python
for category in all_categories:
    product_description_text -> product_description_vector ->  ($v_2$ dimensional vector) -> model -> probabily value of $logit_1$
                                                          /
    category_text ------------> category_vector ---------/

prediction = argmax(logits for all categories)
```

See [here](https://github.com/gsamil/text-classification/blob/main/recommender/evaluation.py) for evaluation pipeline.

## Results

We should compare our suggested solutions both in terms of performance, memory requirements and inference time.

One thing to note here is that I used a sub-sample of both training (by selecting 1000 samples from each class) and test (by selecting 100 samples from each class) set in these results, because my computer isn't fast enough to evaluate all of the test data in a reasonable time. So using all data, I assume results would be improved significantly.

I trained both models for 3 epochs.

```markdown
|Method     |Accuracy|Precision|Recall  |F1-Score|Inference Time (sec)|
|-----------|--------|---------|--------|--------|--------------------|
|Classifier | 0.6925 | 0.7006  | 0.6925 | 0.6871 | 11.27              |
|Recommender| 0.3081 | 1.0000  | 0.3081 | 0.4711 | 3506.54            |
```

Memory requirements for the recommender will be much higher compared to the clasifier, because of the number of inferences we need to run for each sample. (if we use batch inference)

## Conclusions

- Using classification model is much faster and accuracy is much higher.
- Notice that precision of recommender model is 1, which means it is a highly cautious model. So my guess is with some hyperparameter tuning and using all of the training data, we could obtaine much better results that classification model.
- If our resources is limited however, it's a better idea to go with the classifier. Because using more that would definitely increase the performance of this model as well. We only used 1000 samples for each class and we have more than 1000 classes, so we need more samples.

## Future Directions

- I didn't use a separate validation data. It's much better to get the results for a validation test set after each step too. So we can separate train data into train and validation.
- In the recommender model, we can use fixed dimensional vectors for product description and category separately, then merge them. Model will understand where is the text and where is the label, and my guess is it will generate better results.
- We can use other metrics like Mean Average Precison at N (MAP@N) to understand the ranking capability of the models.
- We can experiment on the feature dimensions, maybe we don't need 100 characters.
- We can try to combine classifier and recommender. After getting the results from the classifier model, we can re-sort top-k logits with recommender. This will eliminate the time limitation of recommender model and probably increase the classification accuracy more.

## References

- [Code implementation](https://github.com/gsamil/text-classification/)