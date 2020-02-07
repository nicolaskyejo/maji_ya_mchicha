import pytest
from flask_app import __version__
from flask_app import restaurants


def test_version():
    assert __version__ == '0.1.0'


def test_blurhash_validity_checker():
    """Tests the blurhash checker function with some true and false values"""
    assert restaurants.blurhash_validity_checker('UUKJMXv|x]oz0gtRM{V@AHRQwvxZXSs9s;o0')
    assert restaurants.blurhash_validity_checker('UHNJ8q0KBGIpNMpIi]S6oxspD%nz%Mxt%2sk')
    assert not restaurants.blurhash_validity_checker('ABC')
    assert not restaurants.blurhash_validity_checker('-giH^b9+mCG}3XN$6*nh|,*JFtJBbL|tl8c=')
    assert not restaurants.blurhash_validity_checker('f+_}3Xot@;VdS;@uC%N5?xRJJvdtta_6yQ~v')


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
    """Tests that the search function returns expected results"""
    # test that it gives a known restaurant at its location
    restaurants_found = restaurants.search('falafel', [60.171, 24.939])
    test_dict = {restaurant['name']: restaurant for restaurant in restaurants_found['restaurants']}
    assert "Fafa's Sokos" in test_dict

    # test that both "O'Learys" and "Olearys" give a result
    restaurants_found = restaurants.search("O'Learys", [60.16799, 24.94055])
    assert len(restaurants_found['restaurants']) > 0
    restaurants_found = restaurants.search("OLearys", [60.16799, 24.94055])
    assert len(restaurants_found['restaurants']) > 0

    # test that both "north african" and "north-africa" give a result in tags (cuisine)
    restaurants_found = restaurants.search("north african", [60.16799, 24.94055])
    assert len(restaurants_found['restaurants']) > 0
    restaurants_found = restaurants.search("north-africa", [60.16799, 24.94055])
    assert len(restaurants_found['restaurants']) > 0

    # test that it gives a reasonable result of restaurants <= 3km
    restaurants_found = restaurants.search('veg', [60.17, 24.94])
    assert len(restaurants_found['restaurants']) >= 2

    # test that it gives a empty result with (lat, lon) from another country
    restaurants_found = restaurants.search('ramen', [39.223537, -76.897222])  # Wood elves way, MD, USA.
    assert len(restaurants_found['restaurants']) == 0
    restaurants_found = restaurants.search('veg', [40, 60])  # Turkmenistan
    assert len(restaurants_found['restaurants']) == 0
