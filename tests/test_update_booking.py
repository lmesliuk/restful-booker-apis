import logging
import requests
from conftest import BASE_URL

def test_update_booking(auth_token, created_booking_id):
    headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Cookie": f"token={auth_token}"
    }
    payload = {
        "firstname": "Luciana",
        "lastname": "Mesliuk",
        "totalprice": 500,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-06-01",
            "checkout": "2025-06-10"
        },
        "additionalneeds": "Breakfast"
    }
    
    response = requests.put(f"{BASE_URL}/booking/{created_booking_id}", headers=headers, json=payload)
    data = response.json()
    
    logging.info(f"Status: {response.status_code}")
    # logging.info(f"Updated booking ID: {data.get('bookingid')}")
    logging.info(f"Updated booking: {data}")
    logging.info(f"Response text: {response.text}")
    
    assert response.status_code == 200
    assert data["firstname"] == "Luciana"
    assert data["totalprice"] == 500
    assert data["depositpaid"] == False