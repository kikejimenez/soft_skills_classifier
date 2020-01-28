#!/bin/bash
python -c  '
from src.model.pipeline import Pipeline
pl = Pipeline()
train_data = "data/proc/front_end_developer/train.jsonl"
test_data = "data/proc/front_end_developer/test.jsonl"
model_file = "model/pattern_model"
model = pl.train(train_file = train_data, model_file = model_file)
pl.evaluate(model,test_data)
'