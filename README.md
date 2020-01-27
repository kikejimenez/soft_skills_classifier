# Soft Skills

A machine learning utility to retrieve soft skills from Job description.
## Quick Start Guide

```bash
# Install requirements
pip install -r requirements.txt

# Retrieve language model from spacy
python -m spacy download en

# Predict soft skills
python src/reports/soft_skills.py <name of the txt file>

# train and evaluate your own model
./train.sh
```
## Results from our model 
We have trained and evaluated our model with a thousand of sentences (with train/test split 70/30) generated from backend developer job descriptions. The evaluation of the resulting model gives:
```
{'accuracy': 0.9641255605381166,  
 'precision': 0.9601418291792678,  
  'recall': 0.9641255605381166,  
  'fscore': 0.9607065411903407}
```
## Example
 The command `python reports/predict.py example1.txt` outputs:
```
IQVIA™ is the leading human data science company focused on helping healthcare clients find unparalleled insights and better solutions for patients. Formed through the merger of IMS Health and Quintiles, IQVIA offers a broad range of solutions that harness the power of healthcare data, domain expertise, transformative technology, and advanced analytics to drive healthcare forward. 

Deliverables 
Coordinate study build and technical activities across a regional or global team. 
Coordinate study post production changes across regional or global team. 
Ensure overall study technical deliverables meet time and quality goals. 
Serve as technical liaison with customer and DM team. 
Performs activities related to the database design, programming of data validation checks, debugging, modification, technical integrations, and maintenance of clinical database management systems in various third-party vendor platforms. 
May lead or assist in configuration settings and associated programming. 
May lead or assist in configuring and associated programming activities in various integration modules. 
May lead or assist in planning and coordinating database design, development, implementation, maintenance, and user support of clinical systems. 
May lead or assist in the preparation of documentation and procedures for system installation and maintenance. 
May lead or assist in creating custom functions associated with various CDMS tools. 
May lead or assist in performing peer review of programming codes. 
May lead or assist in providing impact assessment of programming mid study change. 
May lead or assist in setting up and configuring internal tools for medical coding. 
May lead or assist in setting up and configuring internal tools for document indexing. 
May lead or assist in creating client specific reports. 
Meet objectives as assigned and interact with the project team to organize timelines, responsibilities and deliverables. 
Maintains compliance with core operating procedures and working instructions. 
Develops and maintains good communications and working relationships with teams and external clients. 
Interacts with corporate team members to negotiate timelines, responsibilities and deliverables. 
May lead or assist IT in developing and implementing new technologies. 
May lead or assist IT in testing and evaluating new upgrades to technologies. 
May lead or assist in developing, revising, and maintaining core operating procedures and working instructions. 
May Serve as a lead programmer on the corporate team. 

Trainings 
Trained/certified on various third-party vendor applications such as Medidata RAVE and associated applications. 
Attend trainings on internal and/or client specific standard operating procedures and work instructions. 
Participate in corporate training programs and contribute to lessons learnt sharing initiatives. 

Technical and Domain skills 
Experience with Rave Classic and EDC data capture tools. 
Experience preferred with various Rave modules and tools, such as CODER, RWS, ePRO, etc. 
Experience with Medidata custom functions and advanced study build tools and techniques. 
Experience with Medidata Rave data integrations. 
Knowledge of back-end EDC data structures preferred. 
Knowledge on clinical data management. 
Knowledge on programming and reporting process. 
Knowledge on ICH GCP. 
Demonstrate ability to learn new systems and function in an evolving technical environment. 
Attention to details and ability to work in virtual team setup. 
Good awareness on business decisions and work with awareness on Changes. 
Maintain regulatory knowledge 
Language Skills 
Competent in written and oral English. 
Excellent communication skills. 
Project management skills 
Ability to negotiate timelines and meet timelines. 
Coordinate lead programmers, study team with timelines and budget. 
Interact with internal stakeholders and customers with regards to technical issues. 
Provide technical support and advice to internal teams and customers. 

Knowledge
Requires knowledge of principles, theories, and concepts of a job area, typically obtained through advanced education. 

Education 
Master’s or bachelor’s degree in Computer Science or related discipline, or equivalent experience. 

Join Us 
Making a positive impact on human health takes insight, curiosity, and intellectual courage. It takes brave minds, pushing the boundaries to transform healthcare. Regardless of your role, you will have the opportunity to play an important part in helping our clients drive healthcare forward and ultimately improve outcomes for patients. 
Forge a career with greater purpose, make an impact, and never stop learning. 
IQVIA is an EEO Employer - Minorities/Females/Protected Veterans/Disabled 
IQVIA, Inc. provides reasonable accommodations for applicants with disabilities. Applicants who require reasonable accommodation to submit an application for employment or otherwise participate in the application process should contact IQVIA’s Talent Acquisition team at  workday_recruiting@iqvia.com  to arrange for such an accommodation. 

Job ID:  R1105482

 
###############  Soft Skills  ############

Demonstrate ability to learn new systems and function in an evolving technical environment.
Language Skills
Competent in written and oral English.
Excellent communication skills.
```
## Train your own model
To train your model first change  `train.sh`  file to an executable mode (with ``chmod`` command) and specify the training  set, the test set and the model files in `train.sh`:
```
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
```

## Data format

The data for training and testing must be in the json line format:

```
{"text": "React Javascript with knowledge of Redux state container", "soft skill": "no"}
{"text": "Eager to work in a fast-paced and dynamic environment", "soft skill": "yes"}
...
```

### Python Environment

Python version in this repo is 3.6 and utilizes packages that are not part of the common library. To make sure you have all of the  appropriate packages, please use `pip` to install the `requirements.txt` file. 

## Author
Enrique Jimenez

Email: `ejimenez@intekglobal.com` 