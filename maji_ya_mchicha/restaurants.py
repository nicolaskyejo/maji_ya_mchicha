import json


def load_restaurants(file='../restaurants.json'):
    """Opens a file and returns a JSON object"""
    with open(file, 'r') as f:
        return json.load(f)
