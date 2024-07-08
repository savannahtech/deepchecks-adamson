import io

import pytest
from fastapi.testclient import TestClient

from app.main import app
from . import setup_database


client = TestClient(app)


@pytest.fixture
def csv_data():
    return """
        id,Input,Output
        1,What is Deepchecks?,Deepchecks is an LLM Evaluation Tool
        2,When was Deepchecks founded?,Deepchecks was founded in 2024
        3,How are you doing?,I’m doing just fine, how about you?
    """


def test_create_interactions_from_csv(csv_data, setup_database):
    csv_bytes = csv_data.encode('utf-8')
    response = client.post(
        "/api/interactions/bulk",
        files={
            "csv_file": ("test.csv", io.BytesIO(csv_bytes), "text/csv")
        }
    )
    data = response.json()

    assert response.status_code == 200
    assert data["success"] == True


def test_create_interaction(setup_database):
    response = client.post(
        "/api/interactions",
        json={
            "input_text": "Test input",
            "output_text": "Test output"
        }
    )
    data = response.json()

    assert response.status_code == 200
    assert data["success"] == True