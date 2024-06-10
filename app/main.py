# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import pickle

app = FastAPI()

#  Load the model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

class PredictionRequest(BaseModel):
    data: list

class HealthCheckResponse(BaseModel):
    status: str

@app.get("/health", response_model=HealthCheckResponse)
def health_check():
    return HealthCheckResponse(status="OK")

@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        input_data = pd.DataFrame(request.data)
        prediction = model.predict(input_data)
        return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
