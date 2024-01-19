# Alignment Problem

## [1. What is the alignment problem?](https://aligned.substack.com/p/what-is-alignment)

There are 2 reasons why an AI system may fail:

1. Capability : System is not capable to do the intended task.
2. Alignment : System is not aligned well to do the intended task.

Today, we align large large models by fine-tuning them with specifically curated datasets. (See [InstructGPT](https://openai.com/blog/instruction-following/))

### Problem

How can we align a model to do the intended task; if task is difficult for humans to evaluate?

### Not-Answer

[RL from human feedback (RLHF)](https://www.deepmind.com/blog/learning-through-human-feedback) doesn’t apply here because model might be fooling us in ways that are hard for us to detect, ie. it won’t scale.

### Possible-Answer

Can we train the AI to assist humans in evaluation?

[Recursive Reward Modeling (RRM)](https://deepmindsafetyresearch.medium.com/scalable-agent-alignment-via-reward-modeling-bf4ab06dfd84) is an extension to the RLHF. 

1. If the task is easy for humans to evaluate; use RLHF.
2. If task is hard, then we will create new tasks (evaluation assistance tasks) to evaluate the original task easier.

So, instead of aligning the model to the difficult tasks, we will align it to evaluation assistance tasks.

Think of book summarization. Instead of trying to summarize all of the book, we need to summarize each chapter, then get a summary from these.

### a question to the possible answer

How far can we push this idea? ie. What is the largest set of tasks that we can align our models on by training evaluation assistance?

We can also leverage our model’s ability to generalize to make expensive evaluation a lot cheaper.

### Ground Truth problem

We would like to reach a ground truth using human evaluations. (this is not feasible)

### Ground Truth solution

We would like to automate the cognitive labor required for evaluation; so human evaluators can focus more on preference input more.

## Next : **[What is inner alignment?](https://aligned.substack.com/p/inner-alignment)**

## References

1. [Musings on the Alignment Problem](https://aligned.substack.com/) (Jan Leike)
2. [InstructGPT](https://openai.com/blog/instruction-following/) (RLHF to align GPT-3 with human intent) (27.01.2022)
3. [RL from human feedback (RLHF)](https://www.deepmind.com/blog/learning-through-human-feedback) (12.06.2017)
4. [Recursive Reward Modeling (RRM)](https://deepmindsafetyresearch.medium.com/scalable-agent-alignment-via-reward-modeling-bf4ab06dfd84) (20.11.2018)
5. [A survey of tool use and workflows in alignment research](https://www.alignmentforum.org/posts/ebYiodG3MAEqskCDG/a-survey-of-tool-use-and-workflows-in-alignment-research-1)
