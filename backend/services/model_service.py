import joblib
import numpy as np
import pandas as pd

class ModelService:
    def __init__(self):
        self.model = joblib.load('models/ensemble_model.pkl')
        self.scaler = joblib.load('models/scaler.pkl')
        self.threshold = joblib.load('models/threshold.pkl')

    def preprocess(self, data):
        input_df = pd.DataFrame([data])
        input_df = input_df[['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9',
                             'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18',
                             'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27',
                             'V28', 'Amount']]

        scaled_data = self.scaler.transform(input_df)
        return scaled_data

    def predict(self, data):
        processed_data = self.preprocess(data)
        prob_fraud = self.model.predict_proba(processed_data)[:, 1][0]
        prediction = int(prob_fraud >= self.threshold)
        return prediction, prob_fraud
