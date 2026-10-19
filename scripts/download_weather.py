
import requests
import pandas as pd
from pathlib import Path

CITIES = {
    "Lahore": (31.5204, 74.3587),
    "Karachi": (24.8607, 67.0011),
    "Islamabad": (33.6844, 73.0479),
    "Peshawar": (34.0151, 71.5249),
    "Quetta": (30.1798, 66.9750),
}

OUT = Path("data/raw/weather")
OUT.mkdir(parents=True, exist_ok=True)

for city, (lat, lon) in CITIES.items():
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": "2022-01-01",
        "end_date": "2024-12-31",
        "hourly": (
            "temperature_2m,relative_humidity_2m,"
            "precipitation,wind_speed_10m,wind_direction_10m"
        ),
        "timezone": "Asia/Karachi",
        "wind_speed_unit": "kmh",
    }

    response = requests.get(
        "https://archive-api.open-meteo.com/v1/archive",
        params=params,
        timeout=120,
    )
    response.raise_for_status()

    df = pd.DataFrame(response.json()["hourly"])
    df.insert(0, "city", city)

    path = OUT / f"{city.lower()}_weather.csv"
    df.to_csv(path, index=False)
    print(f"Saved {path}: {len(df)} hourly records")

print("Weather download complete.")
