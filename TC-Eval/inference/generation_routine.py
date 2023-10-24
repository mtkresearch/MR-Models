import os
import sys
import re
import json
import argparse
from collections import defaultdict
from tqdm import tqdm
from rich import print

from inference.scenarios import BigBenchPenguinsInATableTC, FGC, DRCD, TTQA, XSumTC, TMMLU, IMDBTC
from inference.get_response import TGIResponseModel, OpenAIResponseModel


_CUR_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f"{_CUR_DIR}/..")

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


def generation_routine(config):
    # dictionary for saving results
    state_dict = defaultdict(list)

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
        outputs = response_model.get_response(input_text, **config)
        output_text = outputs['completions'][0]

        # Log results into state_dict
        log_state = dict(id=sample['id'], query=input_text, references=sample['references'], response=output_text)
        state_dict[scenario_name].append(log_state)
    
    # Save results
    output_dir = f"{config['output_dir']}/{scenario_name}"
    os.makedirs(output_dir, exist_ok=True)

    result_path = f"{output_dir}/result.json"
    json.dump(state_dict, open(result_path, "w"), ensure_ascii=False, indent=2)

    # Dump logging
    config['result_path'] = result_path
    json.dump(config, open(f"{output_dir}/config.json", "w"), ensure_ascii=False, indent=2)

    return config


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=None, type=str)
    args = parser.parse_args()

    config_path = args.config
    configs = json.load(open(config_path, "r"))

    new_configs = []
    for config in configs:
        print(config)
        # generation_routine(config)
        try:
            ng = generation_routine(config)
            new_configs.append(ng)
        except Exception as e:
            print(f"Error: {e}")




