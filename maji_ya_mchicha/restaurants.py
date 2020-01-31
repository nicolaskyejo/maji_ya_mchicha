import json
from math import cos, asin, sqrt, pi
from typing import List


def load_restaurants(file: str = '../restaurants.json') -> dict:
    """Opens a file and returns a JSON object"""
    with open(file, 'r', encoding='utf8') as f:
        return json.load(f)


# copied and adapted from https://github.com/halcy/blurhash-python
def blurhash_validity_checker(blurhash: str) -> bool:
    """Checks if a blurhash is valid and returns True or False"""
    if len(blurhash) < 6:
        return False

    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$%*+,-.:;=?@[]^_{|}~"
    alphabet_values = dict(zip(alphabet, range(len(alphabet))))
    size_info = alphabet_values[blurhash[0]]
    size_y = int(size_info / 9) + 1
    size_x = (size_info % 9) + 1
    if len(blurhash) != 4 + 2 * size_x * size_y:
        return False
    return True


# https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula/21623206#21623206
# Haversine formula
def distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate the distance between two coordinates in kilometers"""
    p = pi / 180
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))  # 2 * Radius of the Earth in km * asin...


def search(query: str, location: List[float]) -> dict:
    """Searches for restaurants using query string in (name, description and tags) fields,
    and finds restaurants closer than 3 km (< 3 km), and finally returns a dict with matched
    restaurant objects
    """
    all_restaurants = load_restaurants()
    restaurants_matches_list = []
    # It is a bit faster to search in dict, than a list (which is present in the data structure)
    name_dict = {restaurant['name']: restaurant for restaurant in all_restaurants['restaurants']}
    description_dict = {restaurant['description']: restaurant for restaurant in all_restaurants['restaurants']}
    tags_dict = {', '.join(restaurant['tags']): restaurant for restaurant in all_restaurants['restaurants']}

    # Checking for query matches and adding matches found
    for name in name_dict:
        if query.lower() in name.lower():
            restaurants_matches_list.append(name_dict[name])
    for description in description_dict:
        if query.lower() in description.lower():
            if description_dict[description] in restaurants_matches_list:
                continue
            restaurants_matches_list.append(description_dict[description])
    for tags in tags_dict:
        if query.lower() in tags.lower():
            if tags_dict[tags] in restaurants_matches_list:
                continue
            restaurants_matches_list.append(tags_dict[tags])

    # Then check the distance
    for query_match in restaurants_matches_list:
        restaurant_lat, restaurant_lon = map(float, query_match['location'])  # restaurant lat, lon are already
        # of type Float, but it doesn't hurt to double check
        user_lat, user_lon = location
        distance_between = distance(restaurant_lat, restaurant_lon, user_lat, user_lon)
        if distance_between > 3:  # remove restaurant from results if true
            restaurants_matches_list.remove(query_match)

    if len(restaurants_matches_list) == 0:
        return {}  # i.e no matches
    return {"restaurants": restaurants_matches_list}
