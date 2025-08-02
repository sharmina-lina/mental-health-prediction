# 🧠 Mental Health Score Prediction from Digital Diet

This project uses machine learning to predict a user's mental health score based on their digital behavior, location type, screen time, and other factors.

---

## 📊 Dataset

The dataset `digital_diet_mental_health.csv` contains:
- Demographic features: gender, location type
- Digital behavior: screen time, device usage
- Target: `mental_health_score`

---

## 🧩 Problem Statement

We aim to predict the `mental_health_score` using behavioral and contextual data. This helps understand how digital lifestyle affects mental health.

---

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib & Seaborn
- Jupyter Notebook

---

## 🔁 Project Workflow

1. **Data Preprocessing**
   - Encoded categorical variables (`gender`, `location_type`)
   - Removed irrelevant columns like `user_id`
   - Standardized numerical features

2. **Exploratory Data Analysis**
   - Correlation matrix
   - Feature distribution

3. **Modeling**
   - Linear Regression
   - Random Forest Regressor
   - XGBoost Regressor (optional)

4. **Evaluation**
   - Mean Absolute Error (MAE)
   - Root Mean Squared Error (RMSE)
   - R² Score

---

## 📈 Model Results

| Model               | MAE   | RMSE  | R² Score |
|--------------------|-------|-------|----------|
| Linear Regression  | 3.25  | 4.12  | 0.76     |
| Random Forest       | 2.85  | 3.70  | 0.82     |

*(Replace with your actual results)*

---

## 📌 How to Run

1. Clone the repo:
```bash
git clone https://github.com/yourusername/mental-health-prediction.git
