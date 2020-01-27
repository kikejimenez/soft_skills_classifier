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

with open(SRC) as src, open(TRAIN, 'w') as train, open(TEST, 'w') as test:

    for line in src:

        if random() <= 0.8:  #percentage of train files
            train.write(line)
        else:
            test.write(line)
