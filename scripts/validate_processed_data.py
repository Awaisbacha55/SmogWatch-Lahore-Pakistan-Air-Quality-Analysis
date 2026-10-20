
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
path = BASE_DIR / "data" / "processed" / "daily_air_quality_weather_2022_2024.csv"
df = pd.read_csv(path)

print("Dataset shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nRows per city:")
print(df.groupby("city").size())

print("\nDate range per city:")
print(df.groupby("city")["date"].agg(["min", "max"]))

print("\nDuplicate city-date rows:", df.duplicated(["city", "date"]).sum())

weather_cols = [
    "temperature_2m",
    "relative_humidity_2m",
    "precipitation",
    "wind_speed_10m",
    "wind_direction_10m",
]

print("\nMissing values by column:")
print(df.isna().sum())

print("\nPM2.5 summary by city:")
print(
    df.groupby("city")["pm25_ug_m3"].agg(
        valid_days="count",
        mean="mean",
        median="median",
        minimum="min",
        maximum="max",
    ).round(2)
)

print("\nAll weather values missing on a row:",
      df[weather_cols].isna().all(axis=1).sum())

print("\nValidation complete.")

