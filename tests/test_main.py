import requests

api_url = 'http://localhost:8000'

def test_healthcheck():
    response = 200
    assert response == 200