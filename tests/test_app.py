from quote_disp.app import app, health
import pytest

@pytest.fixture
def test_client():
    app.config.update({'TESTING': True})
    with app.test_client() as client:
        yield client

def test_health():
    assert health() == 'healthy'

def test_health_route(test_client):
    response = test_client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data