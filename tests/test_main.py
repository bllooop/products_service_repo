import requests

api_url = 'http://localhost:8000'

def test_healthcheck():
    response = requests.get('http://localhost:8000/v1/products')
    assert response.status_code == 200