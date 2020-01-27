import os, json, sys
import en_core_web_sm
from unidecode import unidecode
import pathlib
from pathlib import Path
from pattern.vector import KNN

PARENT_DIR = Path(
    Path(os.path.dirname(os.path.realpath(__file__))).parent
).parent

sys.path.append(os.path.join(PARENT_DIR, 'src/model'))
from pipeline import Pipeline


def report(model_file, text_file):
    pl = Pipeline()
    model = KNN.load(model_file)
    nlp = en_core_web_sm.load()
    make_doc = lambda text: nlp(unidecode(text).strip())

    text = [line for line in open(text_file) if line.strip()]
    docs = [make_doc(line) for line in text]
    sentences = [sent.text for doc in docs for sent in doc.sents]

    print('\n'.join(text))

    predictions = pl.predict(model, sentences, print_pred=False)
    print('\n \n ###############  Soft Skills  ############\n')
    print(
        *[sent for sent, pred in zip(sentences, predictions) if 'yes' == pred],
        sep='\n'
    )


if __name__ == "__main__":
    from random import randint
    import sys
    if len(sys.argv) == 1:
        data_dir = os.path.join(PARENT_DIR, 'data/raw/back_end_developer')
        files = os.listdir(data_dir)
        text_file = os.path.join(data_dir, files[randint(0, len(files) - 1)])
    else:
        text_file = sys.argv[1]
    model_file = os.path.join(PARENT_DIR, 'model/pattern_model')
    report(model_file, text_file)
