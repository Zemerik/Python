"""
Exercise 1: Weather App (API Interaction)
Create a weather app that:
- Fetches current weather from OpenWeatherMap API
- Accepts city name input
- Displays formatted temperature/humidity
"""

import requests
import os

class WeatherApp:
    """Weather app using OpenWeatherMap API"""
    
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    DEMO_MODE = True  # Set to False to use real API
    DEMO_RESPONSE = {
        "main": {"temp": 293.15, "humidity": 56},
        "weather": [{"description": "clear sky"}],
        "name": "Demo City"
    }
    
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("OPENWEATHER_API_KEY")
    
    def fetch_weather(self, city):
        if self.DEMO_MODE or not self.api_key:
            print("[Demo mode] Returning mock weather data.")
            return self.DEMO_RESPONSE
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }
        try:
            resp = requests.get(self.BASE_URL, params=params, timeout=5)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            print(f"Error fetching weather: {e}")
            return None
    
    def display_weather(self, data):
        if not data:
            print("No weather data available.")
            return
        city = data.get("name", "Unknown")
        main = data.get("main", {})
        weather = data.get("weather", [{}])[0]
        temp = main.get("temp")
        humidity = main.get("humidity")
        desc = weather.get("description", "N/A")
        print(f"Weather for {city}:")
        print(f"  Description: {desc}")
        print(f"  Temperature: {temp}°C" if temp is not None else "  Temperature: N/A")
        print(f"  Humidity: {humidity}%" if humidity is not None else "  Humidity: N/A")

def main():
    print("=== Weather App ===")
    app = WeatherApp()
    while True:
        city = input("Enter city name (or 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            break
        data = app.fetch_weather(city)
        app.display_weather(data)

if __name__ == "__main__":
    main() 