import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/api/products')  # Оновіть маршрут тут
    assert response.status_code == 200

