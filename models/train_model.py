import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
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

# Train Logistic Regression Model
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

print("\nLogistic Regression Model Trained Successfully!")

# Predict on test data
y_pred = model.predict(X_test)

print("\nFirst 20 Predictions:")
print(y_pred[:20])
# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy")
print(f"{accuracy:.4f}")

print("\nFirst 20 Actual Values:")
print(y_test.values[:20])