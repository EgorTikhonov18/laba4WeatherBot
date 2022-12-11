import config
from urllib.request import urlopen
import json

class Coordinates:
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

def get_response(city_name: str) -> str:
        url = config.geo_api.format(city_name=city_name)
        return urlopen(url).read()

def get_coordinates(user_input: str) -> Coordinates:
        geo_response = get_response(
            city_name=user_input
        )
        coordinates = _parse_response(geo_response)
        print(coordinates.longitude, coordinates.latitude)
        return coordinates


def _parse_longitude(coord_dict: dict) -> str:
    return coord_dict[0]["lon"]


def _parse_latitude(coord_dict: dict) -> str:
    return coord_dict[0]["lat"]

def _parse_response(geo_response: str) -> Coordinates:
    coord_dict = json.loads(geo_response)
    return Coordinates(
        longitude=float(_parse_longitude(coord_dict)),latitude=float(_parse_latitude(coord_dict))
    )


