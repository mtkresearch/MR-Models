import re
import os
import json
from typing import List, Dict
from functools import partial
from sumeval.metrics.rouge import RougeCalculator
from tqdm import tqdm

import numpy as np
import pandas as pd


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
    CHOICES = "ABCDE"

    def __init__(self, dir):
        super().__init__()
        self._prepare_data(dir)

    def _extract_choice(self, response):
        if len(response.strip()) == 0:
            return -1

        patterns = [
            r"^\s*([A-Ea-e])",
            r"^\s*\(([A-Ea-e])\)",
            r"^[選|选]\(*([A-Ea-e])\)*",
            r"^[選|选][項|项|擇|择]\(*([A-Ea-e])\)*",
            r"[選|选][擇|择]\s*\(*([A-Ea-e])\)*",
            r"答案[選|选][項|项|擇|择][為|为]\s*\(*([A-Ea-e])\)*",
            r"答案是\s?[選|选]?[項|项|擇|择]?\s?\(*([A-Ea-e])\)*",
            r"答案[為|为]\s?[選|选]?[項|项|擇|择]?\s?\(*([A-Ea-e])\)*",
            r"答案[應|应][為|为]\s?[選|选]?[項|项|擇|择]?\s?\(*([A-Ea-e])\)*",
            r"答案\s?[選|选]?[項|项|擇|择]?\s?\(*([A-Ea-e])\)*",
            r"答案是[：|:]*\s?[選|选]?[項|项|擇|择]?\s?\(*([A-Ea-e])\)*",
            r"答案[應|应][該|该]是[：|:]*\s?[選|选]?[項|项|擇|择]?\s?\(*([A-Ea-e])\)*",
            r"正[確|确]的[選|选|一][项|項][應|应|應該|应该]*是\s?\(*([A-Ea-e])\)*",
            r"正[確|确]的[项|項]是\s?\(*([A-Ea-e])\)*",
            r"正[確|确]的*[陳|陈]述[應|应][該|该]*是\s*\(*([A-Ea-e])\)*",
            r"答案[為|为][：|:]*\s?[選|选]?[項|项|擇|择]?\s?\(*([A-Ea-e])\)*",
            r"答案[應|应][為|为][：|:]*\s?[選|选]?[項|项|擇|择]?\s?\(*([A-Ea-e])\)*",
            r"答案[：|:]\s?[選|选]?[項|项|擇|择]?\s?\(*([A-Ea-e])\)*",
            r"答案是[：|:]*\s?[選|选]?[項|项|擇|择]?\s?\(*([A-Ea-e])\)*",
            r"答案[應|应][該|该]是[：|:]*\s?[選|选]?[項|项|擇|择]?\s?\(*([A-Ea-e])\)*",
            r"答案[為|为][：|:]\s?[選|选]?[項|项|擇|择]?\s?\(*([A-Ea-e])\)*",
            r"答案[應|应][為|为][：|:]*\s?[選|选]?[項|项|擇|择]?\s?\(*([A-Ea-e])\)*",
            r"答案[：|:]\s?[選|选]?[項|项|擇|择]?\s?\(*([A-Ea-e])\)*",
            r"答案可能是[：|:]*\s?[選|选]?[項|项|擇|择]?\s?\(*([A-Ea-e])\)*",
            r"答案[選|选][擇|择][：|:]*\s?[選|选]?[項|项|擇|择]?\s?\(*([A-Ea-e])\)*",
            r"答案[選|选][擇|择][：|:]*\s?[選|选]?[項|项|擇|择]?\s?\(*([A-Ea-e])\)*",
            r"[應|应][該|该]*[選|选][擇|择][：|:]*\s*\(*([A-Ea-e])\)*",
            r"[應該|应该]是[：|:]*\s*\(*([A-Ea-e])\)*",
            r"正確的敘述是[：|:]*\s*\(*([A-Ea-e])\)*",
            r"正確.{0,8}是[選項|选项|選擇|选择]*[：|:]*\s*\(*([A-Ea-e])\)*",
            r"最恰當的選項為[：|:]*\s*\(*([A-Ea-e])\)*",
            r"[選|选][項|项|擇|择]\s*[：|:]*\s*\(*([A-Ea-e])\)*\s*是*正[確|确]",
            r'\(*([A-Ea-e])\)*\s*[應該|应该]*[是|為|为]正[確|确]',
        ]
        found_set = set()
        for p in patterns:
            for char in re.findall(p, response):
                found_set.add(char.upper())
        if len(found_set) == 1:
            char = found_set.pop()
            return self.CHOICES.index(char.upper())  
        
        # when the response has only one english char and the char is A/B/C/D
        # high possible the char is the answer
        en_chars = re.findall(r'[a-zA-Z]', response)
        if len(en_chars) == 1:
            char = en_chars[0].upper()
            if char in self.CHOICES:
                return self.CHOICES.index(char.upper())  

        return -1

    def evaluate(self, list_of_response: List[Dict]) -> Dict:
        correct_list = []
        gold_dict= self._gold_dict

        response_dict = {}
        for data in list_of_response:
            response_dict[data['id']] = data['response']

        for idx in self._gold_dict.keys():
            choice = self._extract_choice(f'{idx}')
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
    def _prepare_data(self, dir):
        data = json.load(open(f'{dir}/TTQA_mc_1.0.0.json'))
        self._gold_dict = {}
        for idx in data:
            self._gold_dict[idx] = self.CHOICES.index(data[idx]['mc_answer'])


class TMMLUTask(MultipleChoiceTask):
    def _prepare_data(self, dir):
        df = pd.read_csv(f'{dir}/data.csv')
        self._gold_dict = {}
        for i, row in df.iterrows():
            self._gold_dict[i] = self.CHOICES.index(row['content.A'])


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
    # ['summarization_xsum_tc', XSumTCTask()],
    # ['drcd', DRCDTask()],
    # ['fgc', FGCTask()],
    # ['ttqa_mc', TTQATask('./data/TTQA/')],
    # *[[f'TMMLU_{subject}', TMMLUTask(f'./data/TMMLU/subjects/{subject}/')]
    #   for subject in os.listdir('./data/TMMLU/subjects/')],

]

def main(result_path):
    results = json.load(open(result_path))
    metrics = {}
    for name, task in EVALUATION_ITEMS:
        list_of_response = results['results'][name]
        metrics[name] = task.evaluate(list_of_response)
    print(metrics)
    print(np.mean([metrics[k]['accuracy'] for k in metrics if 'TMMLU' in k]))


if __name__ == '__main__':
    result_path = 'results/model_7c_chat_result.json'
    main(result_path)
