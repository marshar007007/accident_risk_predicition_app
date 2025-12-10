# accident_risk_predicition_app
ML Project (Road Accident Risk Predicition)

# Accident Risk Prediction

## Overview
This project predicts accident risk using a K-Nearest Neighbors (KNN) Regressor. It aims to estimate risk levels based on features from an accident dataset.

## Dataset
- **Dataset:** Road Accident risk dataset from kaggle
- **Columns:** 'road_type', 'num_lanes', 'curvature', 'speed_limit', 'lighting',
       'weather', 'road_signs_present', 'public_road', 'time_of_day',
       'holiday', 'school_season', 'num_reported_accidents', 'accident_risk'
- **Preprocessing:** Categorical features encoded using one hot encoder, standard scaler used for numerical features, using PCA vs not using PCA to reduce dimesion(but without using PCA condition has better result, it can be seen under development code file). 

## Model
- **Algorithm:** KNN Regressor and best_k_number (5) is chosen after looping k_values by comparing along with evaluation metircs.
- **Evaluation Metrics:**  
  - R² Score 
  - Mean Squared Error (MSE)  
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)

### Performance
- R2 Score: 0.8349013595439014
- MSE: 0.0051929663999999995
- MAE: 0.0570072
- RMSE 0.07206223976535839
  
## Web App
- Built with **Streamlit**  
- Allows users to input features and get accident risk predictions interactively  
