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
