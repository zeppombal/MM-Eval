 # Multilingual Meta-EVALuation benchmark (MM-Eval)

<p align="center">
<b><a href="https://huggingface.co/datasets/prometheus-eval/MM-Eval">🤗 Dataset</a></b>
|
<b><a href="https://arxiv.org/abs/2410.15522">📄Paper</a></b>
</p>

**MM-Eval** is a multilingual meta-evaluation benchmark consisting of five core subsets—Chat, Reasoning, Safety, Language Hallucination, and Linguistics—spanning 18 languages and a Language Resource subset spanning 122 languages for a broader analysis of language effects. 

> **Design Choice**  
> In this work, we minimize the inclusion of translated samples, as mere translation may alter existing preferences due to translation errors. Instead, we increase the proportion of linguistically and culturally related instances. Consequently, translated samples are only included in the Safety subset. Additionally, we enrich the dataset with a Linguistics subset designed to evaluate the judge model's ability to comprehend the linguistic characteristics of various languages accurately. Furthermore, we incorporate hand-crafted culturally related prompts in the Language Hallucination subset. If you are interested, please look into [MMQA (Multilingual, Multicultural Question Answering)](https://huggingface.co/datasets/prometheus-eval/MMQA).

## How to Use.
In general, we leverage the codebase from Reward-Bench for our experiments. You can replicate our experiments by following the process outlined below.

### Installation
```python
git clone https://github.com/guijinSON/MM-Eval
cd MM-Eval
cd reward-bench

pip install rewardbench
pip install rewardbench[generative]
```

### Installation
