
import os
import sys
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
AIR_DIR = BASE_DIR / "data" / "raw" / "air_quality"
WEATHER_DIR = BASE_DIR / "data" / "raw" / "weather"
OUTPUT_DIR = BASE_DIR / "data" / "processed"

CITIES = ["lahore", "karachi", "islamabad", "peshawar"]

calendar = pd.DataFrame({
    "date": pd.date_range("2022-01-01", "2024-12-31", freq="D")
})
calendar["date"] = calendar["date"].dt.date

all_cities = []

for city in CITIES:
    print(f"\nProcessing {city.title()}...")

    # Load air-quality data
    air_path = AIR_DIR / f"{city}_pm25_2022_2024.csv"
    air = pd.read_csv(air_path)

    air["date"] = pd.to_datetime(
        air["date"], errors="coerce"
    ).dt.date

    air["pm25_ug_m3"] = pd.to_numeric(
        air["pm25_ug_m3"], errors="coerce"
    )

    # Retain only the date and PM2.5 value for this city
    air = air[["date", "pm25_ug_m3"]].dropna(subset=["date"])
    air = air.drop_duplicates(subset=["date"])

    # Load hourly weather data
    weather_path = WEATHER_DIR / f"{city}_weather.csv"
    weather = pd.read_csv(weather_path)

    weather["date"] = pd.to_datetime(
        weather["time"], errors="coerce"
    ).dt.date

    weather_columns = [
        "temperature_2m",
        "relative_humidity_2m",
        "precipitation",
        "wind_speed_10m",
        "wind_direction_10m",
    ]

    for column in weather_columns:
        weather[column] = pd.to_numeric(
            weather[column], errors="coerce"
        )

    # Aggregate hourly weather to daily values
    daily_weather = weather.groupby("date", as_index=False)[
        weather_columns
    ].mean()

    # Precipitation is a daily total, so sum hourly values instead
    daily_precipitation = weather.groupby("date", as_index=False)[
        "precipitation"
    ].sum(min_count=1)

    daily_weather = daily_weather.drop(
        columns=["precipitation"]
    ).merge(daily_precipitation, on="date", how="left")

    # Keep all calendar days, even when PM2.5 is missing
    combined = calendar.merge(air, on="date", how="left")
    combined = combined.merge(
        daily_weather, on="date", how="left"
    )

    combined.insert(0, "city", city.title())
    all_cities.append(combined)

    print("Calendar days:", len(combined))
    print("Valid PM2.5 readings:", combined["pm25_ug_m3"].notna().sum())
    print("Missing PM2.5 readings:", combined["pm25_ug_m3"].isna().sum())
    print("Missing weather rows:", combined[weather_columns].isna().all(axis=1).sum())

# Combine all cities into one analysis-ready dataset
final_df = pd.concat(all_cities, ignore_index=True)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
output_path = OUTPUT_DIR / "daily_air_quality_weather_2022_2024.csv"

# Absolute Data Protection Rule: Do not overwrite existing processed dataset silently
if output_path.exists() and "--force-overwrite" not in sys.argv:
    print("\n" + "!" * 65)
    print("DATA PROTECTION SAFEGUARD TRIGGERED:")
    print(f"Target file already exists: {output_path}")
    print("Under the project data protection rules, existing datasets must")
    print("not be overwritten silently. If regeneration is intended, provide")
    print("a separate output filename or use scripts/prepare_enhanced_analysis_data.py")
    print("!" * 65)
    sys.exit(0)

final_df.to_csv(output_path, index=False)

print("\n" + "=" * 50)
print("COMBINED DATASET SAVED")
print("=" * 50)
print("File:", output_path)
print("Total rows:", len(final_df))
print("Cities:", sorted(final_df["city"].unique()))
print("Date range:", final_df["date"].min(), "to", final_df["date"].max())
print("Missing PM2.5 values:", final_df["pm25_ug_m3"].isna().sum())
print("\nRows per city:")
print(final_df.groupby("city").size())
