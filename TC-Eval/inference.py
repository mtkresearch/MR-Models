import os
import json
import argparse
from typing import Dict, Any
from tqdm import tqdm
from rich import print

from inference.get_response import TGIResponseModel, OpenAIResponseModel
from inference.aggregate_results import ResultAggregator
from inference.tasks import get_task


_CUR_DIR = os.path.dirname(os.path.realpath(__file__))


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

    # Setup task
    task_name = config['task_name']
    prompt_config = config['prompt_config']
    dataset_cls, get_task_query_func = get_task(task_name, prompt_config)
    dataset = dataset_cls()
    
    run_num_samples = config['run_num_samples']
    run_num_samples = min(run_num_samples, len(dataset)) if run_num_samples != -1 else len(dataset)
    for i, sample in tqdm(enumerate(dataset), desc=task_name, total=run_num_samples):
        if i > run_num_samples:
            break

        input_text = get_task_query_func(**sample)
        try:
            outputs = response_model.get_response(input_text, **config)
            output_text = outputs['completions'][0]

            # Log results
            log_state = dict(id=sample['id'], query=input_text, references=sample['references'], response=output_text)
            agg.merge_result({task_name: [log_state]})
            agg.save_agg_result_dict()
        except Exception as e:
            error_text = f"Error in generation loop: {e}"
            print(error_text)


def run(config_path):
    configs = json.load(open(config_path, "r"))
    
    # Create dummy placeholder
    model_name = configs[0]['model_name']
    agg = ResultAggregator(model_name)
    assert len(set([c['model_name'] for c in configs])) == 1, f"Do not support inferencing multiple LM models atm."

    # Go through scenarios
    for config in configs:
        generation_routine(config, agg)


if __name__ == '__main__':
    default_cfg_path = f"{_CUR_DIR}/configs/base.json"
    parser = argparse.ArgumentParser()
    parser.add_argument(f"--config", default=default_cfg_path, type=str)
    args = parser.parse_args()

    config_path = args.config
    run(config_path)