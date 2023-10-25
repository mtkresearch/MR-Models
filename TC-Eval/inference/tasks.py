import os
import sys
import re
from functools import partial
from typing import Tuple
from torch.utils.data import Dataset

_CUR_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f"{_CUR_DIR}/..")

from inference.prompt_template import ALL_MODEL_TEMPLATE_FUNC
from inference.scenarios import ALL_DATASETS


class Task:
    @staticmethod
    def get_task_query(question: str = "",
                       context: str = "",
                       query_template: str = "{question}{context}",
                       model_template_func: callable = lambda x: x,
                       prefix_query: str = "",
                       suffix_query: str = "",
                       **kwargs):
        r"""
        A full `task_query` consists of three parts as follows:
             [3]                 [2]                 [1]              [2]                  [3]
        <prefix_query> <model_template_wrap_front> <query> <model_template_wrap_back> <suffix_query>
        
        [1]: query constructed by user defined `query_template` and data from scenarios, i.e. `question` and `context`
        [2]: wrapping of query by model template callable, e.g. `[INST] {query} [/INST]` as in llama or `USER: {query}` as in vincuna format
        [3]: `prefix_query` and `suffix_query` defined by the user.

        """
        input_vars = dict(question=question, context=context)
        var_names = set(re.findall(r'\{(\w+)\}', query_template))
        for k, v in kwargs:
            if k in var_names:
                input_vars[k] = v
        query = query_template.format(input_vars)
        task_query = f"{prefix_query}{model_template_func(query)}{suffix_query}"
        return task_query


_DEFAULT_QUERY_TEMPLATE = {
    "DRCD": "請根據以下內容回答問題，且答案需盡可能簡短。注意：答案必須為內容的子字串。\n\n{context}\n\n問題：{question}\n\n",
    "FGC": "請根據以下內容回答問題，且答案需盡可能簡短。注意：答案必須為內容的子字串。\n\n{context}\n\n問題：{question}\n\n",
    "TTQA": "{question}",
    "TMMLU": "{question}",
    "XSum_TC": "請閱讀以下評論，並回答此評論是正面還是負面，如果是正面，請回答\'正面\';，如果是負面，請回答\'負面\'：\n\n評論：{context}\n\n",
    "IMDB_TC": "\n\n {context} \n\n 根據上述文章以一句話來總結\n\n",
    "BB_Penguins_in_a_Table_TC": "{question}",
}


def get_task_query_func(task_name, **prompt_config) -> callable:
    query_template = prompt_config.get('query_template', None)
    if query_template is None:
        query_template = _DEFAULT_QUERY_TEMPLATE[task_name]
        print(f"User defined query templated not provided; use default = {query_template}")
    
    model_template_func = partial(ALL_MODEL_TEMPLATE_FUNC[prompt_config.get("model_template", "default")], **prompt_config)

    return partial(Task.get_task_query, 
                   query_template=query_template, 
                   model_template_func=model_template_func
                   **prompt_config)


def get_task(task_name, prompt_config) -> Tuple[Dataset, callable]:
    dataset_cls = ALL_DATASETS[task_name]

    if 'TMMLU' in task_name:
        task_name = 'TMMLU'
    
    return (dataset_cls, get_task_query_func(task_name, **prompt_config))
    
        
    