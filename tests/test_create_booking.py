import logging
import requests

def test_create_booking(base_url):
    payload = {
        "firstname": "Luciana",
        "lastname": "Mesliuk",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-06-01",
            "checkout": "2025-06-10"
        },
        "additionalneeds": "Breakfast"
    }
    
    response = requests.post(f"{base_url}/booking", json=payload)
    data = response.json()
    
    logging.info(f"Status: {response.status_code}")
    logging.info(f"Created booking ID: {data.get('bookingid')}")
    
    assert response.status_code == 200
    assert "bookingid" in data
    assert data["booking"]["firstname"] == "Luciana"