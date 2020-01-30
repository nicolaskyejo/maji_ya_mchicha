import pytest
from maji_ya_mchicha import __version__
from maji_ya_mchicha import restaurants


def test_version():
    assert __version__ == '0.1.0'


def test_load_restaurants():
    """Tests if the file is valid JSON"""
    restaurants_objects = restaurants.load_restaurants('../restaurants.json')
    assert type(restaurants_objects) == dict


def test_distance():
    """Tests distance given by Google from Vegekauppa to Rautatientori (2.2 km)
    within tolerance of 200 meters
    """
    assert restaurants.distance(60.186824, 24.960852, 60.171159, 24.945060) == pytest.approx(2.2, rel=2e-01)


def test_search():
    # test that it gives a reasonable location of restaurants <= 3km
    # test that it gives a empty json object with lat, lon from another country
    pass
