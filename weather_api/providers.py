import requests as reqs
from abc import ABC, abstractmethod
from config import api_keys

class WeatherProvider(ABC):
    @abstractmethod
    def get_weather(self, city):
        pass

class OpenWeatherMapProvider(WeatherProvider):
    def __init__(self):
        self.api_key = api_keys.OPENWEATHER_KEY
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        parametr = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'ru'
        }

        try:
            response = reqs.get(self.base_url, params=parametr, timeout=10)
            response.raise_for_status()
            data = response.json()

            return {
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'wind_speed': data['wind']['speed'],
                'icon': data['weather'][0]['icon']
            }
        except reqs.exceptions.RequestException as e:
            raise Exception(f"Error {e}")
