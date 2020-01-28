'''
Convert Doccano annotations to a binary  'yes' or 'no' soft skills annotations
'''

import csv
import json


class SoftSkills:
    def __init__(self):
        pass

    @staticmethod
    def gen(src_jsonl, dst_jsonl):
        '''
        '''
        with open(src_jsonl) as src_f, open(dst_jsonl, 'w+') as dst_f:
            for line in src_f:
                dic = json.loads(line.strip())
                text = dic['text']

                if dic['annotations']:
                    soft_skill = 'yes' if any(
                        [ann['label'] == 48 for ann in dic['annotations']]
                    ) else 'no'
                    dst_f.write(
                        json.dumps({
                            'text': text,
                            'soft skill': soft_skill
                        })
                    )
                    dst_f.write('\n')

    @staticmethod
    def select_positives(src_jsonl, dst_jsonl):
        '''
        '''
        with open(src_jsonl) as src_f, open(dst_jsonl, 'w+') as dst_f:
            for line in src_f:
                dic = json.loads(line.strip())
                text = dic['text']

                if dic['annotations'] and any(
                    [ann['label'] == 12 for ann in dic['annotations']]
                ):
                    dst_f.write(json.dumps({'text': text, 'soft skill': 'yes'}))
                    dst_f.write('\n')

    @staticmethod
    def load(jsonl):
        '''
        '''
        generator = (sent for sent in open(jsonl))
        return generator

    @staticmethod
    def count_labeled(jsonl, label_name='annotations'):
        tot, nb_labeled = 0, 0
        for line in open(jsonl):
            sent = json.loads(line.strip())
            tot += 1
            nb_labeled += 1 if sent[label_name] else 0
        return {'total': tot, 'labeled': nb_labeled}

    @classmethod
    def count_freqs(cls, jsonl):
        '''
        '''
        sentences = cls.load(jsonl)
        tot, nb_yes = 0, 0,
        for jsonl in sentences:
            sent = json.loads(jsonl)
            tot += 1
            nb_yes += 1 if sent['soft skill'] == 'yes' else 0
        return {'yes': nb_yes, 'no': tot - nb_yes}


if __name__ == "__main__":
    import os
    import pathlib
    from pathlib import Path
    PARENT_DIR = Path(
        Path(os.path.dirname(os.path.realpath(__file__))).parent
    ).parent

    DST_FILE = os.path.join(
        PARENT_DIR, 'data/interim/back_end_developer',
        'positive_sentences_1_from_0_to_1001.jsonl'
    )
    SRC_FILE = os.path.join(
        PARENT_DIR, 'data/interim/back_end_developer',
        'annotated_back_end_sentences_1_from_0_to_1001.jsonl'
    )

    sk = SoftSkills()
    #sk.gen(DST_FILE, SRC_FILE)
    sk.select_positives(src_jsonl=SRC_FILE, dst_jsonl=DST_FILE)
