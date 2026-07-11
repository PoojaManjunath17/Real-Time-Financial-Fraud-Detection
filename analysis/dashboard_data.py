print("=" * 50)
print("DASHBOARD DATA GENERATION")
print("=" * 50)

dashboard_data = {
    "Total Transactions": 6362620,
    "Fraud Transactions": 8213,
    "Safe Transactions": 6354407,
    "Accuracy": "99.73%",
    "Pipeline Status": "Active"
}

print("\nDashboard Metrics")

for key, value in dashboard_data.items():
    print(f"{key} : {value}")

print("\nDashboard data generated successfully.")