import os
import requests
from pathlib import Path
import geocoder
import time
from datetime import datetime

# Get the user's location based on IP address
def get_user_location():
    location = geocoder.ip('me')
    return location.city if location.ok else 'london'  # Default to 'london'

# Configuration
city = get_user_location()
wallpaper_dir = Path(__file__).parent / 'wallpapers'

# Map weather conditions to wallpaper images
wallpaper_map = {
    'clear': 'clear.jpg',
    'clouds': 'cloudy.jpg',
    'rain': 'rain.jpg',
    'drizzle': 'rain.jpg',
    'thunderstorm': 'storm.jpg',
    'snow': 'snow.jpg',
    'mist': 'fog.jpg',
    'fog': 'fog.jpg',
    'overcast': 'cloudy.jpg',
    'partly cloudy': 'cloudy.jpg',
    'light rain': 'rain.jpg',
    'moderate rain': 'rain.jpg',
    'heavy rain': 'rain.jpg',
    'showers': 'rain.jpg',
    'blizzard': 'snow.jpg',
    'freezing rain': 'rain.jpg',
    'freezing fog': 'fog.jpg',
    'patchy rain possible': 'rain.jpg',
    'patchy snow possible': 'snow.jpg',
}

# Fetch current weather condition
def get_current_weather():
    url = f'https://wttr.in/{city}?format=%C'
    response = requests.get(url)
    return response.text.strip().lower()

# Set the wallpaper based on the given image path
def set_desktop_wallpaper(image_path):
    if os.name == 'nt':  # Windows
        import ctypes
        ctypes.windll.user32.SystemParametersInfoW(20, 0, str(image_path), 0)
    elif os.name == 'posix':  # Linux and macOS
        os.system(f'gsettings set org.gnome.desktop.background picture-uri file://{image_path}')

# Main function
def main():
    while True:
        weather = get_current_weather()
        wallpaper_file = wallpaper_map.get(weather, 'clear.jpg')
        wallpaper_path = wallpaper_dir / wallpaper_file

        if wallpaper_path.exists():
            set_desktop_wallpaper(wallpaper_path)

        time.sleep(1800)  # Wait for 30 minutes before updating again

if __name__ == "__main__":
    main()
