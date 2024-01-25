# Recommendation Systems and Factorization Machines

## Recommender System - Challenges and Dynamics (Lesson 140)
- Newly launched products may struggle to be recognized due to a lack of reviews or ratings.
- Large user and product bases, lead to a high volume of data that is sparsely distributed.
- Limited ratings or reviews from users.
- Recommendations may sometimes be irrelevant, like suggesting car wipers repeatedly after a single purchase.
- Continuous changes in products and user reviews necessitate frequent model retraining.

## Introduction to Factorization Machines (Lesson 142)

- A prediction algorithm effective in handling sparse, high-dimensional datasets.
- Recommender system models are rebuilt periodically to capture new preferences and interactions, often in a matter of hours or days.
- Factorization Machines automatically identify pairwise feature interactions in linear time.
- The algorithm is capable of handling large sparse datasets efficiently.

### Data Format
- Input:
    - recordIO-protobuf (with float32 values)
- Output:
    - JSON
    - recordIO-protobuf
