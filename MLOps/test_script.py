# test_request.py
import requests

data = {
    "work_related_hours": 6,
    "entertainment_hours": 2,
    "gaming_hours": 1,
    "sleep_duration_hours": 7,
    "sleep_quality": 3,
    "mood_rating": 4,
    "physical_activity_hours_per_week": 3,
    "mental_health_score": 70
}

response = requests.post("http://localhost:8000/predict", json=data)
print("Status:", response.status_code)
print("Response:", response.json())
