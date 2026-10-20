
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAQ_API_KEY")

sensors = {
    "Karachi": 23747,
    "Lahore": 25135,
    "Peshawar": 23455,
    "Islamabad": 25066,
}

if not API_KEY:
    raise SystemExit("OPENAQ_API_KEY missing from .env")

headers = {"X-API-Key": API_KEY}

# Look for flags around the dates we identified
date_ranges = [
    ("2022-04-19", "2022-04-25"),
    ("2023-09-28", "2023-10-05"),
    ("2024-11-12", "2024-11-17"),
]

for city, sensor_id in sensors.items():
    for start, end in date_ranges:
        # Only query date ranges relevant to each city
        if city == "Karachi" and start != "2022-04-19":
            continue
        if city == "Peshawar" and start != "2023-09-28":
            continue
        if city == "Lahore" and start != "2024-11-12":
            continue
        if city == "Islamabad":
            continue

        print(f"\n{city}: {start} to {end}")

        url = f"https://api.openaq.org/v3/sensors/{sensor_id}/flags"
        params = {
            "datetime_from": start,
            "datetime_to": end,
            "limit": 100,
            "page": 1,
        }

        try:
            response = requests.get(
                url, headers=headers, params=params, timeout=60
            )
            print("HTTP status:", response.status_code)
            response.raise_for_status()

            data = response.json()
            results = data.get("results", [])

            if not results:
                print("No flag records returned for this range.")
                continue

            for item in results:
                flag_type = item.get("flagType") or {}
                start_time = item.get("datetimeFrom") or {}

                print({
                    "flag": flag_type.get("label"),
                    "level": flag_type.get("level"),
                    "note": item.get("note"),
                    "from": start_time.get("local") or start_time.get("utc"),
                    "sensor_ids": item.get("sensorIds"),
                })

        except requests.RequestException as error:
            print("Request failed:", error)

print("\nFlag inspection finished.")
