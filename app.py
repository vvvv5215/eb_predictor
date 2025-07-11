import streamlit as st
import pandas as pd
import joblib
import os
import urllib.request


MODEL_URL = "https://drive.google.com/uc?export=download&id=1fKI3pX3xoS73AfiFv05nSBeKxeqkAMy_"
MODEL_PATH = "data/rf_model.joblib"
ENCODER_URL = "https://drive.google.com/uc?export=download&id=1eWrsWE7rRbF34U5POvoREBLG7QDWWwZb"
ENCODER_PATH = "data/encoders.joblib"


if not os.path.exists(MODEL_PATH):
    os.makedirs("data", exist_ok=True)
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
if not os.path.exists(ENCODER_PATH):
    os.makedirs("data", exist_ok=True)
    urllib.request.urlretrieve(ENCODER_URL, ENCODER_PATH)

model = joblib.load(MODEL_PATH)
encoders = joblib.load(ENCODER_PATH)


st.title("Electricity Bill Predictor using Random Forest Regressor")

fan = st.number_input("Number of Fans", min_value=0, value=1, step=1)
refrigerator = st.number_input("Number of Refrigerators", min_value=0, value=1, step=1)
air_conditioner = st.number_input("Number of Air Conditioners", min_value=0, value=1, step=1)
television = st.number_input("Number of Televisions", min_value=0, value=1, step=1)
monitor = st.number_input("Number of Monitors", min_value=0, value=1, step=1)
motor_pump = st.number_input("Number of Motor Pumps", min_value=0, value=0, step=1)
month = st.number_input("Month (1-12)", min_value=1, value=1,max_value=12, step=1)
city = st.selectbox("City", encoders['City'].classes_)
company = st.selectbox("Company", encoders['Company'].classes_)
monthly_hours = st.number_input("Monthly Usage Hours", min_value=0, value=100, step=1)
tariff_rate = st.number_input("Tariff Rate", min_value=0, value=8, step=1)

if st.button("Predict"):
    user_data = pd.DataFrame({
        'Fan': [fan],
        'Refrigerator': [refrigerator],
        'AirConditioner': [air_conditioner],
        'Television': [television],
        'Monitor': [monitor],
        'MotorPump': [motor_pump],
        'Month': [month],
        'City': [city],
        'Company': [company],
        'MonthlyHours': [monthly_hours],
        'TariffRate': [tariff_rate]
    })
    # Encode categorical columns
    for col in ['City', 'Company']:
        user_data[col] = encoders[col].transform(user_data[col])
    pred = model.predict(user_data)
    st.success(f"Predicted Electricity Bill: {pred[0]:.2f} INR")
