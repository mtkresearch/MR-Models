# TC-Eval

TC-Eval is a Traditional Chinese evaluation suite for foundation models. It covers 5 capabilities, including contextual QA, world knowledge, summarization, classification, and table understanding. You may check [our paper](https://arxiv.org/abs/2309.08448) for more details.


## Evaluate your models

1. `pip install -r requirements.txt`

2. Please follow the instruction in `data/DRCD_Test/README.md` and `data/FGC/README.md` to prepare the dataset DRCD and FGC.

3. Put your results in `results/{MODEL_NAME}_result.json` with the format as following:

```json
{
  "name": "MODEL_NAME",
  "results": {
    "ttqa_mc": [
      {
        "id": "0",
        "query": "...",
        "response": "..."
      },
      {
        "id": "1",
        "query": "...",
        "response": "..."
      },
      ...
    ],
    "TMMLU_會考國文": [
      {
        "id": "0",
        "query": "...",
        "response": "..."
      },
      {
        "id": "1",
        "query": "...",
        "response": "..."
      },
      ...
    ],
    ...
  }
}
```

4. Run evaluation with `python evaluate.py`


## Citation

```
@misc{hsu2023advancing,
    title={Advancing the Evaluation of Traditional Chinese Language Models: Towards a Comprehensive Benchmark Suite}, 
    author={Chan-Jan Hsu and Chang-Le Liu and Feng-Ting Liao and Po-Chun Hsu and Yi-Chang Chen and Da-shan Shiu},
    year={2023},
    eprint={2309.08448},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```
