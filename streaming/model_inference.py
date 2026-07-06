import os
import joblib
import pandas as pd

# Project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load trained model
model_path = os.path.join(BASE_DIR, "models", "fraud_detection_model.pkl")
model = joblib.load(model_path)

print("=" * 50)
print("MODEL LOADED SUCCESSFULLY")
print("=" * 50)

# Sample transaction
sample_transaction = {
    "step": 1,
    "type": 3,
    "amount": 5000.0,
    "oldbalanceOrg": 10000.0,
    "newbalanceOrig": 5000.0,
    "oldbalanceDest": 0.0,
    "newbalanceDest": 5000.0,
    "isFlaggedFraud": 0
}

sample_df = pd.DataFrame([sample_transaction])

prediction = model.predict(sample_df)
probability = model.predict_proba(sample_df)

print("\nPrediction Probability")
print(probability)

print("\nPrediction Result")
print(prediction)

if prediction[0] == 1:
    print("Fraudulent Transaction Detected")
else:
    print("Normal Transaction")