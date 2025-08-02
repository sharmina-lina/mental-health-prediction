from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("model.pkl")

class InputData(BaseModel):
    work_related_hours: float
    entertainment_hours: float
    gaming_hours: float
    sleep_duration_hours: float
    sleep_quality: float
    mood_rating: float
    physical_activity_hours_per_week: float
    mental_health_score: float

@app.get("/")
def read_root():
    return {"message": "Stress Level Prediction API is live. Use POST /predict with JSON body."}

@app.post("/predict")
def predict(data: InputData):
    features = np.array([[data.work_related_hours, data.entertainment_hours, data.gaming_hours,
                          data.sleep_duration_hours, data.sleep_quality, data.mood_rating,
                          data.physical_activity_hours_per_week, data.mental_health_score]])
    prediction = model.predict(features)[0]
    return {"predicted_stress_level": int(prediction)}

