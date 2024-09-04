import pytest
from flask import url_for
from app import create_app

@pytest.fixture
def app():
    from app.config import TestingConfig
    app = create_app(TestingConfig)
    return app

def test_home_page(client):
    response = client.get(url_for('index.home'))
    assert response.status_code == 200
    assert b"Write about one of your goals" in response.data

# def test_form_submission(client):
#     response = client.post(url_for('index.home'), data={'comment': 'Achieve something great'})
#     assert response.status_code in [200, 302]