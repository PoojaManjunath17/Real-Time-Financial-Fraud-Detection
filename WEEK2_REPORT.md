# Week 2 Progress Report

## Project
**Real-Time Financial Fraud Detection Pipeline**

---

# Week 2 Objective

Perform batch data analysis and model training using the PaySim dataset. Prepare the dataset, engineer features, train a machine learning model, evaluate its performance, and serialize the trained model for future real-time deployment.

---

## Day 8 – Data Analysis

- Created a data analysis module using Python and Pandas.
- Loaded the processed PaySim dataset.
- Displayed dataset shape and first few records.
- Checked dataset information and data types.
- Identified missing values in the dataset.
- Verified dataset quality before model training.

---

## Day 9 – Feature Engineering

- Performed feature preprocessing.
- Encoded categorical transaction types using LabelEncoder.
- Converted transaction categories into numerical values.
- Prepared the dataset for machine learning algorithms.
- Saved the processed dataset for further use.

---

## Day 10 – Dataset Preparation

- Split the processed dataset into training and testing datasets.
- Used an 80:20 train-test split.
- Prepared feature matrix (X) and target variable (`isFraud`).
- Verified training and testing dataset sizes.

---

## Day 11 – Model Training

- Implemented a Logistic Regression classifier.
- Trained the model using the training dataset.
- Generated predictions on the testing dataset.
- Compared predicted values with actual fraud labels.

---

## Day 12 – Model Evaluation

- Calculated Accuracy.
- Calculated Precision.
- Calculated Recall.
- Calculated F1 Score.
- Displayed the evaluation summary.
- Assessed the overall fraud detection performance.

---

## Day 13 – Performance Analysis

- Generated the Confusion Matrix.
- Generated the Classification Report.
- Analyzed:
  - True Positives
  - True Negatives
  - False Positives
  - False Negatives
- Focused on reducing missed fraudulent transactions.

---

## Day 14 – Model Serialization

- Saved the trained Logistic Regression model using Joblib.
- Created `fraud_detection_model.pkl`.
- Loaded the saved model successfully.
- Verified predictions using the serialized model.
- Prepared the model for real-time deployment.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Logistic Regression
- Apache Kafka
- Docker

---

# Week 2 Outcome

Successfully completed the batch analytics and machine learning phase of the project. The dataset was analyzed, preprocessed, and transformed into a machine-learning-ready format. The Logistic Regression model was trained, evaluated using multiple performance metrics, serialized using Joblib, and validated for future integration into the real-time Kafka streaming pipeline.