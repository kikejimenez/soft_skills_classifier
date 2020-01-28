'''
split data in train and test sets
'''

import os, json
from pathlib import Path
from random import shuffle, random

PARENT_DIR = Path(
    Path(os.path.dirname(os.path.realpath(__file__))).parent
).parent
#source file
SRC = os.path.join(PARENT_DIR, 'data/proc', 'dataset_binary.json')

#destination files
TRAIN = os.path.join(PARENT_DIR, 'train_data.json')
TEST = os.path.join(PARENT_DIR, 'test_data.json')


def train_test_split(src_f, train_f, test_f):
    with open(src_f) as source, open(train_f,
                                     'w') as train, open(test_f, 'w') as test:

        for line in source:

            if random() <= 0.8:  #percentage of train files
                train.write(line)
            else:
                test.write(line)


def balanced_train_test(src, train, test, balance=.9, split=.8):

    #return print([json.loads(line) for line in open(src)])

    yes = sum('yes' == json.loads(line)['soft skill'] for line in open(src))
    no = int(yes * balance / (1 - balance))
    yes_no = [yes, no]
    c = [0, 0]  # c[0] == yes c[1] == no
    with open(src) as source, open(train,
                                   'w') as train, open(test, 'w') as test:
        for line in source:
            is_no = int(json.loads(line)['soft skill'] == 'no')
            c[is_no] += 1
            if c[is_no] > yes_no[is_no]:
                continue
            if random() <= split:  #percentage of train files
                train.write(line)
            else:
                test.write(line)


PARENT_DIR = Path(
    Path(os.path.dirname(os.path.realpath(__file__))).parent
).parent

SRC = os.path.join(
    PARENT_DIR, 'data/proc/front_end_developer/front_end_developer.jsonl'
)

#destination files
TRAIN = os.path.join(PARENT_DIR, 'data/proc/front_end_developer', 'train.jsonl')
TEST = os.path.join(PARENT_DIR, 'data/proc/front_end_developer', 'test.jsonl')

balanced_train_test(SRC, TRAIN, TEST)

print(sum(1 for line in open(TRAIN)), sum(1 for lines in open(TEST)))
