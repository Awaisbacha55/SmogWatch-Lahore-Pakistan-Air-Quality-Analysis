"""
Harmonizes and merges raw hourly PM2.5 measurements with raw hourly Open-Meteo meteorology
across Lahore, Karachi, Islamabad, and Peshawar (2022–2024).
"""

from pathlib import Path
import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_AQ_DIR = BASE_DIR / "data" / "raw" / "air_quality" / "hourly"
RAW_WEATHER_DIR = BASE_DIR / "data" / "raw" / "weather"
OUTPUT_DIR = BASE_DIR / "data" / "processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

CITIES = ["Lahore", "Karachi", "Islamabad", "Peshawar"]


def assign_season(month: int) -> str:
    if month in [12, 1, 2]:
        return "Winter Smog"
    elif month in [3, 4, 5]:
        return "Pre-Monsoon Spring"
    elif month in [6, 7, 8]:
        return "Monsoon Summer"
    else:
        return "Post-Monsoon Autumn"


def assign_diurnal_phase(hour: int) -> str:
    if hour >= 22 or hour <= 6:
        return "Night Inversion (22:00-06:00)"
    elif 7 <= hour <= 10:
        return "Morning Rush (07:00-10:00)"
    elif 11 <= hour <= 16:
        return "Afternoon Mixing (11:00-16:00)"
    else:
        return "Evening Rush (17:00-21:00)"


def process_hourly_dataset():
    city_frames = []

    for city in CITIES:
        print(f"\nProcessing hourly dataset for {city}...")
        
        # 1. Load raw hourly weather
        weather_file = RAW_WEATHER_DIR / f"{city.lower()}_weather.csv"
        if not weather_file.exists():
            print(f"Weather file not found: {weather_file}")
            continue
            
        w_df = pd.read_csv(weather_file)
        # Parse time: e.g. 2022-01-01T00:00
        w_df["datetime"] = pd.to_datetime(w_df["time"]).dt.tz_localize(None)
        w_df["date"] = w_df["datetime"].dt.date
        w_df["year"] = w_df["datetime"].dt.year
        w_df["month"] = w_df["datetime"].dt.month
        w_df["day"] = w_df["datetime"].dt.day
        w_df["hour"] = w_df["datetime"].dt.hour
        w_df["city"] = city
        
        # Compute circular wind vectors
        rad = np.deg2rad(w_df["wind_direction_10m"])
        w_df["u_wind_10m"] = (-w_df["wind_speed_10m"] * np.sin(rad)).round(2)
        w_df["v_wind_10m"] = (-w_df["wind_speed_10m"] * np.cos(rad)).round(2)
        
        # 2. Load raw hourly air quality
        aq_file = RAW_AQ_DIR / f"{city.lower()}_pm25_hourly_2022_2024.csv"
        if not aq_file.exists():
            print(f"Air quality hourly file not found: {aq_file}")
            continue
            
        aq_df = pd.read_csv(aq_file)
        # Parse timestamp and strip tz info for clean join
        aq_df["datetime"] = pd.to_datetime(aq_df["datetime"]).dt.tz_localize(None).dt.floor("h")
        
        # Drop duplicates by datetime
        aq_df = aq_df.sort_values("datetime").drop_duplicates(subset=["datetime"])
        aq_sub = aq_df[["datetime", "pm25_ug_m3", "sensor_id", "has_flags"]]
        
        # 3. Merge weather and air quality on datetime
        merged = pd.merge(w_df, aq_sub, on="datetime", how="left")
        
        # Filter for study period 2022-01-01 to 2024-12-31
        merged = merged[(merged["datetime"] >= "2022-01-01") & (merged["datetime"] <= "2024-12-31 23:00:00")]
        
        # Add derived analytical features
        merged["season"] = merged["month"].apply(assign_season)
        merged["diurnal_phase"] = merged["hour"].apply(assign_diurnal_phase)
        merged["is_weekend"] = merged["datetime"].dt.dayofweek.isin([5, 6]).astype(int)
        
        city_frames.append(merged)
        
        valid_pm = merged["pm25_ug_m3"].notna().sum()
        total_hours = len(merged)
        print(f"  Total hourly records: {total_hours:,}")
        print(f"  Valid PM2.5 readings: {valid_pm:,} ({valid_pm/total_hours*100:.1f}%)")
        print(f"  Mean PM2.5: {merged['pm25_ug_m3'].mean():.2f} ug/m3 (Median: {merged['pm25_ug_m3'].median():.2f})")

    if not city_frames:
        raise RuntimeError("No city data was processed.")

    final_df = pd.concat(city_frames, ignore_index=True)
    
    # Sort deterministically
    final_df = final_df.sort_values(["city", "datetime"]).reset_index(drop=True)
    
    # Reorder columns
    cols = [
        "datetime", "date", "year", "month", "day", "hour", "city", "season", "diurnal_phase", "is_weekend",
        "pm25_ug_m3", "sensor_id", "has_flags",
        "temperature_2m", "relative_humidity_2m", "precipitation",
        "wind_speed_10m", "wind_direction_10m", "u_wind_10m", "v_wind_10m"
    ]
    # Keep only existing cols
    cols = [c for c in cols if c in final_df.columns]
    final_df = final_df[cols]
    
    out_csv = OUTPUT_DIR / "hourly_air_quality_weather_2022_2024.csv"
    final_df.to_csv(out_csv, index=False)
    print(f"\nSuccessfully generated: {out_csv}")
    print(f"Total rows: {len(final_df):,} | Columns: {len(final_df.columns)}")
    print("\nSummary by city:")
    print(final_df.groupby("city")["pm25_ug_m3"].agg(["count", "mean", "median", "min", "max"]).round(2))


if __name__ == "__main__":
    process_hourly_dataset()

