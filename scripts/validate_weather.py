from pathlib import Path
import pandas as pd

# Derive project root relative to script file
BASE_DIR = Path(__file__).resolve().parent.parent
folder = BASE_DIR / "data" / "raw" / "weather"
files = sorted(list(folder.glob("*.csv")))

if not files:
    print("ERROR: No weather CSV files found at:", folder)
else:
    for file in files:
        print("\n" + "=" * 50)
        print("FILE:", file.name)

        df = pd.read_csv(file)
        print("Rows:", len(df))
        print("Columns:", df.columns.tolist())
        print("\nFirst 5 rows:")
        print(df.head())

        if "time" in df.columns:
            df["time"] = pd.to_datetime(df["time"], errors="coerce")
            print("\nDate range:", df["time"].min(), "to", df["time"].max())
            print("Duplicate dates:", df["time"].duplicated().sum())

        print("\nMissing values:")
        print(df.isna().sum())

        numeric_cols = df.select_dtypes(include="number").columns
        if len(numeric_cols):
            print("\nNumeric summary:")
            print(df[numeric_cols].describe().round(2))
