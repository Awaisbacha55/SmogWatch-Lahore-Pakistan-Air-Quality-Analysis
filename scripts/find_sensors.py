
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAQ_API_KEY")
BASE_URL = "https://api.openaq.org/v3"
HEADERS = {"X-API-Key": API_KEY}

CITIES = {
    "Lahore": (31.5204, 74.3587),
    "Karachi": (24.8607, 67.0011),
    "Islamabad": (33.6844, 73.0479),
    "Peshawar": (34.0151, 71.5249),
    "Quetta": (30.1798, 66.9750),
}

if not API_KEY:
    raise SystemExit("API key nahi mili. .env file check karein.")

for city, (lat, lon) in CITIES.items():
    print(f"\n{'=' * 45}")
    print(f"City: {city}")
    print("=" * 45)

    try:
        response = requests.get(
            f"{BASE_URL}/locations",
            headers=HEADERS,
            params={
                "coordinates": f"{lat},{lon}",
                "radius": 25000,
                "parameters_id": 2,
                "limit": 1000,
            },
            timeout=60,
        )

        print("HTTP status:", response.status_code)

        if response.status_code != 200:
            print("API error:", response.text[:300])
            continue

        locations = response.json().get("results", [])
        print("Locations found:", len(locations))

        for location in locations:
            print(
                "Location ID:", location.get("id"),
                "| Name:", location.get("name"),
                "| Sensors:", len(location.get("sensors", []))
            )

            for sensor in location.get("sensors", []):
                parameter = sensor.get("parameter", {})
                if parameter.get("id") == 2 or parameter.get("name") == "pm25":
                    print("  PM2.5 sensor:", sensor.get("id"))
                    print("  Parameter:", parameter.get("name"))
                    print("  Sensor data:", sensor.get("datetimeFirst"),
                          "to", sensor.get("datetimeLast"))

    except requests.RequestException as error:
        print("Connection error:", error)
