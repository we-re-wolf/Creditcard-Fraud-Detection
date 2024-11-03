import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def data_preprocess(file_path):
    data = pd.read_csv(file_path)
    #print(data.head())

    if data.isnull().values.any():
        data.fillna(method='ffill', inplace=True)
        
    scaler = StandardScaler()
    data['Amount'] = scaler.fit_transform(data['Amount'].values.reshape(-1, 1))
    data['Time'] = scaler.fit_transform(data['Time'].values.reshape(-1, 1))
    X = data.drop(['Class'], axis=1)  # Features
    y = data['Class']  # Target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test


