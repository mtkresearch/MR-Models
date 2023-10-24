import os
import sys
import re
import json
import argparse
from typing import Dict, Any
from collections import defaultdict
from tqdm import tqdm
from rich import print

from inference.scenarios import BigBenchPenguinsInATableTC, FGC, DRCD, TTQA, XSumTC, TMMLU, IMDBTC
from inference.get_response import TGIResponseModel, OpenAIResponseModel
from inference.aggregate_results import ResultAggregator


_CUR_DIR = os.path.dirname(os.path.realpath(__file__))

_which_scenario = {
    'BB_Penguins_in_a_Table_TC': BigBenchPenguinsInATableTC,
    'FGC': FGC,
    'DRCD': DRCD,
    'TTQA': TTQA,
    'XSum_TC': XSumTC,
    'IMDB_TC': IMDBTC,
    'TMMLU': TMMLU
}


def _get_response_model(config):
    resp_model_name = config['resp_model_name']
    response_model = None
    if resp_model_name == 'tgi':
        api_base = config['api_base']
        response_model = TGIResponseModel(api_base)
    elif resp_model_name == "openai":
        response_model = OpenAIResponseModel(**config)
    else:
        raise NotImplementedError

    return response_model


def generation_routine(config: Dict[str, Any], agg: ResultAggregator = None):
    # Set up response model
    response_model = _get_response_model(config)

    # Set up scenario
    scenario_cls = _which_scenario[config['scenario']]
    scenario = scenario_cls(**config)
    scenario_name = scenario.name

    # Get results
    prompt_template = config['prompt_template']
    var_names = set(re.findall(r'\{(\w+)\}', prompt_template))

    eval_num_samples = min(config['eval_num_samples'], len(scenario))
    for i, sample in tqdm(enumerate(scenario), desc=scenario_name, total=eval_num_samples):
        if i > eval_num_samples:
            break

        # Construct varialbes to be placed into prompt_template
        input_vars = dict(system_prompt=config["system_prompt"], suffix_inst=config["suffix_inst"])
        for k, v in sample.items():
            if k in var_names:
                input_vars[k] = v
    
        input_text = prompt_template.format(**input_vars)
        try:
            outputs = response_model.get_response(input_text, **config)
            output_text = outputs['completions'][0]

            # Log results
            log_state = dict(id=sample['id'], query=input_text, references=sample['references'], response=output_text)
            agg.merge_result({scenario_name: [log_state]})
            agg.save_agg_result_dict()
        except Exception as e:
            error_text = f"Error in generation loop: {e}"
            print(error_text)


def run(config_path, model_name):
    configs = json.load(open(config_path, "r"))
    
    # Create dummy placeholder
    agg = ResultAggregator(model_name)

    # Go through scenarios
    for config in configs:
        generation_routine(config, agg)


if __name__ == '__main__':
    default_cfg_path = f"{_CUR_DIR}/configs/base.json"
    default_model_name = "my_model"
    parser = argparse.ArgumentParser()
    parser.add_argument(f"--config", default=default_cfg_path, type=str)
    parser.add_argument(f"--model_name", default=default_model_name, type=str)
    args = parser.parse_args()

    config_path = args.config
    model_name = args.model_name
    run(config_path, model_name)