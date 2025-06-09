from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from datetime import datetime
import pytz
import random

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root_redirect():
    """
    Redirects the root URL to the static index.html page.

    Returns:

        RedirectResponse: A response object that redirects the client to the /static/index.html page.
    """
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

@app.get("/tictactoe")
def tictactoe_redirect():
    """
    Redirects to the Tic Tac Toe game UI.

    This function is responsible for handling the redirection to the Tic Tac Toe game UI.
    It returns a RedirectResponse object that redirects the client to the /static/tictactoe.html page.

    Parameters:
    None

    Returns:
    RedirectResponse: A response object that redirects the client to the /static/tictactoe.html page.
    """
    return RedirectResponse(url="/static/tictactoe.html")


# Calculator route
@app.get("/calculator")
def calculator_redirect():
    """
    Redirects to the Calculator UI.

    This function is responsible for handling the redirection to the Calculator UI.
    It returns a RedirectResponse object that redirects the client to the /static/calculator.html page.

    Parameters:
    None

    Returns:
    RedirectResponse: A response object that redirects the client to the /static/calculator.html page.
    """
    return RedirectResponse(url="/static/calculator.html")

# Generate boilerplate route for calculator functions using the provided functions in calcfunc.py
@app.get("/calculator/{operation}/{a1}/{a2}")
def calculator_operation(operation: str, a1: int, a2: int):
    """
    Performs a basic arithmetic operation on two numbers.

    Args:
        operation (str): The arithmetic operation to perform. Supported operations include: add, subtract, multiply, division.
        a1 (int): The first number to use in the operation.
        a2 (int): The second number to use in the operation.

    Returns:
        int: The result of the arithmetic operation.
    """
    from calcfunc import add, sub, mul, div

    if operation == "add":
        return add(a1, a2)
    elif operation == "sub":
        return sub(a1, a2)
    elif operation == "mul":
        return mul(a1, a2)
    elif operation == "div":
        if a2 == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
        return div(a1, a2)
    else:
        raise HTTPException(status_code=400, detail="Invalid operation.")



@app.get("/rps/{player_choice}")
def rock_paper_scissors(player_choice: str):
    """
    Plays a game of rock, paper, scissors against the computer.

    Args:
        player_choice (str): The player's choice (rock, paper, or scissors).

    Returns:
        dict: A dictionary containing the player's choice, the computer's choice, and the result of the game.
    """
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    if player_choice not in choices:
        raise HTTPException(status_code=400, detail="Invalid choice. Choose rock, paper, or scissors.")

    result = ""
    if player_choice == computer_choice:
        result = "It's a draw!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "You lose!"

    return {"player_choice": player_choice, "computer_choice": computer_choice, "result": result}

@app.get("/rps")
def rps_redirect():
    """
    Redirects to the Rock Paper Scissors game UI.
    """
    return RedirectResponse(url="/static/rps.html")

# generate a boilerplate for a soccer API
@app.get("/soccer/{team}")
def get_team_info(team: str):
    """
    Endpoint to retrieve information about a soccer team.

    Args:
        team (str): The name of the team for which information is being retrieved.

    Returns:
        dict: A dictionary containing detailed information about the team, including players, coach, stadium, and attendance.
    """
    # Define a dictionary containing the team information.
    # This dictionary includes the team name, a list of players with their respective positions and goals, 
    # the coach's name, the stadium name, and the average attendance.
    team_data = {
        "team": team,
        "players": [
            # List of players with their roles and goals scored
            {"name": "Player 1", "position": "Forward", "goals": 3},
            {"name": "Player 2", "position": "Midfielder", "goals": 2},
            {"name": "Player 3", "position": "Defender", "goals": 1}
        ],
        # Name of the team's coach
        "coach": "Coach Name",
        # Name of the stadium where the team plays
        "stadium": "Stadium Name",
        # Average attendance for the team's games
        "attendance": 10000
    }
    # Return the team data dictionary as the response
    return team_data



# Generate boilerplate for a football scores API, given a team name, csv file with scores is provided from a link, use pd.read_csv to read the csv file and return the scores for the team.
@app.get("/football/scores/{team}")
def get_football_scores(team: str):
    """
    Retrieves the football scores for a given team.
    Args:
        team (str): The name of the team.
    Returns:
        dict: A dictionary containing the team's scores.
    """
    import pandas as pd
    # URL to the CSV file containing football scores
    csv_url = "https://raw.githubusercontent.com/footballcsv/england/refs/heads/master/2010s/2015-16/eng.1.csv"
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_url)
        """
        
        Filter the DataFrame for the specified team.
        The DataFrame is expected to have columns like Round,Date,Team 1,FT,Team 2
        """
        team_scores = df[(df['Team 1'].str.lower() == team.lower()) | (df['Team 2'].str.lower() == team.lower())]
        # Check if the team has any scores 
        # If not, raise a 404 HTTPException with an appropriate message. 
        
        # Convert the DataFrame to a dictionary
        scores = team_scores.to_dict(orient='records')

        return {"team": team, "scores": scores} 

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/rs/{string}")
def reverse_string(string: str):
    """
    Returns the reverse of the given string.
    
    This function takes a string as an argument and returns a new string that is the reverse of the input string.
    
    For example, if the input string is "hello", the returned string will be "olleh".
    
    The function does not modify the input string in any way, it simply returns a new string that is the reverse of the input string.
    """
    # Get the input string
    input_str = string
    
    # Reverse the string
    reversed_str = input_str[::-1]
    
    # Return the reversed string
    return reversed_str
