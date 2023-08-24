import json
import numpy as np

prompt_lens = []
answer_lens = []

with open("restricted/ttqa/TTQA_1.0.0.json", encoding="utf-8") as f:
    samples = json.load(f)

    for sample in samples:
        prompt, answers = sample['examples'], sample['answer']
        answers = answers.split(',')
        prompt_lens.append(len(prompt))
        answer_lens.append(np.max(np.array([len(answer) for answer in answers])))

print(len(prompt_lens))  
print(sum(prompt_lens)/len(prompt_lens))
print(np.max(np.array(prompt_lens)))
print(sum(answer_lens)/len(answer_lens))
print(np.max(np.array(answer_lens)))