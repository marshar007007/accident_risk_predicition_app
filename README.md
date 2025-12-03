# accident_risk_predicition_app
ML Project (Road Accident Risk Predicition)

# Accident Risk Prediction

## Overview
This project predicts accident risk using a K-Nearest Neighbors (KNN) Regressor. It aims to estimate risk levels based on features from an accident dataset.

## Dataset
- **Dataset:** Road Accident risk dataset from kaggle
- **Features:** 'road_type', 'num_lanes', 'curvature', 'speed_limit', 'lighting',
       'weather', 'road_signs_present', 'public_road', 'time_of_day',
       'holiday', 'school_season', 'num_reported_accidents', 'accident_risk'  
- **Preprocessing:** Categorical features encoded using one hot encoder, dimension reduced using PCA

## Model
- **Algorithm:** KNN Regressor  
- **Evaluation Metrics:**  
  - R² Score 
  - Mean Squared Error (MSE)  
  - Mean Absolute Error (MAE)  

### Performance
- R² Score: 0.828 (test data)
- R² Score: 0.887 (train data)
- MSE: 0.0054  
- MAE: 0.058  

## Web App
- Built with **Streamlit**  
- Allows users to input features and get accident risk predictions interactively  
