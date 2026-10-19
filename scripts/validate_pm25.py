
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
file_path = BASE_DIR / "data" / "raw" / "air_quality" / "peshawar_pm25_2022_2024.csv"

df = pd.read_csv(file_path, parse_dates=["date"])

# Check data quality
print("Total rows:", len(df))
print("Duplicate dates:", df["date"].duplicated().sum())
print("Missing PM2.5:", df["pm25_ug_m3"].isna().sum())

# Check expected dates
expected_dates = pd.date_range(
    "2022-01-01",
    "2024-12-31",
    freq="D",
    tz="Asia/Karachi"
)

actual_dates = pd.DatetimeIndex(df["date"].dropna()).normalize()
missing_dates = expected_dates.difference(actual_dates)

print("Expected calendar days:", len(expected_dates))
print("Dates with no record:", len(missing_dates))
print("\nFirst 15 missing dates:")
print(missing_dates[:15].tolist())

# Check invalid negative measurements
negative = df[df["pm25_ug_m3"] < 0]
print("\nNegative PM2.5 readings:", len(negative))

# Summary by year
df["year"] = df["date"].dt.year
print("\nYearly summary:")
print(df.groupby("year")["pm25_ug_m3"].agg(
    ["count", "mean", "median", "min", "max"]
).round(2))
