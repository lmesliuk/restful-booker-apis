import requests

'''def test_api_is_alive():
    response = requests.get("https://restful-booker.herokuapp.com/ping")
    assert response.status_code == 201
'''    

def test_get_all_bookings(base_url):
    response = requests.get(f"{base_url}/booking")
    assert response.status_code == 200
    assert len(response.json()) > 0