# Electricity Bill Predictor

Predict your monthly electricity bill based on various factors!

---

## Features

- Predicts electricity bill based on:
  - Number of appliances 
  - Month
  - City and Company
  - Monthly usage hours
  - Tariff rate
- Interactive web app built with Streamlit
- Compares Random Forest and Linear Regression models


---

## 🛠️ How to Use

### 1. Clone the repository
```bash
git clone https://github.com/vvvv5215/eb_predictor.git
cd eb_predictor
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3.  Train the model
- Run the Jupyter notebook in `notebook/final_soln.ipynb` 

### 4. Run the Streamlit app from root folder
```bash
streamlit run app.py
```
- Enter your appliance usage and other details in the web interface to get your predicted bill.

---

## Project Structure

├── app.py # Streamlit web app
├── requirements.txt # Python dependencies
├── data/ # Dataset and (optionally) model files
│ └── electricity_bill_dataset.csv
├── notebook/
│ └── final_soln.ipynb # Model training and analysis
├── report/
│ └── model_summary.txt # Model summary and findings
└── README.md # Project documentation

## Notes

- The trained model is not included in the repository due to GitHub’s file size limits.
- To use your own trained model, save it in the `data/` directory.
