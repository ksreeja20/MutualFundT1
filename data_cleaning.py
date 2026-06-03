import pandas as pd
import os

# Create processed folder
os.makedirs("data/processed", exist_ok=True)

print("STARTING DATA CLEANING...\n")

# =====================================
# 1. CLEAN NAV HISTORY
# =====================================

nav_df = pd.read_csv("data/raw/02_nav_history.csv")

nav_df["date"] = pd.to_datetime(nav_df["date"])

nav_df = nav_df.sort_values(["amfi_code", "date"])

nav_df["nav"] = nav_df.groupby("amfi_code")["nav"].ffill()

nav_df = nav_df.drop_duplicates()

nav_df = nav_df[nav_df["nav"] > 0]

nav_df.to_csv("data/processed/02_nav_history_cleaned.csv", index=False)

print("NAV HISTORY CLEANED")


# =====================================
# 2. CLEAN INVESTOR TRANSACTIONS
# =====================================

txn_df = pd.read_csv("data/raw/08_investor_transactions.csv")

txn_df["transaction_date"] = pd.to_datetime(txn_df["transaction_date"])

txn_df["transaction_type"] = txn_df["transaction_type"].str.strip().str.title()

txn_df = txn_df[txn_df["amount_inr"] > 0]

print("\nKYC STATUS VALUES:")
print(txn_df["kyc_status"].unique())

txn_df.to_csv("data/processed/08_investor_transactions_cleaned.csv", index=False)

print("INVESTOR TRANSACTIONS CLEANED")


# =====================================
# 3. CLEAN SCHEME PERFORMANCE
# =====================================

perf_df = pd.read_csv("data/raw/07_scheme_performance.csv")

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    perf_df[col] = pd.to_numeric(perf_df[col], errors="coerce")

anomalies = perf_df[
    (perf_df["expense_ratio_pct"] < 0.1) |
    (perf_df["expense_ratio_pct"] > 2.5)
]

print("\nEXPENSE RATIO ANOMALIES:")
print(len(anomalies))

perf_df.to_csv("data/processed/07_scheme_performance_cleaned.csv", index=False)

print("SCHEME PERFORMANCE CLEANED")

print("\nDATA CLEANING COMPLETED")
