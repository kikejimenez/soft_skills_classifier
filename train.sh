#!/bin/bash
python -c  '
from src.model.pipeline import Pipeline
pl = Pipeline()
train_data = "train_data.json"
test_data = "test_data.json"
model_file = "model/pattern_model"
model = pl.train(train_file = train_data, model_file = model_file)
pl.evaluate(model,test_data)
'