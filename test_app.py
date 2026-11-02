
import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_prediction():
    response = client.post(
        "/predict",
        json={"study_hours": 6}
    )
    assert response.status_code == 200
    assert response.json()["predicted_score"] == pytest.approx(68.16)


def test_invalid_study_hours():
    response = client.post(
        "/predict",
        json={"study_hours": 30}
    )
    assert response.status_code == 422
