def task_config_check(config):
    
    def _check_tgi_generation_config(cfg):
        _check_keys = set({'do_sample', 'temperature', 'max_new_tokens', 'best_of'})
        for k in cfg.keys():
            if k not in _check_keys:
                raise KeyError(f"{k} not in {_check_keys} of the tgi_generation_config")
        
    def _check_openai_generation_config(cfg):
        _check_keys = set({'temperature'})
        for k in cfg.keys():
            if k not in _check_keys:
                raise KeyError(f"{k} not in {_check_keys} of the openai_generation_config")
    
    def _check_prompt_config(cfg):
        _check_keys = set({'query_template', 'prefix_resp', 'model_template', 'sys_prompt'})
        for k in cfg.keys():
            if k not in _check_keys:
                raise KeyError(f"{k} not in {_check_keys} of the prompt_config")
        
    
    _check_tgi_generation_config(config.get("tgi_generation_config", {}))
    _check_openai_generation_config(config.get("openai_generation_config", {}))
    _check_prompt_config(config["prompt_config"])


def deep_merge(dict1, dict2):
    result = dict1.copy()
    for k in dict2:
        if k in result and isinstance(result[k], dict) and isinstance(dict2[k], dict):
            result[k] = deep_merge(result[k], dict2[k])
        else:
            result[k] = dict2[k]
    return result        
