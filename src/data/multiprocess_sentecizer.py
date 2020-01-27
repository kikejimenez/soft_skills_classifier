'''
Generate sentences file from multiple files in a directory
'''

import os, json
import en_core_web_sm
from unidecode import unidecode
import multiprocessing
from multiprocessing import Pool
import pathlib
from pathlib import Path

PARENT_DIR = Path(
    Path(os.path.dirname(os.path.realpath(__file__))).parent
).parent
#source dir
SRC_DIR = os.path.join(PARENT_DIR, 'data/raw', 'back_end_developer')
DST_FILE = os.path.join(
    PARENT_DIR, 'data/interim/back_end_developer', 'sentences.josn'
)

if os.path.isfile(DST_FILE):
    os.remove(DST_FILE)

with open(DST_FILE, 'w+') as f:
    pass


def gen_sentences(files):

    nlp = en_core_web_sm.load()
    make_doc = lambda text: nlp(unidecode(text).strip())

    for file in files:
        with open(file) as txt_f, open(DST_FILE, 'a') as dst_f:
            docs = (make_doc(line) for line in txt_f if line.strip())
            json_arr = (
                json.dumps({
                    "text": sent.text,
                    # "binary": []
                }) for doc in docs for sent in doc.sents
            )
            for jsonl in json_arr:
                dst_f.write(jsonl + '\n')


def sentences_in_chunks(files, nb_chunks):
    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    with Pool(nb_chunks) as p:
        p.map(gen_sentences, chunks(files, nb_chunks))


if __name__ == "__main__":

    files = [os.path.join(SRC_DIR, f) for f in os.listdir(SRC_DIR)]
    nb_chunks = 10

    sentences_in_chunks(files, nb_chunks)
