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
            choice = self._extract_choice(response_dict[idx])
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
    pass

EVALUATION_ITEMS = [
    ('TTQA', TTQATask('./data/TTQA/')),
]
