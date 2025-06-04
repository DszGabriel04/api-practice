# API Practice

A simple FastAPI-based project for practicing and demonstrating the development of RESTful APIs in Python. This project provides endpoints for retrieving the current time in major cities, redirects for static web apps (like Tic-Tac-Toe or a calculator), and simple math utility functions.

## Features

- **Current Time API**: Get the current local time for a variety of major global cities by name.
- **Tic-Tac-Toe & Calculator Redirects**: Redirects to static HTML pages hosting a Tic-Tac-Toe game and a calculator.
- **Math Utilities**: Includes a module (`calcfunc.py`) with functions for basic arithmetic operations (addition, subtraction, multiplication, division) with input validation.
- **Static File Serving**: Serves static files (e.g., HTML, CSS, JS) from a `static` directory.
- **Testing**: Contains a `tests` directory for future test cases.

## Endpoints

| Method | Path                | Description                                    |
|--------|---------------------|------------------------------------------------|
| GET    | `/`                 | Redirects to `/static/index.html`              |
| GET    | `/time/{city}`      | Returns local time for supported city          |
| GET    | `/tictactoe`        | Redirects to `/static/tictactoe.html`          |
| GET    | `/calculator`       | Redirects to `/static/calculator.html`         |

### Supported Cities for `/time/{city}`

- new_york, london, paris, tokyo, sydney, los_angeles, chicago, berlin, mumbai, beijing, moscow, cape_town, dubai, singapore, rio

## Example Usage

**Get the current time in Tokyo:**
```
GET /time/tokyo
```
_Response:_
```json
{
  "city": "tokyo",
  "time": "2025-06-04 16:33:19",
  "timezone": "Asia/Tokyo"
}
```

## Quick Start

### Requirements

- Python 3.8+
- (See `requirements.txt` for a full list of dependencies)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/DszGabriel04/api-practice.git
    cd api-practice
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    uvicorn main:app --reload
    ```

4. Open your browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the static index page or try out the API endpoints.

## File Structure

```
.
├── main.py             # FastAPI application with endpoints
├── calcfunc.py         # Utility functions for basic arithmetic
├── requirements.txt    # Python dependencies
├── static/             # Static files (HTML, CSS, JS)
├── tests/              # Tests (to be implemented)
└── README.md           # Project documentation
```

## Math Utility Functions (`calcfunc.py`)

- `add(a1: int, a2: int)` — Addition
- `sub(a1: int, a2: int)` — Subtraction
- `mul(a1: int, a2: int)` — Multiplication
- `div(a1: int, a2: int)` — Division (raises error on divide by zero)

All math functions validate that their inputs are integers and raise `TypeError` otherwise.

## Contributing

Pull requests and issues are welcome! Please open an issue to discuss your ideas or report bugs.

## License

This project is provided for educational purposes and does not have a specific license. If you wish to reuse or extend, please contact the repository author.

---

**Author:** [DszGabriel04](https://github.com/DszGabriel04)
