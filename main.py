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
    'Drizzle': 'drizzle.jpg',
    'Thunderstorm': 'storm.jpg',
    'Snow': 'snow.jpg',
    'Mist': 'mist.jpg',
    'Fog': 'fog.jpg',
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

if __name__ == "__main__":
    main()