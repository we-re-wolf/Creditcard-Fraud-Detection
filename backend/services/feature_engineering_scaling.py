# models/preprocess.py
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def add_features(df):
    df['Amount_log'] = np.log1p(df['Amount'])
    df['V1_V2_ratio'] = df['V1'] / (df['V2'] + 1e-5)
    df['V3_V4_diff'] = df['V3'] - df['V4']
    return df

def scale_features(df, scaler=None):
    scaled_columns = ['Time', 'Amount', 'Amount_log', 'V1_V2_ratio', 'V3_V4_diff'] + [f'V{i}' for i in range(1, 29)]
    if not scaler:
        scaler = StandardScaler()
        df[scaled_columns] = scaler.fit_transform(df[scaled_columns])
    else:
        df[scaled_columns] = scaler.transform(df[scaled_columns])
    return df, scaler
