import os
import requests
from pathlib import Path
import geocoder

# Get user location dynamically
def get_location():
    g = geocoder.ip('me')
    if g.ok:
        return g.city
    return 'London'

# Configuration
CITY = get_location()  # Use dynamic location
WALLPAPER_DIR = Path(__file__).parent / 'wallpapers'  # Use wallpapers folder in the same directory

# Weather condition to wallpaper mapping
WALLPAPER_MAP = {
    'Clear': 'clear.jpg',
    'Clouds': 'cloudy.jpg',
    'Rain': 'rain.jpg',
    'Drizzle': 'rain.jpg',
    'Thunderstorm': 'storm.jpg',
    'Snow': 'snow.jpg',
    'Light Snow': 'snow.jpg',
    'Moderate Snow': 'snow.jpg',
    'Heavy Snow': 'snow.jpg',
    'Sleet': 'snow.jpg',
    'Hail': 'storm.jpg',
    'Mist': 'fog.jpg',
    'Fog': 'fog.jpg',
    'Overcast': 'cloudy.jpg',
    'Partly Cloudy': 'cloudy.jpg',
    'Light Rain': 'rain.jpg',
    'Moderate Rain': 'rain.jpg',
    'Heavy Rain': 'rain.jpg',
    'Showers': 'rain.jpg',
    'Blizzard': 'snow.jpg',
    'Freezing Rain': 'rain.jpg',
    'Freezing Fog': 'fog.jpg',
    'Patchy Rain Possible': 'rain.jpg',
    'Patchy Snow Possible': 'snow.jpg',
}

# Fetch weather data using wttr.in API
def get_weather():
    url = f'https://wttr.in/{CITY}?format=%C'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.strip()
    return None

# Main function
def main():
    weather = get_weather()
    print(f"Weather condition: {weather}")
    if weather in WALLPAPER_MAP:
        print(f"Mapped wallpaper: {WALLPAPER_MAP[weather]}")
    else:
        print("No matching wallpaper found.")

if __name__ == "__main__":
    main()
