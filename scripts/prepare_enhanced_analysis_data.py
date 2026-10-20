"""
SmogWatch: Enhanced Analysis Dataset Preparation
------------------------------------------------
Prepares an enhanced analysis dataset with circular wind direction averaging,
temporal indicators, and WHO guideline reference flags.

CRITICAL DATA INTEGRITY RULE:
This script preserves the original processed dataset
('daily_air_quality_weather_2022_2024.csv') unchanged and writes ONLY to a separate
enhanced file ('daily_air_quality_weather_enhanced.csv').
"""

from pathlib import Path
import numpy as np
import pandas as pd

# Define paths relative to this script location for robust execution
BASE_DIR = Path(__file__).resolve().parent.parent
AIR_DIR = BASE_DIR / "data" / "raw" / "air_quality"
WEATHER_DIR = BASE_DIR / "data" / "raw" / "weather"
OUTPUT_DIR = BASE_DIR / "data" / "processed"
ENHANCED_OUTPUT = OUTPUT_DIR / "daily_air_quality_weather_enhanced.csv"

CITIES = ["lahore", "karachi", "islamabad", "peshawar"]


def calculate_circular_mean_degrees(angles_deg: pd.Series) -> float:
    """
    Computes the circular mean of angular directions (in degrees [0, 360)).
    Treats angles as unit vectors in polar space, averages their sine and
    cosine components, and returns the resulting angle in degrees.
    """
    valid_angles = angles_deg.dropna()
    if valid_angles.empty:
        return np.nan
    rad = np.deg2rad(valid_angles)
    sin_mean = np.mean(np.sin(rad))
    cos_mean = np.mean(np.cos(rad))
    mean_rad = np.arctan2(sin_mean, cos_mean)
    mean_deg = np.rad2deg(mean_rad) % 360.0
    return round(float(mean_deg), 2)


def deg_to_compass(deg: float) -> str:
    """Converts wind direction in degrees to an 8-point compass sector."""
    if pd.isna(deg):
        return "Unknown"
    val = int((deg / 45.0) + 0.5) % 8
    sectors = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    return sectors[val]


def assign_season(month: int) -> str:
    """Assigns meteorological season for Pakistan."""
    if month in (12, 1, 2):
        return "Winter"
    elif month in (3, 4, 5):
        return "Spring/Pre-Monsoon"
    elif month in (6, 7, 8):
        return "Summer/Monsoon"
    else:
        return "Autumn/Post-Monsoon"


def assign_who_target(pm25: float) -> str:
    """
    Classifies PM2.5 daily average against WHO 2021 Air Quality Guideline
    and Interim Targets (IT).
    """
    if pd.isna(pm25):
        return "Missing"
    elif pm25 <= 15.0:
        return "Within WHO Guideline (<= 15)"
    elif pm25 <= 25.0:
        return "WHO Interim Target 4 (15.1-25)"
    elif pm25 <= 37.5:
        return "WHO Interim Target 3 (25.1-37.5)"
    elif pm25 <= 50.0:
        return "WHO Interim Target 2 (37.6-50)"
    elif pm25 <= 75.0:
        return "WHO Interim Target 1 (50.1-75)"
    else:
        return "Exceeds All WHO Targets (> 75)"


def prepare_enhanced_dataset():
    print("=" * 60)
    print("PREPARING ENHANCED ANALYSIS DATASET (SEPARATE OUTPUT)")
    print("=" * 60)

    calendar = pd.DataFrame({
        "date": pd.date_range("2022-01-01", "2024-12-31", freq="D")
    })
    calendar["date"] = calendar["date"].dt.date

    all_cities_dfs = []

    for city in CITIES:
        print(f"Processing city: {city.title()}...")
        # 1. Load Raw PM2.5 CSV
        air_file = AIR_DIR / f"{city}_pm25_2022_2024.csv"
        if not air_file.exists():
            raise FileNotFoundError(f"Air quality file not found: {air_file}")
        air = pd.read_csv(air_file)
        air["date"] = pd.to_datetime(air["date"], errors="coerce").dt.date
        air["pm25_ug_m3"] = pd.to_numeric(air["pm25_ug_m3"], errors="coerce")
        air = air[["date", "pm25_ug_m3"]].dropna(subset=["date"])
        air = air.drop_duplicates(subset=["date"])

        # 2. Load Raw Weather CSV
        weather_file = WEATHER_DIR / f"{city}_weather.csv"
        if not weather_file.exists():
            raise FileNotFoundError(f"Weather file not found: {weather_file}")
        weather = pd.read_csv(weather_file)
        weather["date"] = pd.to_datetime(weather["time"], errors="coerce").dt.date

        # Numeric conversions
        for col in ["temperature_2m", "relative_humidity_2m", "precipitation",
                    "wind_speed_10m", "wind_direction_10m"]:
            weather[col] = pd.to_numeric(weather[col], errors="coerce")

        # 3. Aggregate Weather Variables
        # - Daily Means for Continuous Measurements
        daily_means = weather.groupby("date", as_index=False)[
            ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"]
        ].mean().round(2)

        # - Daily Sum for Precipitation
        daily_precip = weather.groupby("date", as_index=False)[
            "precipitation"
        ].sum(min_count=1).round(2)

        # - Arithmetic Mean Wind Direction (to preserve compatibility with original schema)
        daily_wind_dir_arith = weather.groupby("date", as_index=False)[
            "wind_direction_10m"
        ].mean().round(2)

        # - Scientifically Accurate Circular Mean for Wind Direction
        circular_dirs = weather.groupby("date")["wind_direction_10m"].apply(
            calculate_circular_mean_degrees
        ).reset_index(name="wind_direction_circular_deg")

        daily_weather = daily_means.merge(daily_wind_dir_arith, on="date", how="left")
        daily_weather = daily_weather.merge(circular_dirs, on="date", how="left")
        daily_weather = daily_weather.merge(daily_precip, on="date", how="left")

        # 4. Merge Calendar + Air Quality + Weather
        combined = calendar.merge(air, on="date", how="left")
        combined = combined.merge(daily_weather, on="date", how="left")
        combined.insert(0, "city", city.title())

        all_cities_dfs.append(combined)

    final_df = pd.concat(all_cities_dfs, ignore_index=True)

    # 5. Add Enriched Temporal & Guideline Columns
    dt_series = pd.to_datetime(final_df["date"])
    final_df["year"] = dt_series.dt.year
    final_df["month"] = dt_series.dt.month
    final_df["month_name"] = dt_series.dt.strftime("%b")
    final_df["day"] = dt_series.dt.day
    final_df["day_of_week"] = dt_series.dt.day_name()
    final_df["season"] = final_df["month"].apply(assign_season)
    # Peak smog season in Punjab/Indus plain is October through February
    final_df["is_smog_season"] = final_df["month"].isin([10, 11, 12, 1, 2])

    # Preserve raw PM2.5 and flag 985 ug/m3 sensor-ceiling errors
    final_df["pm25_ug_m3_raw"] = final_df["pm25_ug_m3"]
    date_str = final_df["date"].astype(str)
    
    is_karachi_error = (final_df["city"] == "Karachi") & (date_str == "2022-04-21")
    is_peshawar_error = (final_df["city"] == "Peshawar") & (date_str.isin(["2023-09-30", "2023-10-01", "2023-10-02"]))
    final_df["is_sensor_ceiling_error"] = is_karachi_error | is_peshawar_error

    # Set sensor errors to NaN in the cleaned analysis column
    final_df.loc[final_df["is_sensor_ceiling_error"], "pm25_ug_m3"] = np.nan

    # Wind Compass Sector
    final_df["wind_compass"] = final_df["wind_direction_circular_deg"].apply(deg_to_compass)

    # WHO Guideline reference indicators
    final_df["who_24h_exceeded"] = final_df["pm25_ug_m3"].apply(
        lambda x: True if pd.notna(x) and x > 15.0 else (False if pd.notna(x) else np.nan)
    )
    final_df["who_target_level"] = final_df["pm25_ug_m3"].apply(assign_who_target)

    # 6. Save ONLY to Enhanced File
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    final_df.to_csv(ENHANCED_OUTPUT, index=False)

    print("\n" + "=" * 60)
    print("ENHANCED DATASET GENERATED SUCCESSFULLY")
    print("=" * 60)
    print(f"Destination: {ENHANCED_OUTPUT}")
    print(f"Total Rows: {len(final_df)} (Expected 4384)")
    print(f"Total Columns: {len(final_df.columns)}")
    print(f"Columns: {final_df.columns.tolist()}")
    print("\nPM2.5 Missing Count per City:")
    print(final_df.groupby("city")["pm25_ug_m3"].apply(lambda s: s.isna().sum()))
    print("\nCircular Wind Direction Sample vs Arithmetic:")
    sample = final_df[["city", "date", "wind_direction_10m", "wind_direction_circular_deg", "wind_compass"]].dropna().head(5)
    print(sample.to_string(index=False))


if __name__ == "__main__":
    prepare_enhanced_dataset()
