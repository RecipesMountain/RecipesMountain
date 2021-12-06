from app.main import __version__, app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_version():
    assert __version__ == "0.1.0"


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
