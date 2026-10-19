
import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAQ_API_KEY")

if not api_key:
    print("API key nahi mili. .env file check karein.")
else:
    response = requests.get(
        "https://api.openaq.org/v3/locations",
        headers={"X-API-Key": api_key},
        params={"parameters_id": 2, "limit": 1},
        timeout=30,
    )

    print("Status code:", response.status_code)

    if response.status_code == 200:
        print("Success! API key kaam kar rahi hai.")
    else:
        print("Error:", response.text[:300])
