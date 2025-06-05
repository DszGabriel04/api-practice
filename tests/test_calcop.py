from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_calculator_subtract_larger_from_smaller():
    response = client.get("/calculator/sub/10/3")
    assert response.status_code == 200
    assert response.json() == 7
def test_calculator_add_two_positive_integers():
    response = client.get("/calculator/add/5/3")
    assert response.status_code == 200
    assert response.json() == 8
def test_calculator_operation_mul_negative_integers():
    response = client.get("/calculator/mul/-3/-4")
    assert response.status_code == 200
    assert response.json() == 12
def test_calculator_operation_div_positive_integers():
    response = client.get("/calculator/div/10/2")
    assert response.status_code == 200
    assert response.json() == 5
def test_calculator_operation_division_by_zero():
    response = client.get("/calculator/div/10/0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Division by zero is not allowed."}