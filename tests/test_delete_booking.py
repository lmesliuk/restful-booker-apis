import logging
import requests
from conftest import BASE_URL

def test_delete_booking(auth_token, created_booking_id):
    headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Cookie": f"token={auth_token}"
    }

    response = requests.delete(f"{BASE_URL}/booking/{created_booking_id}", headers=headers)
    logging.info(f"Response: {response.text}")
        
    assert response.status_code == 201