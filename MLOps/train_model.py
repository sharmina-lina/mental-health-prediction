# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_csv("digital_diet_mental_health.csv")

# Drop missing and encode gender
df.dropna(inplace=True)
df["gender"] = df["gender"].map({"Male": 0, "Female": 1})

X = df[["work_related_hours", "entertainment_hours", "gaming_hours", 
        "sleep_duration_hours", "sleep_quality", "mood_rating", 
        "physical_activity_hours_per_week", "mental_health_score"]]
y = df["stress_level"].astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))

joblib.dump(model, "model.pkl")
