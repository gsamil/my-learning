# 140. Recommender System

## Introduction to Recommender Systems
- **Definition**: Recommender Systems are specialized machine learning systems tailored for personalized recommendations.
- **Characteristics**:
  - **Personalization**: Recommendations are unique to each user.
  - **New Product Recognition Issue**: Newly launched products may struggle to be recognized due to a lack of reviews or ratings.
  - **High Cardinality and Sparse Data**: Large user and product bases, like Amazon's, lead to a high volume of data that is sparsely distributed.

## Challenges and Dynamics
- **Sparse User Interactions**: Despite limited ratings or reviews from users, recommender systems need to show relevant products.
- **Collaborative Filtering**: This method suggests products by learning from the preferences of similar users.
- **Predictive Modelling**: The algorithm predicts user preferences for specific items.
- **Inconsistent Recommendations**: Recommendations may sometimes be irrelevant, like suggesting car wipers repeatedly after a single purchase.
- **Data Fluidity**: Continuous changes in products and user reviews necessitate frequent model retraining.

## Implementing Recommender Systems in SageMaker
- **Key Algorithm**: Factorization Machines are widely used for building effective recommender systems.
- **Application**: The course will cover building and deploying a recommender system using SageMaker with a real-world dataset.

# 142. Introduction to Factorization Machines

## Overview of Factorization Machines
- **Definition**: A prediction algorithm effective in handling sparse, high-dimensional datasets.
- **Applications**: Commonly used in ad placement strategies (based on historical click rates) and recommender systems (for personalizing content).

## Factorization Machines and Recommender Systems
- **Content Personalization**: Recommender systems use Factorization Machines for suggesting products, movies, and prioritizing user-relevant content on social media.
- **Similarities to PCA**: Like PCA, Factorization Machines can capture interactions between various features using factorized parameters.

## Example by Rendle
- **Paper Reference**: Developed by Rendle, the paper illustrates the algorithm with a movie rating example.
- **User-Movie Interaction**: The example involves predicting if users Alice or Charlie would like the movie 'Star Trek', based on their ratings of other movies.
- **Feature Interaction**: Analysis of user-movie, user-user, and movie-movie interactions to predict preferences.
- **Predictive Capability**: The ability to predict user preferences for unrated items based on similar interactions and preferences.

## Rebuilding and Updating Models
- **Periodic Rebuilding**: Recommender system models are rebuilt periodically to capture new preferences and interactions, often in a matter of hours or days.
- **Automatic Feature Interaction**: Factorization Machines automatically identify pairwise feature interactions in linear time.
- **Handling Large Datasets**: The algorithm is capable of handling large sparse datasets efficiently.

## Data Format and AWS SageMaker
- **Data Representation**: Users and movies are represented using one-hot encoding in sparse datasets.
- **RecordIO Format**: AWS SageMaker requires training data in RecordIO format, with float32 values.
- **Prediction Requests**: Accepts either JSON or RecordIO formatted payload.
- **Resource Links**: Includes the Factorization Machine paper by Rendle, LibFM software, and other resources for further study.

## Hands-On Exercise
- **Building a Movie Recommendation System**: Using the MovieLens dataset.
- **Data Download**: Ensure the dataset is downloaded for the upcoming exercise.
- **Next Steps**: The following lecture will focus on constructing the movie recommendation system.
