import json
import numpy as np

prompt_lens = []
answer_lens = []

def create_prompt(sample: dict):
    """
    Given an example in dataset format, create the prompt and the list of
    correct references.
    """
    symbol = "____"
    prompt = "請閱讀以下短文，並在空格內填入正確的成語：\n\n"
    content = sample['examples'].replace("____", symbol)
    prompt += f"內容：{content}"
    prompt += f"空格中應填入成語\n"
    prompt += "1."
    

    answers = sample["ans"].split(',')
    

    return prompt, answers

with open("restricted/tcic/valid.json", encoding="utf-8") as f:
    all_samples = json.load(f)

    clean_samples = all_samples

    for sample in clean_samples:
        prompt, answers = create_prompt(sample)
        prompt_lens.append(len(prompt))
        answer_lens.append(np.max(np.array([len(answer) for answer in answers])))

print(len(prompt_lens))  
print(sum(prompt_lens)/len(prompt_lens))
print(np.max(np.array(prompt_lens)))
print(sum(answer_lens)/len(answer_lens))
print(np.max(np.array(answer_lens)))
