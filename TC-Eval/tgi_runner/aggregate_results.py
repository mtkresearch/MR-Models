import os
import argparse
import json
import glob
from tqdm import tqdm
_CUR_DIR = os.path.dirname(os.path.realpath(__file__))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--result_dir", default=None, type=str)
    parser.add_argument("--model_name", default=None, type=str)
    args = parser.parse_args()

    result_dir = args.result_dir
    model_name = args.model_name

    result_jpath = glob.glob(f"{result_dir}/**/result.json")

    outputs = {'name': model_name, 'link': "", "describe": "", "results": []}
    for jpath in tqdm(result_jpath):
        jdata = json.load(open(jpath, "r"))
        print(jdata.keys())
        ds_name = list(jdata.keys())[0]
        
        # Remove query and references
        new_jdata = [dict(id=s['id'], response=s['response']) for s in jdata[ds_name]]
        outputs['results'].append({ds_name: new_jdata})
    
    # Save to result folder
    dest = f"{_CUR_DIR}/../results/{model_name}_result.json"
    json.dump(outputs, open(dest, "w"), indent=2, ensure_ascii=False)
    print(f".... save aggregated results to {dest}")





