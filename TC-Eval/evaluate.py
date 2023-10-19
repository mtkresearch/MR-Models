import re
import os
import json
from typing import List, Dict

import numpy as np
import pandas as pd


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
            choice = self._extract_choice(response_dict[f'id{idx}'])  # TODO: walk-around  
            correct_list.append(1 if choice == gold_dict[idx] else 0)
        return {
            'accuracy': np.mean(correct_list)
        }


class QuestionAnsweringTask(Task):
    def evaluate(self, list_of_response: List[Dict]) -> Dict:
        pass


class SummaryTask(Task):
    def evaluate(self, list_of_response: List[Dict]) -> Dict:
        pass


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


EVALUATION_ITEMS = [
    ['ttqa_mc', TTQATask('./data/TTQA/')],
    *[[f'TMMLU_{subject}', TMMLUTask(f'./data/TMMLU/subjects/{subject}/')]
      for subject in os.listdir('./data/TMMLU/subjects/')],
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
