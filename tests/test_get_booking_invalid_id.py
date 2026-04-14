import logging
from urllib import response
import requests

def test_get_booking_invalid_id(base_url):
    response = requests.get(f"{base_url}/booking/999999")
    logging.info(f"Status: {response.status_code}")
    assert response.status_code == 404