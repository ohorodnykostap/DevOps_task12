from app import app

def test_homepage():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the App" in response.data

