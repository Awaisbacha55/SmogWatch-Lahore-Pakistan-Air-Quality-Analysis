"""
Download hourly PM2.5 measurements from OpenAQ API v3 for Lahore, Karachi, Islamabad, and Peshawar (2022–2024).
"""

import os
import time
from pathlib import Path
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAQ_API_KEY")
if not API_KEY:
    raise SystemExit("Missing OPENAQ_API_KEY in .env file.")

CITIES = {
    "Lahore": 25135,
    "Karachi": 23747,
    "Islamabad": 25066,
    "Peshawar": 23455,
}

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "data" / "raw" / "air_quality" / "hourly"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

HEADERS = {"X-API-Key": API_KEY}
LIMIT = 1000


def download_city_hourly(city: str, sensor_id: int):
    print(f"\n{'=' * 50}")
    print(f"Fetching Hourly Data: {city} (Sensor ID: {sensor_id})")
    print(f"{'=' * 50}")

    url = f"https://api.openaq.org/v3/sensors/{sensor_id}/hours"
    all_records = []
    
    # Download year by year to keep requests focused and manageable
    for year in [2022, 2023, 2024]:
        dt_from = f"{year}-01-01T00:00:00Z"
        dt_to = f"{year}-12-31T23:59:59Z"
        page = 1
        print(f"  --> Year {year} ({dt_from} to {dt_to})...")
        
        while True:
            params = {
                "datetime_from": dt_from,
                "datetime_to": dt_to,
                "limit": LIMIT,
                "page": page,
            }
            
            try:
                resp = requests.get(url, headers=HEADERS, params=params, timeout=45)
            except Exception as e:
                print(f"    [Retry] Connection error on page {page}: {e}. Retrying in 3s...")
                time.sleep(3)
                resp = requests.get(url, headers=HEADERS, params=params, timeout=45)
                
            if resp.status_code == 429:
                print("    Rate limited (429). Sleeping 15 seconds...")
                time.sleep(15)
                continue
                
            if resp.status_code != 200:
                print(f"    Error {resp.status_code}: {resp.text[:200]}")
                break
                
            data = resp.json()
            results = data.get("results", [])
            if not results:
                break
                
            for item in results:
                period = item.get("period") or {}
                dt_from_info = period.get("datetimeFrom") or {}
                param = item.get("parameter") or {}
                flag_info = item.get("flagInfo") or {}
                
                # Use local datetime if available, otherwise UTC
                dt_str = dt_from_info.get("local") or dt_from_info.get("utc")
                val = item.get("value")
                
                all_records.append({
                    "datetime": dt_str,
                    "city": city,
                    "sensor_id": sensor_id,
                    "parameter": param.get("name", "pm25"),
                    "pm25_ug_m3": val,
                    "has_flags": flag_info.get("hasFlags", False),
                })
                
            print(f"    Page {page}: {len(results)} records")
            if len(results) < LIMIT:
                break
            page += 1
            time.sleep(0.5)  # Respect rate limits

    if not all_records:
        print(f"Warning: No hourly records found for {city}")
        return

    df = pd.DataFrame(all_records)
    df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce")
    df["pm25_ug_m3"] = pd.to_numeric(df["pm25_ug_m3"], errors="coerce")
    df = df.dropna(subset=["datetime"])
    df = df.sort_values("datetime").drop_duplicates(subset=["datetime", "sensor_id"])

    out_file = OUTPUT_DIR / f"{city.lower()}_pm25_hourly_2022_2024.csv"
    df.to_csv(out_file, index=False)
    print(f"Saved {len(df):,} hourly records to {out_file.name}")
    print(f"Valid PM2.5 readings: {df['pm25_ug_m3'].notna().sum():,}")
    print(f"Date range: {df['datetime'].min()} to {df['datetime'].max()}")


if __name__ == "__main__":
    for city, sid in CITIES.items():
        download_city_hourly(city, sid)
    print("\nHourly PM2.5 download complete!")

