import config
from urllib.request import urlopen
import json
# json стэтхэм
from geo import Coordinates
class Weather:
    def __init__(self,temperature: float, weather:str, wind: float):
        self.temperature = temperature
        self.weather = weather
        self.wind = wind
        pass


def get_weather(coordinates: Coordinates) -> Weather:
    openweather_response = _get_openweather_response(
        longitude=coordinates.longitude, latitude=coordinates.latitude
    )
    weather = _parse_openweather_response(openweather_response)
    return weather


def _get_openweather_response(latitude: float, longitude: float) -> str:
    url = config.weather_api.format(latitude=latitude, longitude=longitude)
    return urlopen(url).read()


def _parse_openweather_response(openweather_response: str) -> Weather:
    openweather_dict = json.loads(openweather_response)
    return Weather(_parse_temperature(openweather_dict), _parse_description(openweather_dict), _parse_wind_speed(openweather_dict))


def _parse_description(openweather_dict) -> str:
    return str(openweather_dict['weather'][0]['description']).capitalize()

def _parse_wind_speed(openweather_dict: dict) -> float:
    return openweather_dict['wind']['speed']

def _parse_temperature(openweather_dict: dict) -> float:
    return openweather_dict['main']['temp']