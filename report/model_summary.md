Model Summary: Electricity Bill Prediction

Model Used:
- Random Forest Regressor (main model)
- Linear Regression (for comparison)

Features Used:
- Fan
- Refrigerator
- AirConditioner
- Television
- Monitor
- MotorPump
- Month (1-12)
- City (encoded)
- Company (encoded)
- MonthlyHours
- Tariff Rate

Data Preprocessing:
- Categorical columns ('City', 'Company') encoded using LabelEncoder.
- Data split into training and test sets (80/20 split, random_state=42 for reproducibility).

Model Performance:
Random Forest Regressor (n_estimators=300):
    - RMSE: ~5.18
    - R² Score: ~0.99998
Linear Regression:
    - RMSE: ~70.50
    - R² Score: ~0.9956

Key Findings:
- Random Forest Regressor significantly outperforms Linear Regression, indicating the presence of non-linear relationships in the data.
- The most important features influencing the electricity bill are MonthlyHours and TariffRate, with appliance counts and categorical variables also contributing.
- The model achieves very high accuracy, with predictions typically within a few rupees of the actual bill.

Usage:
- The trained model and encoders are saved using joblib for deployment 
- New user data must be encoded in the same way as the training data before making predictions.

Reproducibility:
- All random processes controlled with random_state=42 for consistent results. 