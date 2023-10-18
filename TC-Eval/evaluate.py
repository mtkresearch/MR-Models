from typing import List, Dict

import numpy as np


class Task:
    def evaluate(self, list_of_data: List[Dict], list_of_response: List[str]) -> Dict:
        pass
        # return metrics


class MultipleChoiceTask(Task):
    def _extract_choice(self, response):
        pass

    def evaluate(self, list_of_data: List[Dict], list_of_response: List[str]) -> Dict:
        # keys of data: gold
        correct_list = []
        for data, response in zip(list_of_data, list_of_response):
            choice = self._extract_choice(response)
            correct_list.append(1 if choice == data['gold'] else 0)
        return {
            'accuracy': np.mean(correct_list)
        }


class QuestionAnsweringTask(Task):
    def evaluate(self, list_of_data: List[Dict], list_of_response: List[str]) -> Dict:
        pass


class SummaryTask(Task):
    def evaluate(self, list_of_data: List[Dict], list_of_response: List[str]) -> Dict:
        pass


