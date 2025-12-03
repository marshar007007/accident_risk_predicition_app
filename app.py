import streamlit as st
import pandas as pd
import joblib
import os

model = joblib.load("accident_risk_model.joblib")
st.set_page_config(page_title="Accident Risk Prediction", layout="wide")


st.sidebar.title("Information")

logo_path = "images/paramiuniversity_logo.jfif"
if os.path.exists(logo_path):
    st.sidebar.image(logo_path, width=140)

st.sidebar.markdown("**Student ID:** PIUS20230053")
st.sidebar.markdown("**Student Name:** Thandar Htwe")
st.sidebar.markdown("**Course:** Intro to ML")
st.sidebar.markdown("**University:** Parami University")
st.sidebar.markdown("**Instructor:** Prof Nwe Nwe Htay Win")

st.title("Road Accident Risk Prediction System")
st.markdown("Provide the road and environmental conditions to estimate the accident risk score.")

st.divider()
st.subheader("Road Settings")
col1, col2, col3 = st.columns(3)
with col1: road_type = st.selectbox("Road Type", ["rural", "highway", "urban"])
with col2: public_road = st.selectbox("Is it a Public Road?", ["Yes", "No"])
with col3: road_signs_present = st.selectbox("Road Signs Present", ["Yes", "No"])

st.divider()
st.subheader("Road Features")
col1, col2, col3 = st.columns(3)
with col1:num_lanes = st.number_input("Number of Lanes", min_value=1, max_value=4, value=2)
with col2:curvature = st.number_input("Road Curvature", min_value=0.29, max_value=0.93, step=0.01, value=0.3)
with col3:speed_limit = st.number_input("Speed Limit (km/h)", min_value=25, max_value=70, value=60)

st.divider()
st.subheader("Environmental Conditions")
col1, col2, col3 = st.columns(3)
with col1: lighting = st.selectbox("Lighting Condition", ["night", "dim", "daylight"])
with col2: weather = st.selectbox("Weather Condition", ["rainy", "clear", "foggy"])
with col3: time_of_day = st.selectbox("Time of Day", ["morning", "afternoon", "evening", "night"])

st.divider()
st.subheader("Seasonal Status")
col1, col2 = st.columns(2)
with col1: holiday = st.selectbox("Holiday", ["Yes", "No"])
with col2: school_season = st.selectbox("School Season", ["Yes", "No"])

st.divider()
st.subheader("Historical Data")
num_reported_accidents = st.number_input("Number of Reported Accidents",min_value=0, max_value=10, value=1)

st.divider()

input_data = pd.DataFrame({
    "road_type": [road_type],
    "num_lanes": [num_lanes],
    "curvature": [curvature],
    "speed_limit": [speed_limit],
    "lighting": [lighting],
    "weather": [weather],
    "road_signs_present": [True if road_signs_present == "Yes" else False],
    "public_road": [True if public_road == "Yes" else False],
    "time_of_day": [time_of_day],
    "holiday": [True if holiday == "Yes" else False],
    "school_season": [True if school_season == "Yes" else False],
    "num_reported_accidents": [num_reported_accidents]
})

st.subheader("Input Summary")
st.dataframe(input_data, use_container_width=True)

st.divider()
 
def categorize_risk(value):
    if value <= 0.3:
        return "Low Accident Risk"
    elif value <= 0.6:
        return "Moderate Accident Risk"
    else:
        return "High Accident Risk"

risk_images = {
    'Low Accident Risk': 'images/low_risk.jpg',
    'Moderate Accident Risk': 'images/moderate_risk.jpg',
    'High Accident Risk': 'images/high_risk.jpg'
}

if st.button("Predict Accident Risk", use_container_width=True):
    try:
        prediction = model.predict(input_data)[0]
        risk_label = categorize_risk(prediction)

        st.subheader("Prediction Result")
        st.write(f"**Predicted Risk Score:** {prediction:.3f}")
        st.success(f"Risk Level: {risk_label}")
        st.image(risk_images[risk_label], caption=f"{risk_label}",width=400)

    except Exception as e:
        st.error(f"Prediction Error: {e}")
        st.info("Make sure the model and input features match exactly.")
