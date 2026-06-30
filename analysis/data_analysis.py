import os
import pandas as pd

# -----------------------------
# Locate the project directory
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Dataset path
csv_path = os.path.join(
    BASE_DIR,
    "data",
    "PS_20174392719_1491204439457_log.csv"
)

# -----------------------------
# Load the dataset
# -----------------------------
df = pd.read_csv(csv_path)

print("=" * 60)
print("PaySim Dataset Loaded Successfully")
print("=" * 60)

# -----------------------------
# Display first 5 rows
# -----------------------------
print("\nFirst 5 Rows:")
print(df.head())

# -----------------------------
# Dataset Shape
# -----------------------------
print("\nDataset Shape:")
print(df.shape)

# -----------------------------
# Dataset Information
# -----------------------------
print("\nDataset Information:")
df.info()

# -----------------------------
# Missing Values
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# Fraud Distribution
# -----------------------------
print("\nFraud Distribution:")
print(df["isFraud"].value_counts())

# -----------------------------
# Percentage of Fraud
# -----------------------------
fraud_percent = (df["isFraud"].sum() / len(df)) * 100

print(f"\nFraud Percentage: {fraud_percent:.4f}%")

# -----------------------------
# Statistical Summary
# -----------------------------
print("\nStatistical Summary:")
print(df.describe())

# -----------------------------
# Transaction Type Distribution
# -----------------------------
print("\nTransaction Type Distribution:")
print(df["type"].value_counts())

print("\nAnalysis Completed Successfully!")