import json


path = 'FGC_official_final.json'

data = json.load(open(path))

preprocessed = {}
for inst in data:
    paragraph_str = inst['DTEXT']
    for qa in inst['QUESTIONS']:
        question_str = qa['QTEXT']
        references = [qa['ANSWER']]
        preprocessed[str(len(preprocessed))] = {
            'paragraph': paragraph_str,
            'question': question_str,
            'references': references
        }

with open('preprocessed_FGC_official_final.json', 'w') as fw:
    json.dump(preprocessed, fw, ensure_ascii=False, indent=4)
