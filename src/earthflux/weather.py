
"""Download historical daily weather data using Open-Meteo."""

from datetime import date
from pathlib import Path
import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen

import pandas as pd


API_URL = "https://archive-api.open-meteo.com/v1/archive"


def download_weather(
    latitude: float,
    longitude: float,
    start_date: str,
    end_date: str,
    output_file: str | Path,
) -> pd.DataFrame:
    """Download, validate, and save daily weather data."""

    # Check that the user's inputs are valid.
    if not -90 <= latitude <= 90:
        raise ValueError("Latitude must be between -90 and 90.")

    if not -180 <= longitude <= 180:
        raise ValueError("Longitude must be between -180 and 180.")

    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)

    if start > end:
        raise ValueError("Start date must not be after end date.")

    # Build the request parameters.
    parameters = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": (
            "temperature_2m_max,"
            "temperature_2m_min,"
            "precipitation_sum"
        ),
        "timezone": "UTC",
    }

    url = f"{API_URL}?{urlencode(parameters)}"

    # Send the HTTP request.
    try:
        with urlopen(url, timeout=30) as response:
            data = json.load(response)
    except (HTTPError, URLError, TimeoutError) as exc:
        raise RuntimeError(
            f"Weather data request failed: {exc}"
        ) from exc

    # Check that the API returned the expected fields.
    daily = data.get("daily")

    required = (
        "time",
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum",
    )

    if not isinstance(daily, dict):
        raise ValueError("API response is missing daily data.")

    missing = [key for key in required if key not in daily]

    if missing:
        raise ValueError(f"Missing weather variables: {missing}")

    if len({len(daily[key]) for key in required}) != 1:
        raise ValueError("Weather variables have unequal lengths.")

    # Convert the response into a pandas DataFrame.
    df = pd.DataFrame(
        {
            "date": daily["time"],
            "tmax_c": daily["temperature_2m_max"],
            "tmin_c": daily["temperature_2m_min"],
            "precipitation_mm": daily["precipitation_sum"],
        }
    )

    df["date"] = pd.to_datetime(df["date"])

    # Save the downloaded data.
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)

    return df

from earthflux.weather import download_weather

# Download January 2025 weather data for Columbia, Missouri.
weather = download_weather(
    latitude=38.9517,
    longitude=-92.3341,
    start_date="2025-01-01",
    end_date="2025-01-31",
    output_file="data/columbia_weather_2025_01.csv",
)

print("Weather data downloaded successfully!")
print(weather.head())
print(f"\nTotal days downloaded: {len(weather)}")
