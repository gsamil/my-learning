# CLIP: Contrastive Language-Image Pretraining

- Paper by [Alec Radford](https://twitter.com/alecrad), [Ilya Sutskever](https://twitter.com/ilyasut) et al. from OpenAI

## What is it?

- Task agnostic pre-training on internet scale natural language has powered a breakthrough in NLP
- This paper observes if it can also be leveraged to improve the performance of computer vision.

## Training Approach

- Method uses an abundantly available source of supervision: the text paired with images found across the internet.
- This data is used to create the following proxy training task for CLIP: given an image, predict which out of a set of 32,768 randomly sampled text snippets, was actually paired with it in the dataset.

## Advantages

- CLIP learns from text–image pairs that are already publicly available on the internet. Reducing the need for expensive large labeled datasets
- CLIP can be adapted to perform a wide variety of visual classification tasks without needing additional training examples.
- There is a smaller gap between “benchmark performance” and “real performance.”

## Key Takeaways

- CLIP is highly efficient.
  - adoption of a contrastive objective for connecting text with images
  - adoption of the Vision Transformer
- CLIP models are significantly more flexible and general than existing ImageNet models.

## What are the limitations?

- It struggles on more abstract or systematic tasks such as counting the number of objects in an image and on more complex tasks such as predicting how close the nearest car is in a photo.
- Zero-shot CLIP also struggles compared to task specific models on very fine-grained classification, such as telling the difference between car models, variants of aircraft, or flower species.
- CLIP also still has poor generalization to images not covered in its pre-training dataset.
- CLIP’s zero-shot classifiers can be sensitive to wording or phrasing and sometimes require trial and error “prompt engineering” to perform well.

## What are broader impacts?

- CLIP allows people to design their own classifiers and removes the need for task-specific training data. 
- Given that CLIP does not need task-specific training data it can unlock certain niche tasks with greater ease.

## References

- [OpenAI blog](https://openai.com/research/clip)
- [Paper](https://arxiv.org/pdf/2103.00020.pdf)
