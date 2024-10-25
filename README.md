# Multilingual Meta-EVALuation benchmark (MM-Eval)



<p align="center">
<b><a href="https://huggingface.co/datasets/prometheus-eval/MM-Eval">🤗 MM-Eval</a></b>
|
<b><a href="https://arxiv.org/abs/2410.15522">📄Paper</a></b>
|
<b><a href="https://huggingface.co/datasets/prometheus-eval/MMQA">🤗 MMQA</a></b>
</p>

**MM-Eval** is a multilingual meta-evaluation benchmark consisting of five core subsets—Chat, Reasoning, Safety, Language Hallucination, and Linguistics—spanning 18 languages and a Language Resource subset spanning 122 languages for a broader analysis of language effects. 

> **Design Choice**  
> In this work, we minimize the inclusion of translated samples, as mere translation may alter existing preferences due to translation errors. Instead, we increase the proportion of linguistically and culturally related instances. Consequently, translated samples are only included in the Safety subset. Additionally, we enrich the dataset with a Linguistics subset designed to evaluate the judge model's ability to comprehend the linguistic characteristics of various languages accurately. Furthermore, we incorporate hand-crafted culturally related prompts in the Language Hallucination subset. If you are interested, please look into [MMQA (Multilingual, Multicultural Question Answering)](https://huggingface.co/datasets/prometheus-eval/MMQA).

### This is a fork of the [RewardBench codebase](https://github.com/allenai/reward-bench).
If you use our code in your work, please consider citing both [our work](https://arxiv.org/abs/2410.15522) and [RewardBench](https://arxiv.org/abs/2403.13787). Many thanks to the original authors of RewardBench. 

## How to Use
You can replicate our experiments by following the process outlined below.

### Installation
```python
git clone https://github.com/guijinSON/MM-Eval
cd MM-Eval

pip install -e .
```
:warning: `pip install reward-bench` will not work

### Evaluating Reward Models
Run this for evaluation on MM-Eval
```bash
python scripts/run_rm.py --model=prometheus-eval/MM-Mistral-7B-RM --custom_dataset_path prometheus-eval/MM-Eval
```
Ensure your model fits on the GPU. If not, reduce the batch size:

```bash
--batch_size 1
```

For some models, you may also need to add the following flag:

```bash
--trust_remote_code
```

### Evaluating Proprietary Models
First, add your OpenAI API key:
```bash
export OPENAI_API_KEY="{your-api-key}"
```
Then, run this for evaluation on MM-Eval
```bash
python scripts/run_generative.py --model=gpt-4o-mini-2024-07-18 --custom_dataset_path prometheus-eval/MM-Eval
```

### Evaluating Prometheus2.0 and Self-Taught Evaluator
For [Prometheus-2](https://huggingface.co/prometheus-eval/prometheus-7b-v2.0) and [Self-Taught Evaluator](https://huggingface.co/facebook/Self-taught-evaluator-llama3.1-70B) we use their original implementations instead of the Reward-Bench codebase. Tutorials to replicate the experiments will be added shortly.

### Analysis
Notebooks for replicating the experiment and plot in Section 6. Analysis is in the ```analysis``` folder.

## How to Cite
```
[TBD]
```
