import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_curve
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.calibration import CalibratedClassifierCV
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import VotingClassifier
import joblib
import numpy as np

data = pd.read_csv('../datasets/creditcard.csv')

X = data.drop(columns=['Class'])
y = data['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

smote = SMOTE(sampling_strategy=0.1, random_state=42)
X_res, y_res = smote.fit_resample(X_train, y_train)

scaler = StandardScaler()
X_res = scaler.fit_transform(X_res)
X_test = scaler.transform(X_test)

joblib.dump(scaler, '../backend/models/scaler.pkl')

rf = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    class_weight='balanced',
    random_state=42
)

xgb = XGBClassifier(
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1,
    scale_pos_weight=len(y_train[y_train == 0]) / len(y_train[y_train == 1]),  # Adjust for imbalance
    eval_metric='logloss',
    use_label_encoder=False,
    random_state=42
)

ensemble_model = VotingClassifier(
    estimators=[('rf', rf), ('xgb', xgb)],
    voting='soft'
)

param_grid = {
    'xgb__max_depth': [6, 8, 10],
    'xgb__learning_rate': [0.01, 0.1, 0.2],
    'rf__n_estimators': [100, 200],
    'rf__max_depth': [8, 10, 12]
}

grid_search = GridSearchCV(ensemble_model, param_grid, scoring='f1', cv=5, n_jobs=-1, verbose=2)
grid_search.fit(X_res, y_res)

ensemble_model = grid_search.best_estimator_

calibrated_model = CalibratedClassifierCV(ensemble_model, method='sigmoid', cv=5)
calibrated_model.fit(X_res, y_res)

joblib.dump(calibrated_model, '../backend/models/ensemble_model.pkl')

y_pred_proba = calibrated_model.predict_proba(X_test)[:, 1]

fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
optimal_idx = np.argmax(tpr - fpr)
optimal_threshold = thresholds[optimal_idx]

joblib.dump(optimal_threshold, '../backend/models/threshold.pkl')

y_pred = (y_pred_proba >= optimal_threshold).astype(int)

print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Optimal Threshold:", optimal_threshold)
