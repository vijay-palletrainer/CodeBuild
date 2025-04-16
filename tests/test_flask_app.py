import pytest
from my_project.flask_app import app as flask_app



@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_flask_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, Flask!" in response.data
