import re
import os
import json
from typing import List, Dict
from functools import partial
from glob import glob

from sumeval.metrics.rouge import RougeCalculator
import numpy as np
import pandas as pd


def prefix_exact_match(gold: str, pred: str) -> float:
    if not pred:
        return 0
    
    return 1 if pred.strip().startswith(gold.strip()) else 0


def rouge_tc_score(gold: str, pred: str, rouge_type: str, scorer: "RougeCalculator") -> float:
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
    def __init__(self, dir):
        self._prepare_data(dir)

    def _prepare_data(self, dir):
        # create self._gold_dict
        raise NotImplementedError
    
    def _get_response_dict(self, list_of_response):
        response_dict = {}
        for data in list_of_response:
            response_dict[str(data['id'])] = data['response']
        return response_dict

    def evaluate(self, list_of_response: List[Dict]) -> Dict:
        # return metrics
        raise NotImplementedError


class ChoiceTask(Task):
    CHOICES = None

    def _extract_choice(self, response):
        raise NotImplementedError
    
    def evaluate(self, list_of_response: List[Dict]) -> Dict:
        correct_list = []
        gold_dict= self._gold_dict

        response_dict = self._get_response_dict(list_of_response)

        for idx in self._gold_dict.keys():
            choice = self._extract_choice(response_dict[idx])
            correct_list.append(1 if choice == gold_dict[idx] else 0)
        return {
            'accuracy': np.mean(correct_list)
        }


class MultipleChoiceTask(ChoiceTask):
    CHOICES = "ABCDE"

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


class QuestionAnsweringTask(Task):
    _metric_fns = {"prefix_exact_match": prefix_exact_match}
    
    def evaluate(self, list_of_response: List[Dict]) -> Dict:
        gold_dict= self._gold_dict
        response_dict = self._get_response_dict(list_of_response)

        metrics = {}
        for m_name, metric_fn in self._metric_fns.items():
            vals = []
            for idx in self._gold_dict.keys():
                references = gold_dict[idx]
                pred = response_dict[idx]
                vals.append(np.max([metric_fn(ref, pred) for ref in references]))
            metrics[m_name] = np.mean(vals)
        return metrics


class SummaryTask(Task):
    _metric_fns = {"rouge1": get_rouge_tc_function("rouge1"),
                   "rouge2": get_rouge_tc_function("rouge2"),
                   "rougeL": get_rouge_tc_function("rougeL")}

    def evaluate(self, list_of_response: List[Dict]) -> Dict:
        gold_dict= self._gold_dict
        response_dict = self._get_response_dict(list_of_response)

        metrics = {}
        for m_name, metric_fn in self._metric_fns.items():
            vals = []
            for idx in self._gold_dict.keys():
                vals.append(metric_fn(gold_dict[idx], response_dict[idx]))
            metrics[m_name] = np.mean(vals)
        return metrics


class TTQATask(MultipleChoiceTask):
    def _prepare_data(self, dir):
        data = json.load(open(f'{dir}/TTQA_mc_1.0.0.json'))
        self._gold_dict = {}
        for idx in data:
            self._gold_dict[str(idx)] = self.CHOICES.index(data[idx]['mc_answer'])


class TMMLUTask(MultipleChoiceTask):
    def _prepare_data(self, dir):
        df = pd.read_csv(f'{dir}/data.csv')
        self._gold_dict = {}
        for i, row in df.iterrows():
            self._gold_dict[str(i)] = self.CHOICES.index(row['content.A'])


class IMDBTCTask(ChoiceTask):
    CHOICES = '負正'

    def _prepare_data(self, dir):
        df = pd.read_csv(f'{dir}/test.csv')
        self._gold_dict = {}
        for i, row in df.iterrows():
            self._gold_dict[str(i)] = int(row['label'])

    def _extract_choice(self, response):
        if len(response.strip()) == 0:
            return -1

        patterns = [
            r"^\s*([正|負])面",            
        ]
        found_set = set()
        for p in patterns:
            for char in re.findall(p, response):
                found_set.add(char)
        if len(found_set) == 1:
            char = found_set.pop()
            return self.CHOICES.index(char)  

        return -1


class XSumTCTask(SummaryTask):
    def _prepare_data(self, dir):
        df = pd.read_csv(f'{dir}/test_sub5000.csv')
        self._gold_dict = {}
        for i, row in df.iterrows():
            self._gold_dict[str(i)] = str(row['summary'])


class DRCDTask(QuestionAnsweringTask):
    def _prepare_data(self, dir):
        data = json.load(open(f'{dir}/preprocessed_DRCD_test.json'))
        self._gold_dict = {}
        for idx in data:
            self._gold_dict[str(idx)] = data[idx]['references']


class FGCTask(QuestionAnsweringTask):
    def _prepare_data(self, dir):
        raise NotImplementedError


EVALUATION_ITEMS = [
    ['summarization_xsum_tc', XSumTCTask('./data/XSum_TC_5k/')],
    ['drcd', DRCDTask('./data/DRCD_Test/')],
    # ['fgc', FGCTask()],
    ['ttqa_mc', TTQATask('./data/TTQA/')],
    ['imdb_tc_sub5000', IMDBTCTask('./data/IMDB_TC/')],
    *[[f'TMMLU_{subject}', TMMLUTask(f'./data/TMMLU/subjects/{subject}/')]
      for subject in os.listdir('./data/TMMLU/subjects/')]
]


def evaluate_all(result_path):
    results = json.load(open(result_path))
    metrics = {}
    for name, task in EVALUATION_ITEMS:
        list_of_response = results['results'][name]
        metrics[name] = task.evaluate(list_of_response)
    return metrics


if __name__ == '__main__':
    for path in glob('results/*_result.json'):
        print(f'== {path} ==')
        metrics = evaluate_all(path)
        metrics['TMMLU_Avg'] = np.mean([metrics[k]['accuracy'] for k in metrics if 'TMMLU' in k])

        print(metrics)
        print('====')
