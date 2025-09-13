from providers import OpenWeatherMapProvider
from cache import WeatherCache

class WeatherServices:
    def __init__(self):
        self.provider = OpenWeatherMapProvider()
        self.cache = WeatherCache()

    def get_weather(self, city):
        cached_data = self.cache.get(city)
        if cached_data:
            return cached_data
        print("hello")
        data = self.provider.get_weather(city)

        self.cache.set(city, data)

        return data