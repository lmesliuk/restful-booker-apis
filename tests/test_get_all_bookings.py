import requests
import logging

def test_get_all_bookings(base_url):
    response = requests.get(f"{base_url}/booking") # Use the base_url fixture
    #logging.info(f"GET /booking response: {response.status_code} - {response.text}") # Log the response status and body
    logging.info(f"Total bookings: {len(response.json())}")
    assert response.status_code == 200 # Check if the status code is 200
    assert len(response.json()) > 0 # Check if there is at least one booking in the response