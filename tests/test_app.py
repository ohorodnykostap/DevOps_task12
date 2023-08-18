import pytest
import json
from app import app
from db import *

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        init_db()
        yield client
        clear_db()

def test_get_products(client):
    response = client.get('/api/products')
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, list)

def test_create_product(client):
    response = client.post('/api/products', json={'name': 'Test Product', 'price': 10})
    data = response.get_json()

    assert response.status_code == 201
    assert 'message' in data
    assert 'productId' in data

    product_id = data['productId']
    product = get_product_by_id(product_id)
    assert product is not None
    assert product.name == 'Test Product'

def test_get_product_by_id(client):
    product = create_product('Test Product', 10)
    response = client.get(f'/api/products/{product.id}')
    data = response.get_json()

    assert response.status_code == 200
    assert 'id' in data
    assert 'name' in data
    assert 'price' in data

def test_update_product(client):
    product = create_product('Test Product', 10)
    response = client.patch(f'/api/products/{product.id}', json={'price': 15})
    data = response.get_json()

    assert response.status_code == 200
    assert 'message' in data

    updated_product = get_product_by_id(product.id)
    assert updated_product.price == 15

def test_delete_product(client):
    product = create_product('Test Product', 10)
    response = client.delete(f'/api/products/{product.id}')
    data = response.get_json()

    assert response.status_code == 200
    assert 'message' in data

    deleted_product = get_product_by_id(product.id)
    assert deleted_product is None
