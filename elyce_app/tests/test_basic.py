import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'MONGO_URI': 'mongodb://localhost:27017/mytestdb'  # Use a separate URI for testing
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_hello_world(client):
    response = client.get('/')
    assert response.data == b'Hello, World!'
    assert response.status_code == 200