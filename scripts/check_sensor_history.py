
import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAQ_API_KEY")

if not API_KEY:
    raise ValueError("OPENAQ_API_KEY .env file mein nahi mili.")

headers = {"X-API-Key": API_KEY}
sensors = {
    "Lahore": 25135,
    "Karachi": 23747,
    "Islamabad": 25066,
    "Peshawar": 23455,
    "Quetta": 13340547,
}

for city, sensor_id in sensors.items():
    print("\n" + "=" * 45)
    print(f"{city} | Sensor ID: {sensor_id}")

    try:
        # Check sensor metadata and recorded date range
        url = f"https://api.openaq.org/v3/sensors/{sensor_id}"
        response = requests.get(url, headers=headers, timeout=30)
        print("Metadata status:", response.status_code)
        response.raise_for_status()

        payload = response.json()
        results = payload.get("results", [])
        if isinstance(results, dict):
            results = [results]

        if results:
            sensor = results[0]
            print("Name:", sensor.get("name"))
            print("First recorded:", sensor.get("datetimeFirst"))
            print("Last recorded:", sensor.get("datetimeLast"))
        else:
            print("No sensor metadata returned.")

        # Check daily records for 2022–2024
        url = f"https://api.openaq.org/v3/sensors/{sensor_id}/days"
        params = {
            "date_from": "2022-01-01T00:00:00+05:00",
            "date_to": "2024-12-31T23:59:59+05:00",
            "limit": 1,
            "page": 1,
        }
        response = requests.get(
            url, headers=headers, params=params, timeout=30
        )
        print("Daily-data status:", response.status_code)
        response.raise_for_status()

        payload = response.json()
        meta = payload.get("meta", {})
        print("API metadata:", meta)
        print("Sample record:", payload.get("results", [])[:1])

    except requests.RequestException as error:
        print("Request error:", error)
    except (ValueError, KeyError, TypeError) as error:
        print("Data/response error:", error)
