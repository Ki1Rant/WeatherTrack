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
        self.base_url = "http://api.weatherapi.com/v1/current.json"

    def get_weather(self, city):
        parametr = {
            'key': self.api_key,
            'q': city,
            'aqi': 'no',
        }
        #url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={city}"

        try:
            response = reqs.get(self.base_url, params=parametr, timeout=10)
            #response = reqs.get(url)
            response.raise_for_status()
            data = response.json()

            return {
                'temperature': data['current']['temp_c'],
                'feels_like': data['current']['feelslike_c'],
                'description': data['current']['condition']['text'],
                'humidity': data['current']['humidity'],
                'pressure': data['current']['pressure_mb'],
                'wind_speed': data['current']['wind_kph'],
            }
        except reqs.exceptions.RequestException as e:
            raise Exception(f"Error {e}")
