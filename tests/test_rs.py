from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_reverse_string_hello():
    response = client.get("/rs/hello")
    assert response.status_code == 200
    assert response.json() == "olleh"

def test_reverse_string():
    response = client.get("/rs/abc123")
    assert response.status_code == 200
    assert response.json() == "321cba"

def test_reverse_string_palindrome():
    response = client.get("/rs/racecar")
    assert response.status_code == 200
    assert response.json() == "racecar"

def test_reverse_string_single_character():
    response = client.get("/rs/a")
    assert response.status_code == 200
    assert response.json() == "a"

def test_reverse_string_japanese_characters():
    response = client.get("/rs/はちにんこ")
    assert response.status_code == 200
    assert response.json() == "こんにちは"

def test_reverse_string_with_emojis():
    response = client.get("/rs/%F0%9F%98%81%F0%9F%98%84%F0%9F%98%83%F0%9F%98%80")
    assert response.status_code == 200
    assert response.json() == "😀😃😄😁"