import requests

BASE_URL = "https://restful-booker.herokuapp.com"

def test_get_auth_token(base_url, auth_token): # Use the auth_token fixture
    assert auth_token is not None # Check if the token is not None
    assert auth_token != "" # Check if the token is not empty
    
    