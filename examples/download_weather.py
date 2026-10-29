from earthflux.weather import download_weather

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