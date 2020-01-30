import pytest
import json
from maji_ya_mchicha import app


@pytest.fixture
def client():
    with app.app.test_client() as client:
        yield client


def test_not_found_error(client):
    """Tests response for invalid URLs"""
    response = client.get('/')
    assert b'Resource not found' in response.data
    assert response.status_code == 404


def test_restaurants_all(client):
    """Tests that the response is valid JSON and contains at least
    the 'restaurants' object
    """
    response = client.get('/restaurants')
    json_data = json.loads(response.data)
    assert 'restaurants' in json_data


def test_restaurants_search(client):
    """Tests different scenarios when search endpoint is accessed"""
    url = '/restaurants/search'
    # test that None or empty parameters returns an error
    assert b'Malformed request' in client.get(url).data
    # test minimum length is accepted
    assert b'Malformed request' not in client.get(url + '?q=b&lat=2&lon=1').data
    # test that all parameters are given / if a parameter is missing, return an error
    assert b'Malformed request' in client.get(url + '?q=pizza&lat=&lon=60').data  # lat missing
    assert b'Malformed request' in client.get(url + '?q=pizza&lat=24&lon=').data  # lon missing
    assert b'Malformed request' in client.get(url + '?q=&lat=24&lon=60').data  # q missing

    # test that it returns valid json
    # url = 'restaurants/search?q=vegan&lat=25.21&lon=40.11'
    # response = client.get(url)
    # json_data = json.loads(response.data)
    # assert 'restaurants' in json_data
