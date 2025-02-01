# Model Deployment Strategies

This blog is a refactor of [this blog](https://neptune.ai/blog/model-deployment-strategies), so I didn't write it (except the questions at the end). I wanted to refactor it so that I can organize it in my mind.

**We can summarize "ML Model Development Lifecycle" in 5 steps:** 

1. Data collection
2. Create model and training
3. Testing and evaluation
4. Deployment and production
5. Monitoring

**What is Model Deployment (or Model Release)?**

Model deployment (release) is a process that enables you to integrate machine learning models into production to make decisions on real-world data.

---

We will cover the following strategies and techniques for model deployment:

1. Shadow evaluation
2. A/B testing
3. Multi Arm Bandits
4. Blue-green deployment
5. Canary testing
6. Feature flag
7. Rolling deployment
8. Recreate strategy

These strategies can be broken down into two categories:

|Distribution of Traffic| Strategies                                                                  |
| ---                   | ---                                                                         |
|Static                 | A/B testing<br/>Canary testing<br/>Shadow deployment<br/>Blue-green         |
|Dynamic                | Multi Arm Bandits                                                           |

## 1. Shadow deployment strategy

In shadow evaluation, the request is sent to both the models running parallel to each other using two API endpoints. During the inference, predictions from both the models are computed and stored, but only the prediction from the live model is used in the application which is returned to the users.

## 2. A/B testing model deployment strategy

In A/B testing there are two types of hypothesis; *Null Hypothesis* and *Alternate Hypothesis*. If the alternate hypothesis is accepted and the null hypothesis is rejected then that feature is added and the new model is deployed globally. It is important to know that in order to reject the null hypothesis you have to prove the *statistical significance* of the test.

## 3. Multi Armed Bandit

Multi-Armed Bandit or MAB is an advanced version of A/B testing. It is also inspired by reinforcement learning, and the idea is to explore and exploit the environment that maximizes the reward function.

## 4. Blue-green deployment strategy

In Blue-green deployment, the two identical environments consist of the same database, containers, virtual machines, same configuration et cetera. The Blue environment which contains the original model is live and keeps servicing requests while the Green environment acts as a staging environment for a new version of the model. Once the testing is successfully completed ensuring that all the bugs and issues are rectified the new model is made live.

## 5. Canary deployment strategy

Design a new model and route a small sample of users’ requests to the new model. Check for bugs, efficiency, reports, and issues in the new model, if found then perform a rollback. Repeat steps one and two until all errors and issues are resolved, before routing all traffic to the new model.

|Strategy               | Pros                                                                                                                              | Cons                                                         |
| ---                   | ---                                                                                                                               | ---                                                          |
|Shadow deployment      | - Model evaluation is efficient<br/>- No overloading irrespective of the traffic<br/>- Reduced risk for stability and performance | - Expensive<br/>- Can be tedious<br/>- No user response data |
|A/B testing            | - Simple <br/>- Quick results                                                                                                     | - Unreliable in complex cases                                |
|Multi Armed Bandit     | - Adaptive testing<br/>- Resource efficient (compared to A/B)<br/>- Fast                                                          | - Expensive                                                  |
|Blue-green deployment  | - Ensures application availability<br/>- Easy rollbacks<br/>- Less deployment risk                                                | - Costly                                                     |
|Canary deployment      | - Cheaper compared to Blue-Green<br/>- Ease to test the new model against real data<br/>- Zero downtime<br/>- Easy rollback       | - Slow rollout<br/>- proper monitoring must be in place      |

|Strategy               | When to use it?                                                                                                                                                                                               |
| ---                   | ---                                                                                                                                                                                                           |
|Shadow deployment      | - If you want to compare multiple models with each other<br/>- Evaluate the pipeline, latency while yielding results as well the load-bearing capacity.                                                       |
|A/B testing            | - If you have two models you can use A/B to evaluate and choose which one to deploy globally.<br/>- A/B testing is predominantly used for e-commerce, social media platforms, and online streaming platforms. |
|Multi Armed Bandit     | - When the conversion rate is the primary concern and decisions need to be made quickly.                                                                                                                      |
|Blue-green deployment  | - When your application cannot afford downtime and you want a seamless transition from the old version to the new one.                                                                                        |
|Canary deployment      | - When you want to evaluate the new model or version against real-world, real-time data.<br/>- When you want to detect and resolve potential issues before deploying globally, without causing downtime.      |

## 6. Other model deployment strategies and techniques

### Feature Flag:

Feature flags are a technique that allows developers to control the activation of specific features or code changes within an application. These features can be kept dormant until they are fully ready for activation. Feature flags enable collaborative development, testing, and gradual feature rollout, making them versatile in combination with other deployment techniques.

### Rolling Deployment:

Rolling deployment is a strategy that involves gradually updating and replacing the older version of a software application or system with a new version. This deployment occurs in a running instance and does not require staging or private development environments. It is characterized by horizontally scaling the service and updating instances one by one, ensuring continuous availability.

### Recreate Strategy:

The recreate strategy is a straightforward approach where the live version of a software application or model is shut down entirely, and the new version is deployed from scratch. This strategy offers simplicity and a complete renewal of the environment but may involve temporary downtime during the transition.

## Comparison: which model release strategy to use?

| Deployment or testing pattern | Zero downtime | Real production traffic testing | Releasing to users based on conditions | Rollback duration  | Impact on hardware and cloud costs                                                   |
|-------------------------------|---------------|---------------------------------|----------------------------------------|--------------------|--------------------------------------------------------------------------------------|
| Shadow                        | ✓             | ✓                               | ✗                                      | Does not apply     | Need to maintain parallel environments in order to capture and replay user requests  |
| A/B                           | ✓             | ✓                               | ✓                                      | Fast               | No extra setup required                                                              |
| Blue/green                    | ✓             | ✗                               | ✗                                      | Instant            | Need to maintain blue and green environments simultaneously                          |
| Canary                        | ✓             | ✓                               | ✗                                      | Fast               | No extra setup required                                                              |
| Multi-Armed Bandit (MAB)	    | ✓             | ✓	                              | ✗	                                   | Fast	            | Can be computationally expensive                                                     |

---

**After reading this blog, I had these 2 questions, so I thought it would be nice if I put the answers:**

1. Canary deployment vs A/B testing

Canary deployment focuses on the gradual introduction of a new version into a real-world environment, allowing for early issue detection and quick rollbacks if problems arise. It's designed for minimizing risks during production deployments and ensuring a smooth transition to a new version.

In contrast, A/B testing is centered around comparing different variations (A and B) to optimize user experiences and metrics. Users are divided into groups, and performance is measured to determine the most effective variation. Unlike canary deployment, A/B testing doesn't include a rollback mechanism; its primary goal is to select the best-performing variation for improving user engagement and conversion rates.

2. Blue-Green vs Shadow Deployment

Blue-green deployment focuses on minimizing downtime during the release of new versions by maintaining two identical environments and allows for quick rollbacks. It does not involve real-world testing with production traffic.

In contrast, shadow deployment is used for testing and evaluating new versions without affecting the live environment. It involves running both the existing live version and the new version simultaneously, using real-world data for evaluation. Shadow deployment does not include a quick rollback mechanism and is primarily focused on testing and evaluation.

## References

- [Model Deployment Strategies](https://neptune.ai/blog/model-deployment-strategies)

