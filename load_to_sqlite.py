import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

print("Loading cleaned datasets into SQLite...\n")

# Load cleaned CSVs
nav_df = pd.read_csv("data/processed/02_nav_history_cleaned.csv")
txn_df = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")
perf_df = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")

# Save to database tables
nav_df.to_sql("fact_nav", engine, if_exists="replace", index=False)
txn_df.to_sql("fact_transactions", engine, if_exists="replace", index=False)
perf_df.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("Database loaded successfully!")

print("\nRow Counts:")
print("fact_nav:", len(nav_df))
print("fact_transactions:", len(txn_df))
print("fact_performance:", len(perf_df))