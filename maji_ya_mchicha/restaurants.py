import json
from math import cos, asin, sqrt, pi


def load_restaurants(file: str = '../restaurants.json') -> dict:
    """Opens a file and returns a JSON object"""
    with open(file, 'r') as f:
        return json.load(f)


# https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula/21623206#21623206
# Haversine formula
def distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate the distance between two coordinates in kilometers"""
    p = pi / 180
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))  # 2 * Radius of the Earth in km * asin...


def search():
    pass
