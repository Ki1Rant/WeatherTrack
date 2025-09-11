import time
from config import setting

class WeatherCache:
    def __init__(self):
        self.cache = {}

    def get(self, city):
        if city in self.cache:
            cached_data, timestamp = self.cache[city]
            if time.time() - timestamp < setting.CACHE_TIMEOUT:
                return cached_data

        return None

    def set(self, city, data):
        self.cache[city] = (data, time.time())

