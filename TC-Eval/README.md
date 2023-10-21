# TC-Eval

TC-Eval is a Traditional Chinese evaluation suite for foundation models. It covers 5 capabilities, including contextual QA, knowledge, summarization, classification, and table understanding. You may find datasets in [`./data`](./data/) and check [our paper](https://arxiv.org/abs/2309.08448) for more details.

## Benchmark

- **Contextual QA**
  - **DRCD** [[1]](#1): DRCD is a Traditional Chinese machine reading comprehension dataset containing 10,014 paragraphs from 2,108 Wikipedia articles and over 30,000 questions. 
  - **FGC** [[2]](#2): FGC dataset is a passage question answering dataset of 750 samples created from Taiwanese news articles and government announcements.
- **Knowledge**
  - **TTQA** (provided by MediaTek Research, [[3]](#3)): TTQA is for assessing language models’ common sense abilities on Taiwanese terms, comprising 64 passages from Wikipedia about diverse Taiwanese cultural topics, necessitating model comprehension and reasoning. 
  - **TMMLU** (provided by MediaTek Research, [[4]](#4)): Taiwan Massive Multitask Language Understanding (TMMLU) is curated from examinations in Taiwan, consisting of 55 subjects spanning across multiple disciplines, from vocational to academic fields, and covering elementary to professional proficiency levels. It is designed to identify a model’s knowledge and problem-solving blind spots similar to human evaluations.
- **Summarization**
  - **XSum-TC** (translate from [[5]](#5)): Extreme Summarization (XSum) dataset evaluates abstractive summarization with 226,711 BBC news articles across diverse domains, aiming for one-sentence summaries.
- **Classification**
  - **IMDB-TC** (translate from [[6]](#6)): IMDB dataset offers binary sentiment classification with 25,000 polar movie reviews each for training and testing sentiment classifiers.
- **Table Understanding**
  - **Penguins-in-a-Table-TC** (translate from [[7]](#7)): The “penguins in a table” task contained in BIG-bench asks a language model to answer questions about the animals contained in a table, or multiple tables, described in the context.

reference:

<a id="1">[1]</a> Chih Chieh Shao, Trois Liu, Yuting Lai, Yiying Tseng, and Sam Tsai. DRCD: A Chinese machine reading comprehension dataset, 2019.

<a id="2">[2]</a> STPI. 2020 「科技大擂台與AI對話」訓練資料集, 2020.

<a id="3">[3]</a> Philipp Ennen, Po-Chun Hsu, Chan-Jan Hsu, Chang-Le Liu, Yen-Chen Wu, Yin-Hsiang Liao, Chin-Tung Lin, Da-Shan Shiu, and Wei-Yun Ma. Extending the pre-training of bloom for improved support of Traditional Chinese: Models, methods and results, 2023.

<a id="4">[4]</a> Chan-Jan Hsu, Chang-Le Liu, Feng-Ting Liao, Po-Chun Hsu, Yi-Chang Chen, and Da-shan Shiu. Advancing the Evaluation of Traditional Chinese Language Models: Towards a Comprehensive Benchmark Suite, 2023.

<a id="5">[5]</a> Shashi Narayan, Shay B. Cohen, and Mirella Lapata. Don’t give me the details, just the summary! topic- aware convolutional neural networks for extreme summarization. ArXiv, abs/1808.08745, 2018.

<a id="6">[6]</a> Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, and Christopher Potts. Learning word vectors for sentiment analysis. In Proceedings of the 49th Annual Meeting of the Associ- ation for Computational Linguistics: Human Language Technologies, pages 142–150, Portland, Oregon, USA, June 2011. Association for Computational Linguistics.

<a id="7">[7]</a> BIG-bench authors. Beyond the imitation game: Quantifying and extrapolating the capabilities of language models. Transactions on Machine Learning Research, 2023. ISSN 2835-8856.

## Evaluate your models

1. `pip install -r requirements.txt`

2. Please follow the instruction in `data/DRCD_Test/README.md` and `data/FGC_Test/README.md` to prepare the dataset DRCD and FGC.

3. Put your results in `results/{MODEL_NAME}_result.json` with the format as following:

```json
{
  "name": "MODEL_NAME",
  "results": {
    "TTQA": [
      {
        "id": "0",
        "response": "..."
      },
      {
        "id": "1",
        "response": "..."
      },
      ...
    ],
    "TMMLU_會考國文": [
      {
        "id": "0",
        "response": "..."
      },
      {
        "id": "1",
        "response": "..."
      },
      ...
    ],
    ...
  }
}
```

4. Run evaluation with `python evaluate.py`

## Generation

We provide generation scripts in `inference/`. See `inference/run.sh` for an example of the usage.

We recommend launching a [`TGI` service](https://huggingface.co/docs/text-generation-inference/main/en/index) to send queries to model. You can set this in a config dictionary. For example, in `inference/tasks_config.json`, replace `api_base` field with your own local server address.


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
