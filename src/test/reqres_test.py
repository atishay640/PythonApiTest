import requests
from http import HTTPStatus
import pytest
from src.main.python.model.user import *


@pytest.fixture
def base_url():
    return "https://reqres.in"


def test_create_user(base_url):
    url = f"{base_url}/api/users"
    data = {
        "name": "morpheus",
        "job": "leader",
        "id": "193",
        "createdAt": "2019-09-28T10:27:49.036Z"
    }
    response = requests.post(url=url,data=data)
    assert response.status_code == HTTPStatus.CREATED


def test_update_user(base_url):
    url = f"{base_url}/api/users/2"
    data = {
        "name": "simon",
        "job": "manager",
        "createdAt": "2019-09-28T10:27:49.036Z"
    }
    response = requests.put(url=url,data=data)
    assert response.status_code == HTTPStatus.OK


def test_delete_user(base_url):
    url = f"{base_url}/api/users/2"
    response = requests.delete(url=url)
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_get_user(base_url):
    id = 2
    url = f"{base_url}/api/users/{id}"
    response = requests.get(url=url)
    body = response.json()
    user_json = body["data"]
    user = User.from_json_or_dict(user_json)
    assert user.id == id
    assert user.first_name == "Janet"
    assert user.last_name == "Weaver"
    assert user.email == "janet.weaver@reqres.in"