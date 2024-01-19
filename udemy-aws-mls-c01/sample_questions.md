# AWS Sample Question #2

A term frequency–inverse document frequency (tf–idf) matrix using both unigrams and bigrams is built from a text corpus consisting of the following two sentences:

```
Please call the number below.
Please do not call us.
```

What are the dimensions of the tf–idf matrix?

A. (2, 16)

B. (2, 8)

C. (2, 10)

D. (8, 10)

## Answer

A – There are 2 sentences, 8 unique unigrams, and 8 unique bigrams, so the result would be (2,16). 

The phrases are “Please call the number below” and “Please do not call us.”

Each word individually (unigram) is “Please,” “call,” ”the,” ”number,” “below,” “do,” “not,” and “us.”

The unique bigrams are “Please call,” “call the,” ”the number,” “number below,” “Please do,” “do not,” “not call,” and “call us.”

# AWS Sample Question #9

A company has collected customer comments on its products, rating them as safe or unsafe, using decision trees. The training dataset has the following features: id, date, full review, full review summary, and a binary safe/unsafe tag. During training, any data sample with missing features was dropped. In a few instances, the test set was found to be missing the full review text field.

For this use case, which is the most effective course of action to address test data samples with missing features?

A. Drop the test samples with missing full review text fields, and then run through the test set.

B. Copy the summary text fields and use them to fill in the missing full review text fields, and then run through the test set.

C. Use an algorithm that handles missing data better than decision trees.

D. Generate synthetic data to fill in the fields that are missing data, and then run through the test set.

## Answer

B – In this case, a full review summary usually contains the most descriptive phrases of the entire review and is a valid stand-in for the missing full review text field.

# AWS Sample Question #5

NOTE: For formulas, you can download Model Performance Evaluation.pdf, available in the "Downloadable Resources" lecture in this section.

A Data Scientist is evaluating different binary classification models. A false positive result is 5 times more expensive (from a business perspective) than a false negative result.

The models should be evaluated based on the following criteria:

Must have a recall rate of at least 80%

Must have a false positive rate of 10% or less

Must minimize business costs

After creating each binary classification model, the Data Scientist generates the corresponding confusion matrix.

Which confusion matrix represents the model that satisfies the requirements?

A. TN = 91, FP = 9, FN = 22, TP = 78

B. TN = 99, FP = 1, FN = 21, TP = 79

C. TN = 96, FP = 4, FN = 10, TP = 90

D. TN = 98, FP = 2, FN = 18, TP = 82

## Answer

NOTE: For formulas, you can download Model Performance Evaluation.pdf, available in the "Downloadable Resources" lecture in this section.

Formula for Recall (also known as True Positive Rate) is

TPR = TP / (TP + FN)

Formula for False Positive Rate (FPR) is

FPR = FP / (TN + FP)

Cost of misclassification is also given

Each false positive is $5 (i.e. what is the business cost when a negative is misclassified as a positive)

Each false negative is $1 (i.e. what is the business cost when a positive is misclassified as a negative)

Clearly, false positive is more expensive and we need to select the model that meets the following criteria

Recall rate of at least 80%

False positive rate of 10% or less

Minimize the business cost due to misclassification.

Let's look at the answer choices

A. TN = 91, FP = 9, FN = 22, TP = 78

Recall = 78/(78+22) = 78/100 or 78%. This is less than desired recall of 80%.

FPR = 9/(91+9) = 9/100 or 9%.

While FPR is less than 10%, recall is not meeting the 80% threshold So, we can eliminate this answer

B. TN = 99, FP = 1, FN = 21, TP = 79

Recall = 79/(79+21) = 79/100 or 79%. This is less than desired recall of 80%.

FPR = 1/(99+1) = 1/100 or 1%.

While FPR is less than 10%, recall is not meeting the 80% threshold So, we can eliminate this answer

C. TN = 96, FP = 4, FN = 10, TP = 90

Recall = 90/(90+10) = 90/100 or 90%. This is better than the desired recall of 80%

FPR = 4 / (96 + 4) = 4/100 or 4%. This is less than 10%.

Both these metrics are looking good. Let's now compute the misclassification cost

Model C misclassification cost = 5 * FP + 1 * FN (FP result is 5 times more expensive than a false negative result)

Misclassification cost = 5 * 4 + 1*10 = 20 + 10 = 30

D. TN = 98, FP = 2, FN = 18, TP = 82

Recall = 82 / (82 + 18) = 82/100 or 82%. This is better than the desired recall of 80%

FPR = 2/(98+2) = 2/100 or 2%. This is also less than 10% FPR

Both these metrics are looking good. Let's now compute the misclassification cost

Model D misclassification cost = 5 * FP + 1 * FN = 5 * 2 + 1 * 18 = 10 + 18 = 28

Both C and D meet the recall and FPR requirement. However, the business cost due to misclassification is less for model D.

So, model D is the answer