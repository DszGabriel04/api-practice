from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from datetime import datetime
import pytz

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root_redirect():
    return RedirectResponse(url="/static/index.html")

@app.get("/time/{city}")
def get_city_time(city: str):
    """
    Get the current local time for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time. 
            Supported cities include: new_york, london, paris, tokyo, sydney, los_angeles, 
            chicago, berlin, mumbai, beijing, moscow, cape_town, dubai, singapore, rio.

    Returns:
        dict: A dictionary containing the city name, the current local time in 'YYYY-MM-DD HH:MM:SS' format,
            and the corresponding timezone.

    Raises:
        HTTPException: If the specified city is not supported, returns a 404 error.
    """
    # Mapping of common city names to timezones
    city_to_timezone = {
        "new_york": "America/New_York",
        "london": "Europe/London",
        "paris": "Europe/Paris",
        "tokyo": "Asia/Tokyo",
        "sydney": "Australia/Sydney",
        "los_angeles": "America/Los_Angeles",
        "chicago": "America/Chicago",
        "berlin": "Europe/Berlin",
        "mumbai": "Asia/Kolkata",
        "beijing": "Asia/Shanghai",
        "moscow": "Europe/Moscow",
        "cape_town": "Africa/Johannesburg",
        "dubai": "Asia/Dubai",
        "singapore": "Asia/Singapore",
        "rio": "America/Sao_Paulo"
    }
    tz_name = city_to_timezone.get(city.lower().replace(' ', '_'))
    if not tz_name:
        raise HTTPException(status_code=404, detail="City not supported.")
    tz = pytz.timezone(tz_name)
    city_time = datetime.now(tz)
    return {"city": city, "time": city_time.strftime('%Y-%m-%d %H:%M:%S'), "timezone": tz_name}