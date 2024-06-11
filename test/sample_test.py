from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.mark.parametrize("country, season", [
    ("France", "summer"),
    ("Italy", "spring"),
    ("Spain", "winter"),
    ("Germany", "autumn"),
    ("Japan", "spring"),
])

def test_post_recommendations(country, season):
    # Test case for POST /recommendations endpoint
    params = {
        "country": country,
        "season": season
    }
    response = client.post("/recommendations", params=params)
    assert response.status_code == 200
    assert "uid" in response.json()

def test_get_recommendation_by_id(uid):
    # Test case for GET /recommendations/{id} endpoint
    response = client.get(f"/status/{uid}")
    assert response.status_code == 200
    assert response.json() == {
        "uid": uid,
        "status": "completed"
    }
