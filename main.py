# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 09:44:02 2023

@author: ACER
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"]
    allow_headers=["*"],
)

class model_input(BaseModel):
    
    Carbohydrate_intake : float

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

@app.post('/diabetes_prediction')

def diabetes_pred(input_parameters: model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    carb = input_dictionary['Carbohydrate_intake']
    
    prediction = diabetes_model.predict([[carb]])
    
    if prediction[0] == 0:
        return 'The person is not diabetic'
    
    else:
        return 'The persion is diabetic'