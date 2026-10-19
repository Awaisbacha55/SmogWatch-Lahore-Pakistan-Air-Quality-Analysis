
import os
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw" / "air_quality"
EXPECTED_DAYS = 1096

cities = ["lahore", "karachi", "islamabad", "peshawar"]

for city in cities:
    filename = f"{city}_pm25_2022_2024.csv"
    filepath = os.path.join(DATA_DIR, filename)

    print("\n" + "=" * 55)
    print(f"CITY: {city.upper()}")
    print("=" * 55)

    if not os.path.exists(filepath):
        print(f"FILE NOT FOUND: {filepath}")
        continue

    df = pd.read_csv(filepath)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["pm25_ug_m3"] = pd.to_numeric(
        df["pm25_ug_m3"], errors="coerce"
    )

    df = df.dropna(subset=["date"])

    # Compare calendar dates, ignoring the timezone and time
    actual_dates = set(df["date"].dt.date)
    expected_dates = set(
        pd.date_range("2022-01-01", "2024-12-31", freq="D").date
    )
    missing_dates = sorted(expected_dates - actual_dates)

    valid_values = df["pm25_ug_m3"].dropna()

    print(f"CSV records: {len(df)}")
    print(f"Expected calendar days: {EXPECTED_DAYS}")
    print(f"Unique dates: {df['date'].dt.date.nunique()}")
    print(f"Missing dates (no record): {len(missing_dates)}")
    print(f"Missing PM2.5 readings: {df['pm25_ug_m3'].isna().sum()}")
    print(f"Valid PM2.5 readings: {len(valid_values)}")
    print(f"Duplicate dates: {df['date'].dt.date.duplicated().sum()}")
    print(f"Negative PM2.5 readings: {(valid_values < 0).sum()}")
    print(f"First date: {df['date'].min()}")
    print(f"Last date: {df['date'].max()}")
    print(f"Units: {df['unit'].dropna().unique()}")

    if missing_dates:
        print("First 10 missing dates:")
        for missing_date in missing_dates[:10]:
            print(f"  {missing_date}")

    if not valid_values.empty:
        print("\nYearly PM2.5 summary (µg/m³):")
        df["year"] = df["date"].dt.year

        summary = df.groupby("year")["pm25_ug_m3"].agg(
            valid_days="count",
            mean="mean",
            median="median",
            minimum="min",
            maximum="max",
        )

        print(summary.round(2).to_string())

        print("\nTop 5 highest recorded values:")
        print(
            df.nlargest(5, "pm25_ug_m3")[
                ["date", "pm25_ug_m3"]
            ].to_string(index=False)
        )

print("\nValidation finished.")
