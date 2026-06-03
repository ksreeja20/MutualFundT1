import pandas as pd
import os

# =========================
# STEP 1: LOAD ALL CSV FILES
# =========================

folder = "data/raw"

files = [f for f in os.listdir(folder) if f.endswith(".csv")]

dataframes = {}

print("\nLOADING DATASETS...\n")

for file in files:
    path = os.path.join(folder, file)

    df = pd.read_csv(path)

    dataframes[file] = df

print("\n--------------------------")
print("FILE:", file)

print("SHAPE:")
print(df.shape)

print("\nDTYPES:")
print(df.dtypes)

print("\nHEAD:")
print(df.head())



# =========================
# STEP 2: FIND FUND MASTER
# =========================

fund_df = None

for file in dataframes:
    if "fund" in file.lower():
        fund_df = dataframes[file]
        break


# =========================
# STEP 3: CLEAN COLUMN NAMES
# =========================

if fund_df is not None:
    fund_df.columns = (
        fund_df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )


# =========================
# STEP 4: FUND MASTER ANALYSIS
# =========================

if fund_df is not None:

    print("\n==============================")
    print("FUND MASTER ANALYSIS")
    print("==============================")

    print("\nCOLUMNS:")
    print(fund_df.columns)

    print("\nUNIQUE FUND HOUSES:")
    print(fund_df["fund_house"].unique())

    print("\nCATEGORIES:")
    print(fund_df["category"].unique())

    print("\nSUB CATEGORIES:")
    print(fund_df["sub_category"].unique())

    print("\nRISK CATEGORIES:")
    print(fund_df["risk_category"].unique())

    print("\nAMFI CODE SAMPLE:")
    print(fund_df["amfi_code"].head())

else:
    print("Fund master file not found")
    print("\n==============================")
print("AMFI CODE VALIDATION")
print("==============================")

nav_df = dataframes["02_nav_history.csv"]

fund_codes = set(fund_df["amfi_code"])
nav_codes = set(nav_df["amfi_code"])

missing_codes = fund_codes - nav_codes

print("Missing Codes:", missing_codes)