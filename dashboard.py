import streamlit as st
import joblib

# Load trained AI model
model = joblib.load("landslide_model.pkl")

st.title("🌍 AI-Based Landslide Risk Monitoring System")
st.write("Enter the sensor values to predict landslide risk.")

# Input values
rainfall = st.number_input(
    "🌧️ Rainfall",
    min_value=0.0,
    value=50.0
)

soil_moisture = st.number_input(
    "🌱 Soil Moisture",
    min_value=0.0,
    value=50.0
)

tilt_angle = st.number_input(
    "📐 Tilt Angle",
    min_value=0.0,
    value=5.0
)

# Prediction button
if st.button("🔍 Predict Risk"):

    prediction = model.predict(
        [[rainfall, soil_moisture, tilt_angle]]
    )

    risk = prediction[0]

    if risk == 0:
        st.success("🟢 LOW RISK")
    elif risk == 1:
        st.warning("🟡 MEDIUM RISK")
    else:
        st.error("🔴 HIGH RISK")


