from fastapi.testclient import TestClient
from app.main import app
from . import setup_database

client = TestClient(app)


def test_get_alerts(setup_database):
    response = client.get("api/alerts")
    data = response.json()

    assert response.status_code == 200
    assert data["success"] == True
    assert isinstance(data["data"], list)