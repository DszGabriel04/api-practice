import pytest
from fastapi.testclient import TestClient
from datetime import datetime
from unittest.mock import patch
from main import app

client = TestClient(app)

def test_get_city_time_valid_city():
    with patch('main.datetime') as mock_datetime:
        mock_now = datetime(2023, 5, 1, 12, 0, 0)
        mock_datetime.now.return_value = mock_now
        
        response = client.get("/time/new_york")
        assert response.status_code == 200
        
        data = response.json()
        assert data["city"] == "new_york"
        assert data["time"] == "2023-05-01 12:00:00"
        assert data["timezone"] == "America/New_York"

def test_get_city_time_case_insensitive():
    with patch('main.datetime') as mock_datetime:
        mock_now = datetime(2023, 5, 1, 12, 0, 0)
        mock_datetime.now.return_value = mock_now

        response = client.get("/time/NEW YORK")
        assert response.status_code == 200
        assert response.json() == {
            "city": "NEW YORK",
            "time": "2023-05-01 12:00:00",
            "timezone": "America/New_York"
        }

        response = client.get("/time/new york")
        assert response.status_code == 200
        assert response.json() == {
            "city": "new york",
            "time": "2023-05-01 12:00:00",
            "timezone": "America/New_York"
        }

def test_get_city_time_unsupported_city():
    response = client.get("/time/unsupported_city")
    assert response.status_code == 404
    assert response.json() == {"detail": "City not supported."}

def test_get_city_time_with_spaces():
    response = client.get("/time/los angeles")
    assert response.status_code == 200
    data = response.json()
    assert data["city"] == "los angeles"
    assert data["timezone"] == "America/Los_Angeles"
    assert datetime.strptime(data["time"], '%Y-%m-%d %H:%M:%S')

@pytest.mark.parametrize("city, dst_date, non_dst_date", [
    ("new_york", "2023-03-12 02:30:00", "2023-11-05 01:30:00"),
    ("london", "2023-03-26 01:30:00", "2023-10-29 01:30:00"),
    ("paris", "2023-03-26 02:30:00", "2023-10-29 02:30:00"),
])
def test_get_city_time_dst_transition(city, dst_date, non_dst_date):
    with patch('main.datetime') as mock_datetime:
        # Test during DST
        mock_datetime.now.return_value = datetime.fromisoformat(dst_date)
        response = client.get(f"/time/{city}")
        assert response.status_code == 200
        dst_result = response.json()
        
        # Test outside of DST
        mock_datetime.now.return_value = datetime.fromisoformat(non_dst_date)
        response = client.get(f"/time/{city}")
        assert response.status_code == 200
        non_dst_result = response.json()
        
        # Check that the timezone is the same, but the times are different
        assert dst_result["timezone"] == non_dst_result["timezone"]
        assert dst_result["time"] != non_dst_result["time"]

def test_supported_cities_timezone():
    supported_cities = [
        "new_york", "london", "paris", "tokyo", "sydney",
        "los_angeles", "chicago", "berlin", "kolkata", "shanghai",
        "moscow", "johannesburg", "dubai", "singapore", "sao_paulo"
    ]
    expected_timezones = [
        "America/New_York", "Europe/London", "Europe/Paris", "Asia/Tokyo",
        "Australia/Sydney", "America/Los_Angeles", "America/Chicago",
        "Europe/Berlin", "Asia/Kolkata", "Asia/Shanghai", "Europe/Moscow",
        "Africa/Johannesburg", "Asia/Dubai", "Asia/Singapore", "America/Sao_Paulo"
    ]
    
    for city, expected_tz in zip(supported_cities, expected_timezones):
        response = client.get(f"/time/{city}")
        assert response.status_code == 200
        assert response.json()["timezone"] == expected_tz

def test_get_city_time_format():
    with patch('main.datetime') as mock_datetime:
        mock_now = mock_datetime.now.return_value
        mock_now.strftime.return_value = '2023-05-01 12:34:56'
        
        response = client.get("/time/london")
        assert response.status_code == 200
        
        data = response.json()
        assert 'time' in data
        assert data['time'] == '2023-05-01 12:34:56'

def test_get_city_time_consistency():
    city = "tokyo"
    responses = [client.get(f"/time/{city}") for _ in range(5)]
    
    assert all(response.status_code == 200 for response in responses)
    
    data = [response.json() for response in responses]
    assert all(item["city"] == city for item in data)
    assert all(item["timezone"] == "Asia/Tokyo" for item in data)
    
    times = [datetime.strptime(item["time"], '%Y-%m-%d %H:%M:%S') for item in data]
    time_diffs = [(times[i+1] - times[i]).total_seconds() for i in range(len(times)-1)]
    
    assert all(0 <= diff <= 1 for diff in time_diffs), "Time differences should be within 1 second"

def test_get_city_time_special_characters():
    with patch('main.datetime') as mock_datetime:
        mock_now = datetime(2023, 5, 1, 12, 0, 0)
        mock_datetime.now.return_value = mock_now

        response = client.get("/time/new_york123!@#")
        assert response.status_code == 200
        assert response.json() == {
            "city": "new_york123!@#",
            "time": "2023-05-01 12:00:00",
            "timezone": "America/New_York"
        }

        response = client.get("/time/L0S_@NG3L3S")
        assert response.status_code == 200
        assert response.json() == {
            "city": "L0S_@NG3L3S",
            "time": "2023-05-01 12:00:00",
            "timezone": "America/Los_Angeles"
        }