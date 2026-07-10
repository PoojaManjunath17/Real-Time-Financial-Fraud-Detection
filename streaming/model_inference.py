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

# Predict a single transaction
def predict_transaction(transaction_df):
    prediction = model.predict(transaction_df)
    return prediction

# Day 22 - Commit 1
# Batch prediction helper
def predict_batch(transactions):
    predictions = model.predict(transactions)
    return predictions

# Fraud alert helper
def fraud_alert(prediction):
    if prediction[0] == 1:
        print("🚨 ALERT: Fraud Transaction Detected!")
    else:
        print("✅ Transaction is Safe")

# Test single prediction
result = predict_transaction(sample_df)

# Test batch prediction
batch_result = predict_batch(sample_df)

# Prediction probability
probability = model.predict_proba(sample_df)

print("\nPrediction Probability")
print(probability)

print("\nPrediction Result")
print(result)

print("\nPrediction from Function:")
print(result)

print("\nBatch Prediction:")
print(batch_result)

# Additional output for Day 22 Commit 1
print("\nBatch Prediction Summary")
print("Transactions Processed :", len(sample_df))
print("Batch Prediction Completed Successfully!")

print("\nFraud Alert Status")
fraud_alert(result)

print("\n" + "=" * 50)
print("MODEL SCORING STATUS")
print("=" * 50)

if result[0] == 1:
    print("Prediction Status : FRAUD")
    print("🚨 Fraudulent Transaction Detected")
else:
    print("Prediction Status : NORMAL")
    print("✅ Normal Transaction")