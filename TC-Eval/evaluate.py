import re
import json
from typing import List, Dict

import numpy as np


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
    def evaluate(self, list_of_response: List[Dict]) -> Dict:
        pass


class SummaryTask(Task):
    def evaluate(self, list_of_response: List[Dict]) -> Dict:
        pass


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


EVALUATION_ITEMS = [
    ('ttqa_mc', TTQATask('./data/TTQA/')),
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