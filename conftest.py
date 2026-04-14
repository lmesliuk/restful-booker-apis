import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com"

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def auth_token():
    payload = {"username": "admin", "password": "password123"}
    response = requests.post(f"{BASE_URL}/auth", json=payload)
    return response.json()["token"]