from fastapi import FastAPI, Request
from pydantic import BaseModel
import joblib

# Read models saved during train phase
estimator_diabetes_loaded = joblib.load("diabetes_xgboost.pkl")

class Diabetes(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    Glucose: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int
    class Config:
        schema_extra = {
            "example": {
                "Pregnancies": 6,
                "Glucose": 145,
                "BloodPressure": 69,
                "SkinThickness": 35,
                "Insulin": 94,
                "BMI": 43.1,
                "DiabetesPedigreeFunction": 0.642,
                "Age": 45
            }
        }

app = FastAPI()

# prediction function
def make_diabetes_prediction(model, request):
    # parse input from request
    Pregnancies = request["Pregnancies"]
    Glucose = request["Glucose"]
    BloodPressure = request["BloodPressure"]
    SkinThickness = request["SkinThickness"]
    Insulin = request["Insulin"]
    BMI = request["BMI"]
    DiabetesPedigreeFunction = request['DiabetesPedigreeFunction']
    Age = request['Age']
    # Make an input vector
    diabetes = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
    # Predict
    prediction = model.predict(diabetes)
    return prediction[0]

# Diabetes Prediction endpoint
@app.post("/prediction/diabetes")
def predict_diabetes(request: Diabetes):
    prediction = make_diabetes_prediction(estimator_diabetes_loaded, request.dict())
    return prediction