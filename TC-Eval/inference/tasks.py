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
                       prefix_resp: str = "",
                       **kwargs):
        r"""
        A full `task_query` consists of three parts as follows:
                   [2]                 [1]              [2]                  [3]
         <model_template_wrap_front> <query> <model_template_wrap_back> <prefix_resp>
        
        [1]: query constructed by user defined `query_template` and data from scenarios, i.e. `question` and `context`
        [2]: wrapping of query by model template callable, e.g. `[INST] {query} [/INST]` as in llama or `USER: {query}` as in vincuna format
        [3]: `prefix_resp` defined by the user.

        """
        input_vars = dict(question=question, context=context)
        var_names = set(re.findall(r'\{(\w+)\}', query_template))
        for k, v in kwargs.items():
            if k in var_names:
                input_vars[k] = v
        assert 'question' in var_names or 'context' in var_names, "{question} or {context} vairable has to appear in query_template"
        query = query_template.format(**input_vars)
        task_query = f"{model_template_func(query)}{prefix_resp}"
        return task_query


_DEFAULT_QUERY_TEMPLATE = {
    "DRCD": "請根據以下內容回答問題，且答案需盡可能簡短。注意：答案必須為內容的子字串。\n\n{context}\n\n問題：{question}\n\n",
    "FGC": "請根據以下內容回答問題，且答案需盡可能簡短。注意：答案必須為內容的子字串。\n\n{context}\n\n問題：{question}\n\n",
    "TTQA": "{question}",
    "TMMLU": "{question}",
    "IMDB_TC": "請閱讀以下評論，並回答此評論是正面還是負面，如果是正面，請回答\'正面\';，如果是負面，請回答\'負面\'：\n\n評論：{context}\n\n",
    "XSum_TC_5k": "\n\n {context} \n\n 根據上述文章以一句話來總結\n\n",
    "PenguinsInTable_TC": "{question}"
}


def get_task_query_func(task_name, **prompt_config) -> callable:
    query_template = prompt_config.get('query_template', None)
    if query_template is None:
        query_template = _DEFAULT_QUERY_TEMPLATE[task_name]
        print(f"Task@{task_name}: User defined query templated not provided; use default = {query_template}")
    
    model_template_func = partial(ALL_MODEL_TEMPLATE_FUNC[prompt_config.get("model_template", "default")], **prompt_config)
    pconfig = {"prefix_resp": prompt_config.get("prefix_resp", ""),
               "sys_prompt": prompt_config.get("sys_prompt", "")
    }
    return partial(Task.get_task_query, 
                   query_template=query_template, 
                   model_template_func=model_template_func,
                   **pconfig)


def get_task(task_name, prompt_config) -> Tuple[Dataset, callable]:
    dataset_cls = ALL_DATASETS[task_name]

    if 'TMMLU' in task_name:
        task_name = 'TMMLU'
    
    return (dataset_cls, get_task_query_func(task_name, **prompt_config))
    
        
    