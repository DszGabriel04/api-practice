from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_generate_random_number_range_within_bounds():
    response = client.get("/rn/1/10")
    assert response.status_code == 200
    random_number = response.json()["random_number"]
    assert 1 <= random_number <= 10

def test_generate_random_number_range_min_equal_max():
    response = client.get("/rn/5/5")
    assert response.status_code == 400
    assert response.json() == {"detail": "Minimum value must be less than maximum value."}

def test_generate_random_number_min_greater_than_max():
    response = client.get("/rn/10/1")
    assert response.status_code == 400
    assert response.json() == {"detail": "Minimum value must be less than maximum value."}

def test_generate_random_number_range_negative_bounds():
    response = client.get("/rn/-10/-1")
    assert response.status_code == 200
    random_number = response.json()["random_number"]
    assert -10 <= random_number <= -1

def test_generate_random_number_min_zero():
    response = client.get("/rn/0/10")
    assert response.status_code == 200
    random_number = response.json()["random_number"]
    assert 0 <= random_number <= 10