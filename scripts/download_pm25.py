
import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAQ_API_KEY")

# Historical PM2.5 sensor IDs verified in the previous step
CITIES = {
    "Lahore": 25135,
    "Karachi": 23747,
    "Islamabad": 25066,
    "Peshawar": 23455,
}

DATE_FROM = "2022-01-01"
DATE_TO = "2024-12-31"
OUTPUT_DIR = "data/raw/air_quality"
LIMIT = 1000

if not API_KEY:
    raise SystemExit(
        "API key nahi mili. Project root ki .env file check karein."
    )

os.makedirs(OUTPUT_DIR, exist_ok=True)

headers = {"X-API-Key": API_KEY}


def download_city(city, sensor_id):
    print(f"\n{'=' * 45}")
    print(f"Downloading: {city} | Sensor ID: {sensor_id}")
    print("=" * 45)

    url = f"https://api.openaq.org/v3/sensors/{sensor_id}/days"
    all_records = []
    page = 1

    while True:
        params = {
            "date_from": DATE_FROM,
            "date_to": DATE_TO,
            "limit": LIMIT,
            "page": page,
        }

        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=60,
        )

        if response.status_code != 200:
            raise RuntimeError(
                f"{city}: API error {response.status_code}: "
                f"{response.text[:300]}"
            )

        data = response.json()
        records = data.get("results", [])

        if not records:
            break

        for item in records:
            period = item.get("period") or {}
            start = period.get("datetimeFrom") or {}
            parameter = item.get("parameter") or {}

            all_records.append({
                "date": start.get("local") or start.get("utc"),
                "city": city,
                "sensor_id": sensor_id,
                "parameter": parameter.get("name"),
                "pm25_ug_m3": item.get("value"),
                "unit": parameter.get("units"),
            })

        print(f"Page {page}: {len(records)} records")

        if len(records) < LIMIT:
            break

        page += 1

    if not all_records:
        print(f"WARNING: {city} ke liye koi records nahi mile.")
        return

    df = pd.DataFrame(all_records)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["pm25_ug_m3"] = pd.to_numeric(
        df["pm25_ug_m3"], errors="coerce"
    )

    df = df.dropna(subset=["date"])
    df = df.sort_values("date")
    df = df.drop_duplicates(subset=["date", "sensor_id"])

    filename = f"{city.lower()}_pm25_2022_2024.csv"
    output_path = os.path.join(OUTPUT_DIR, filename)
    df.to_csv(output_path, index=False)

    print(f"\nSaved: {output_path}")
    print(f"Daily records: {len(df)}")
    print(f"First date: {df['date'].min()}")
    print(f"Last date: {df['date'].max()}")
    print(f"Missing PM2.5 values: {df['pm25_ug_m3'].isna().sum()}")
    print(f"Valid PM2.5 values: {df['pm25_ug_m3'].notna().sum()}")
    print(f"Units: {df['unit'].dropna().unique()}")


for city, sensor_id in CITIES.items():
    try:
        download_city(city, sensor_id)
    except Exception as error:
        print(f"\nERROR for {city}: {error}")
        print("Baaki cities ka download continue hoga.")

print("\nDownload process finished.")
