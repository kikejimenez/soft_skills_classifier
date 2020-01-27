'''
'''

import os, sys, json
import pathlib
from pathlib import Path

from pattern.en import tag
from pattern.vector import KNN, count
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support

PARENT_DIR = Path(
    Path(os.path.dirname(os.path.realpath(__file__))).parent
).parent

sys.path.append(os.path.join(PARENT_DIR, 'src/data'))
from doccano_convert import SoftSkills


class Pipeline:
    def __init__(self):
        pass

    @classmethod
    def train(cls, train_file, model_file):
        sents_dic = (json.loads(jsonl) for jsonl in SoftSkills.load(train_file))
        model = KNN()

        for sent in sents_dic:
            text = sent['text']
            v = count([word for word, pos in tag(text)])  # {'sweet': 1}
            if v:
                model.train(v, type=sent['soft skill'])
        model.save(model_file)
        return model

    @classmethod
    def predict(cls, model, sentences, print_pred=True):

        sentences = sentences if isinstance(sentences, list) else [sentences]

        predictions = [model.classify(sent) for sent in sentences]

        if print_pred:
            for sent, pred in zip(sentences, predictions):
                #print(f'Is sentence \'{s}\' a soft skill?: {p}')
                print(f'{sent} ---> {pred}')
        return predictions

    @classmethod
    def evaluate(cls, model, test_data, print_pred=True):
        sents_dic = (json.loads(jsonl) for jsonl in SoftSkills.load(test_data))
        y_true, y_pred = [], []
        for sent in sents_dic:
            y_true.append(sent['soft skill'])
            y_pred.append(model.classify(sent['text']))
        (precision, recall, fscore, _
        ) = precision_recall_fscore_support(y_true, y_pred, average='weighted')
        accuracy = accuracy_score(y_true, y_pred)
        evaluation = {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "fscore": fscore,
        }
        if print_pred:
            print(evaluation)
        return evaluation


if __name__ == "__main__":
    pl = Pipeline()
