from maji_ya_mchicha import __version__, restaurants


def test_version():
    assert __version__ == '0.1.0'


def test_load_restaurants():
    restaurants_objects = restaurants.load_restaurants('../restaurants.json')
    assert type(restaurants_objects) == dict
