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
