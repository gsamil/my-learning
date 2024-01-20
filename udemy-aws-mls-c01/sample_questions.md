# AWS Sample Question #1

A Machine Learning team has several large CSV datasets in Amazon S3. Historically, models built with the Amazon SageMaker Linear Learner algorithm have taken hours to train on similar-sized datasets. The team’s leaders need to accelerate the training process.

What can a Machine Learning Specialist do to address this concern?

A. Use Amazon SageMaker Pipe mode.

B. Use Amazon Machine Learning to train the models.

C. Use Amazon Kinesis to stream the data to Amazon SageMaker.

D. Use AWS Glue to transform the CSV dataset to the JSON format

## Answer

A – Amazon SageMaker Pipe mode streams the data directly to the container, which improves the performance of training jobs. (Refer to this link for supporting information.) In Pipe mode, your training job streams data directly from Amazon S3. Streaming can provide faster start times for training jobs and better throughput. With Pipe mode, you also reduce the size of the Amazon EBS volumes for your training instances. B would not apply in this scenario. C is a streaming ingestion solution, but is not applicable in this scenario. D transforms the data structure.

https://aws.amazon.com/blogs/machine-learning/now-use-pipe-mode-with-csv-datasets-for-faster-training-on-amazon-sagemaker-built-in-algorithms/

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

# AWS Sample Question #3

A company is setting up a system to manage all of the datasets it stores in Amazon S3. The company would like to automate running transformation jobs on the data and maintaining a catalog of the metadata concerning the datasets. The solution should require the least amount of setup and maintenance. Which solution will allow the company to achieve its goals?

A. Create an Amazon EMR cluster with Apache Hive installed. Then, create a Hive metastore and a script to run transformation jobs on a schedule.

B. Create an AWS Glue crawler to populate the AWS Glue Data Catalog. Then, author an AWS Glue ETL job, and set up a schedule for data transformation jobs.

C. Create an Amazon EMR cluster with Apache Spark installed. Then, create an Apache Hive metastore and a script to run transformation jobs on a schedule.

D. Create an AWS Data Pipeline that transforms the data. Then, create an Apache Hive metastore and a script to run transformation jobs on a schedule.

## Answer

B – AWS Glue is the correct answer because this option requires the least amount of setup and maintenance since it is serverless, and it does not require management of the infrastructure. Refer to this link for supporting information. A, C, and D are all solutions that can solve the problem, but require more steps for configuration, and require higher operational overhead to run and maintain.

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

# AWS Sample Question #8

A Machine Learning Engineer is preparing a data frame for a supervised learning task with the Amazon SageMaker Linear Learner algorithm. The ML Engineer notices the target label classes are highly imbalanced and multiple feature columns contain missing values. The proportion of missing values across the entire data frame is less than 5%.

What should the ML Engineer do to minimize bias due to missing values?

A. Replace each missing value by the mean or median across non-missing values in same row.

B. Delete observations that contain missing values because these represent less than 5% of the data.

C. Replace each missing value by the mean or median across non-missing values in the same column.

D. For each feature, approximate the missing values using supervised learning based on other features.

## Answer

D – Use supervised learning to predict missing values based on the values of other features. Different supervised learning approaches might have different performances, but any properly implemented supervised learning approach should provide the same or better approximation than mean or median approximation, as proposed in responses A and C. Supervised learning applied to the imputation of missing values is an active field of research

# AWS Sample Question #9

A company has collected customer comments on its products, rating them as safe or unsafe, using decision trees. The training dataset has the following features: id, date, full review, full review summary, and a binary safe/unsafe tag. During training, any data sample with missing features was dropped. In a few instances, the test set was found to be missing the full review text field.

For this use case, which is the most effective course of action to address test data samples with missing features?

A. Drop the test samples with missing full review text fields, and then run through the test set.

B. Copy the summary text fields and use them to fill in the missing full review text fields, and then run through the test set.

C. Use an algorithm that handles missing data better than decision trees.

D. Generate synthetic data to fill in the fields that are missing data, and then run through the test set.

## Answer

B – In this case, a full review summary usually contains the most descriptive phrases of the entire review and is a valid stand-in for the missing full review text field.

# AWS Sample Question #10

An insurance company needs to automate claim compliance reviews because human reviews are expensive and error-prone. The company has a large set of claims and a compliance label for each. Each claim consists of a few sentences in English, many of which contain complex related information. Management would like to use Amazon SageMaker built-in algorithms to design a machine learning supervised model that can be trained to read each claim and predict if the claim is compliant or not.

Which approach should be used to extract features from the claims to be used as inputs for the downstream supervised task?

A. Derive a dictionary of tokens from claims in the entire dataset. Apply one-hot encoding to tokens found in each claim of the training set. Send the derived features space as inputs to an Amazon SageMaker built-in supervised learning algorithm.

B. Apply Amazon SageMaker BlazingText in Word2Vec mode to claims in the training set. Send the derived features space as inputs for the downstream supervised task.

C. Apply Amazon SageMaker BlazingText in classification mode to labeled claims in the training set to derive features for the claims that correspond to the compliant and non-compliant labels, respectively.

D. Apply Amazon SageMaker Object2Vec to claims in the training set. Send the derived features space as inputs for the downstream supervised task

## Answer

D – Amazon SageMaker Object2Vec generalizes the Word2Vec embedding technique for words to more complex objects, such as sentences and paragraphs. Since the supervised learning task is at the level of whole claims, for which there are labels, and no labels are available at the word level, Object2Vec needs be used instead of Word2Vec.

