import pandas as pd

df = pd.read_csv("data/PS_20174392719_1491204439457_log.csv")

print(df["isFraud"].value_counts())

print("\nFirst fraud transactions:")
print(df[df["isFraud"] == 1].head())

print("\nIndexes of first fraud transactions:")
print(df[df["isFraud"] == 1].index[:10])