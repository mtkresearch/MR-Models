import os
import argparse 
import json

from inference.generation_routine import generation_routine
from inference.aggregate_results import ResultAggregator

_CUR_DIR = os.path.dirname(os.path.realpath(__file__))

def run(config_path, model_name):
    configs = json.load(open(config_path, "r"))
    
    # Create dummy placeholder
    agg = ResultAggregator(model_name)

    # Go through scenarios
    new_configs = []
    for config in configs:
        print(config)
        ng = None
        try:
            ng = generation_routine(config)
            new_configs.append(ng)
        except Exception as e:
            print(f"Error: {e}")
        
        # Update result dict
        if ng is None:
            continue
        
        agg.merge_result(ng['result_path'])
        agg.save_agg_result_dict()


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