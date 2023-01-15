import requests

api_url = 'http://localhost:8000'

def test_healthcheck():
    response = requests.get(f'{api_url}/__health')
    assert response.status_code == 200


class testProductss():
    def test_get_blank_products():
        response = requests.get(f'{api_url}/v1/products')
        assert response.status_code == 200
        assert len(response.json()) == 0
    
    def test_add_product():
        body = {"name": "Apple", "price": 34, "shopid": 0 }
        response = requests.post(f'{api_url}/v1/products', json = body)
        assert response.status_code == 200
        assert response.json().get('name') == 'Apple'
        assert response.json().get('price') == 34
        assert response.json().get('shopid') == 0
        assert response.json().get('id') == 0

    def test_get_product_id():
        response = requests.post(f'{api_url}/v1/products/0')
        assert response.status_code == 200
        assert response.json().get('name') == 'Apple'
        assert response.json().get('price') == 34
        assert response.json().get('shopid') == 0
        assert response.json().get('id') == 0

    def test_get_product():
        response = requests.get(f'{api_url}/v1/products')
        assert response.status_code == 200
        assert len(response.json()) == 1
    