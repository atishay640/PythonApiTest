import requests
import jsonpath
from http import HTTPStatus
import pytest


@pytest.fixture
def base_url():
    return "http://samples.openweathermap.org/data/2.5/weather"

@pytest.fixture
def app_id():
    return "b6907d289e10d714a6e88b30761fae22"


def test_by_city_name(base_url,app_id):
    city = "London"
    url = f"{base_url}?q={city}&appid={app_id}"
    response = requests.get(url)
    assert response.status_code == HTTPStatus.OK
    body = response.json()
    city_name = jsonpath.jsonpath(body,"name")
    assert city_name[0] == city


def test_by_geographic_coordinates(base_url,app_id):
    lat = 139
    lon = 35
    url = f"{base_url}?lat={lat}&lon={lon}&appid={app_id}"
    response = requests.get(url)
    assert response.status_code == HTTPStatus.OK
    body = response.json()
    name = jsonpath.jsonpath(body, "name")
    assert name[0] == "Tawarano"



