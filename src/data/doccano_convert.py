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
        PARENT_DIR, 'data/proc', 'doccano_job_description.json'
    )
    SRC_FILE = os.path.join(PARENT_DIR, 'data/proc', 'dataset_binary.json')

    sk = SoftSkills()
    sk.gen(DST_FILE, SRC_FILE)
