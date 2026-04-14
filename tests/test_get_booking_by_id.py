import logging
import requests


def test_get_booking_by_id(base_url):
    response = requests.get(f"{base_url}/booking/1")
    data = response.json()
    
    logging.info(f"Booking data: {data}")
    
    assert response.status_code == 200
    assert "firstname" in data
    assert "lastname" in data
    assert "totalprice" in data
    assert "depositpaid" in data
    assert "bookingdates" in data