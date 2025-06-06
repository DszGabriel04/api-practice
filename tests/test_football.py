import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_football_scores_csv_url_inaccessible(monkeypatch):
    def mock_read_csv(*args, **kwargs):
        raise Exception("CSV URL is inaccessible")

    monkeypatch.setattr("pandas.read_csv", mock_read_csv)

    response = client.get("/football/scores/arsenal")
    assert response.status_code == 500
    assert response.json() == {"detail": "CSV URL is inaccessible"}

def test_get_football_scores_non_existent_team():
    response = client.get("/football/scores/non_existent_team")
    assert response.status_code == 200
    assert response.json() == {"team": "non_existent_team", "scores": []}

def test_get_football_scores_existing_team():
    response = client.get("/football/scores/Arsenal FC")
    assert response.status_code == 200
    
    data = response.json()
    assert "team" in data
    assert data["team"].lower() == "arsenal fc"
    assert "scores" in data
    assert isinstance(data["scores"], list)
    assert len(data["scores"]) > 0  # Ensure there are scores returned