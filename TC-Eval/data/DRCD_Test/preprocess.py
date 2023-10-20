import json


path = 'DRCD_test.json'

data = json.load(open(path))

preprocessed = {}
for i, inst in enumerate(data['data']):
    for j, paragraph in enumerate(inst['paragraphs']):
        paragraph_str = paragraph['context']
        for k, qa in enumerate(paragraph['qas']):
            preprocessed[str(len(preprocessed))] = {
                'paragraph': paragraph_str,
                'question': data['data'][i]['paragraphs'][j]['qas'][k]['question'],
                'references': [
                    x['text']
                    for x in data['data'][i]['paragraphs'][j]['qas'][k]['answers']
                ]
            }

with open('preprocessed_DRCD_test.json', 'w') as fw:
    json.dump(preprocessed, fw, ensure_ascii=False, indent=4)
