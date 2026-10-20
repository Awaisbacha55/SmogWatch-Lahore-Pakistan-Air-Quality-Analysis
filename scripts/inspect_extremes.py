
import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAQ_API_KEY")

# City, sensor ID, date to investigate
checks = [
    ("Karachi", 23747, "2022-04-21"),
    ("Peshawar", 23455, "2023-09-30"),
    ("Peshawar", 23455, "2023-10-01"),
    ("Peshawar", 23455, "2023-10-02"),
    ("Lahore", 25135, "2024-11-14"),
]

if not API_KEY:
    raise SystemExit("OPENAQ_API_KEY missing from .env")

headers = {"X-API-Key": API_KEY}

for city, sensor_id, target_date in checks:
    print(f"\n{'=' * 50}")
    print(f"{city} | {target_date} | Sensor {sensor_id}")
    print("=" * 50)

    url = f"https://api.openaq.org/v3/sensors/{sensor_id}/days"

    # Inspect the target date and two days on either side
    start = (
        pd.Timestamp(target_date) - pd.Timedelta(days=2)
    ).strftime("%Y-%m-%d")
    end = (
        pd.Timestamp(target_date) + pd.Timedelta(days=3)
    ).strftime("%Y-%m-%d")

    params = {
        "date_from": start,
        "date_to": end,
        "limit": 20,
        "page": 1,
    }

    try:
        response = requests.get(
            url, headers=headers, params=params, timeout=60
        )
        print("HTTP status:", response.status_code)
        response.raise_for_status()

        results = response.json().get("results", [])

        if not results:
            print("No records returned for this date range.")
            continue

        for item in results:
            period = item.get("period") or {}
            start_time = period.get("datetimeFrom") or {}
            coverage = item.get("coverage") or {}

            print({
                "date": start_time.get("local") or start_time.get("utc"),
                "value": item.get("value"),
                "flagInfo": item.get("flagInfo"),
                "coverage_percent": coverage.get("percentCoverage"),
                "observed_count": coverage.get("observedCount"),
                "expected_count": coverage.get("expectedCount"),
            })

    except requests.RequestException as error:
        print("Request failed:", error)

print("\nInspection finished.")
