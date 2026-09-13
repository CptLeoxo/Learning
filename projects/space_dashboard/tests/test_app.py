import pytest
from app import app

@pytest.fixture
def client():
    # Tells FLask im in a testing mode, if ship sinks, the captain going with it. 
    app.config['TESTING'] = True
    # Dummy client
    with app.test_client() as client:
        yield client

def test_homepage_loads(client):
    # Test that the main dashboard page returns a 200 OK status.
    response = client.get('/')
    assert response.status_code == 200