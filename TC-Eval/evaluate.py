import re
import json
from typing import List, Dict
from functools import partial
from sumeval.metrics.rouge import RougeCalculator
from tqdm import tqdm

import numpy as np


def prefix_exact_match(gold: str, pred: str) -> float:
    if not pred:
        return 0
    
    return 1 if pred.strip().startswith(gold.strip()) else 0


def rouge_tc_score(gold: str, pred: str, rouge_type: str, scorer: RougeCalculator) -> float:
    if rouge_type == "rouge1":
        return scorer.rouge_1(summary=gold, references=pred)
    elif rouge_type == "rouge2":
        return scorer.rouge_2(summary=gold, references=pred)
    elif rouge_type == "rougeL":
        return scorer.rouge_l(summary=gold, references=pred)
    else:
        raise KeyError(f"No rouge_type = {rouge_type}")


def get_rouge_tc_function(rouge_type: str = "rouge2") -> callable:
    scorer = RougeCalculator(stemming=True, lang="zh")
    return partial(rouge_tc_score, scorer=scorer, rouge_type=rouge_type)


class Task:
    def evaluate(self, list_of_response: List[Dict]) -> Dict:
        raise NotImplementedError
        # return metrics


class MultipleChoiceTask(Task):
    def _extract_choice(self, response):
        raise NotImplementedError

    def evaluate(self, list_of_response: List[Dict]) -> Dict:
        correct_list = []
        gold_dict= self._gold_dict

        response_dict = {}
        for data in list_of_response:
            response_dict[data['id']] = data['response']

        for idx in self._gold_dict.keys():
            choice = self._extract_choice(response_dict[f'id{idx}'])  # TODO: walk-around  
            correct_list.append(1 if choice == gold_dict[idx] else 0)
        return {
            'accuracy': np.mean(correct_list)
        }


class QuestionAnsweringTask(Task):
    def __init__(self) -> None:
        self._metric_fns = {"prefix_exact_match": prefix_exact_match}
    
    def evaluate(self, list_of_response: List[Dict]) -> Dict:
        metrics = {}
        for m_name, metric_fn in self._metric_fns.items():
            vals = []
            for inst in tqdm(list_of_response, desc=f"Calculate {m_name}"):
                references = inst["references"]
                pred = inst["response"]
                vals.append(np.max([metric_fn(ref, pred) for ref in references]))
            metrics[m_name] = np.mean(vals)
        return metrics


class SummaryTask(Task):
    def __init__(self):
        self._metric_fns = {"rouge1": get_rouge_tc_function("rouge1"),
                            "rouge2": get_rouge_tc_function("rouge2"),
                            "rougeL": get_rouge_tc_function("rougeL")}
        
    def evaluate(self, list_of_response: List[Dict]) -> Dict:    
        metrics = {}
        for m_name, metric_fn in self._metric_fns.items():
            vals = []
            for inst in tqdm(list_of_response, desc=f"Calculate {m_name}"):
                references = inst["references"]
                pred = inst["response"]
                vals.append(np.max([metric_fn(ref, pred) for ref in references]))
            
            metrics[m_name] = np.mean(vals)
        return metrics


class TTQATask(MultipleChoiceTask):
    CHOICES = "ABCDEF"

    def __init__(self, dir):
        self._prepare_data(dir)

    def _prepare_data(self, dir):
        data = json.load(open(f'{dir}/TTQA_mc_1.0.0.json'))
        self._gold_dict = {}
        for idx in data:
            self._gold_dict[idx] = TTQATask.CHOICES.index(data[idx]['mc_answer'])

    def _extract_choice(self, response):
        if len(response.strip()) == 0:
            return -1
        if response.lstrip()[0] in TTQATask.CHOICES:
            return TTQATask.CHOICES.index(response.lstrip()[0])
        
        patterns = [
            r'答案[：:]\s*([ABCDE])',
            r'([ABCDE])'
        ]
        for p in patterns:
            found_list = re.findall(p, response)
            if len(found_list) == 1:
                char = found_list[0]
                return TTQATask.CHOICES.index(char)

        return -1


class XSumTCTask(SummaryTask):
    def __init__(self):
        super().__init__()


class DRCDTask(QuestionAnsweringTask):
    def __init__(self) -> None:
        super().__init__()


class FGCTask(QuestionAnsweringTask):
    def __init__(self) -> None:
        super().__init__()

EVALUATION_ITEMS = [
    # ('ttqa_mc', TTQATask('./data/TTQA/')),
    ('summarization_xsum_tc', XSumTCTask()),
    ('drcd', DRCDTask()),
    ('fgc', FGCTask())
]

def main(result_path):
    results = json.load(open(result_path))
    metrics = {}
    for name, task in EVALUATION_ITEMS:
        list_of_response = results['results'][name]
        metrics[name] = task.evaluate(list_of_response)
        print(metrics)


if __name__ == '__main__':
    result_path = 'results/model_7c_chat_result.json'
    main(result_path)