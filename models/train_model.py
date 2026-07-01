import os
import pandas as pd
from sklearn.model_selection import train_test_split

# Project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load processed dataset
data_path = os.path.join(BASE_DIR, "data", "processed_data.csv")
df = pd.read_csv(data_path)

print("Dataset Loaded Successfully!")
print(df.head())

# Features and Target
X = df.drop("isFraud", axis=1)
y = df["isFraud"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape :", X_test.shape)