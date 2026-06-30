import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Dataset path
csv_path = os.path.join(
    BASE_DIR,
    "data",
    "PS_20174392719_1491204439457_log.csv"
)

# Read dataset
df = pd.read_csv(csv_path)

print("Before Encoding:")
print(df["type"].head())

# Encode transaction type
encoder = LabelEncoder()
df["type"] = encoder.fit_transform(df["type"])

print("\nAfter Encoding:")
print(df["type"].head())
# Display columns before dropping
print("\nColumns Before Dropping:")
print(df.columns)

# Remove unnecessary columns
df = df.drop(["nameOrig", "nameDest"], axis=1)

# Display columns after dropping
print("\nColumns After Dropping:")
print(df.columns)

# Save processed dataset
processed_path = os.path.join(BASE_DIR, "data", "processed_data.csv")
df.to_csv(processed_path, index=False)

print("\nProcessed dataset saved successfully!")
print(processed_path)