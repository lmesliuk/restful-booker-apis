import pytest
import requests
import logging

BASE_URL = "https://restful-booker.herokuapp.com"

'''@pytest.fixture
# To use only with different base URLs for different environments (e.g., staging, production)
def base_url():
    return BASE_URL # Return the base URL for the API
'''

@pytest.fixture(scope="session")
def auth_token():
    payload = {"username": "admin", "password": "password123"}
    response = requests.post(f"{BASE_URL}/auth", json=payload)
    return response.json()["token"] # Return the authentication token for use in tests

@pytest.fixture(scope="session") # I need to create a booking before running the tests, so I can use its ID in the tests
def created_booking_id(): # Create a booking and return its ID for use in tests
    payload = { 
        "firstname": "Luciana",
        "lastname": "Mesliuk",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-06-01",
            "checkout": "2025-06-10"
        },
        "additionalneeds": "Breakfast"
    }
    # Using BASE_URL constant directly instead of base_url fixture
    # because session-scoped fixtures cannot depend on function-scoped fixtures
    response = requests.post(f"{BASE_URL}/booking", json=payload) # Create a new booking
    return response.json()["bookingid"] # Return the ID of the created booking for use in tests


# Set up logging
logger = logging.getLogger() # Create a logger
logger.setLevel(logging.INFO) # Set the logging level to INFO (I can change it to DEBUG for more detailed logs)

# Logging format
formatter = logging.Formatter("%(levelname)s: %(message)s") # Define the logging format

# Console handler
console = logging.StreamHandler() # Create a console handler
console.setFormatter(formatter) # Set the formatter for the console handler

# File handler
file_handler = logging.FileHandler("test.log") # Create a file handler that writes to test.log
file_handler.setFormatter(formatter) # Set the formatter for the file handler

# Activate handlers 
logger.addHandler(console) # Add the console handler to the logger
logger.addHandler(file_handler) # Add the file handler to the logger
