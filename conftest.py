import pytest
import requests
import logging

BASE_URL = "https://restful-booker.herokuapp.com"

@pytest.fixture
def base_url():
    return BASE_URL # Return the base URL for the API

@pytest.fixture
def auth_token():
    payload = {"username": "admin", "password": "password123"}
    response = requests.post(f"{BASE_URL}/auth", json=payload)
    return response.json()["token"] # Return the authentication token for use in tests

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