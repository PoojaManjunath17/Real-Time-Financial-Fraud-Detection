import os
import joblib
import pandas as pd

# Project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load model
model_path = os.path.join(BASE_DIR, "models", "fraud_detection_model.pkl")
model = joblib.load(model_path)

print("Model loaded successfully!")

# Load dataset
data_path = os.path.join(BASE_DIR, "data", "processed_data.csv")
df = pd.read_csv(data_path)

# Take first 5 records
sample = df.drop("isFraud", axis=1).head(5)

# Predict
prediction = model.predict(sample)

print("\nPredictions:")
print(prediction)