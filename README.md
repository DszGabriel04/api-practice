# FastAPI City Time API

A simple, container-ready FastAPI application that provides the current local time for major cities around the world. Includes a static file server (for a front-end or documentation) and a single REST endpoint.

## Features

- **City Time API**: Returns the current local time for a list of supported global cities.
- **Static File Hosting**: Serves static files (such as HTML, CSS, JS) from the `/static` directory.
- **FastAPI**: Modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **Ready for Deployment**: All dependencies are listed in `requirements.txt` for easy installation.

## Endpoints

### `GET /`
Redirects to `/static/index.html`. Use this to serve a homepage or documentation.

### `GET /time/{city}`
Returns the current local time for the specified city.

**Path Parameters:**
- `city` (str): Name of the city. Supported cities:
  - new_york, london, paris, tokyo, sydney, los_angeles, chicago, berlin, mumbai, beijing, moscow, cape_town, dubai, singapore, rio

**Example request:**
```
GET /time/london
```

**Example response:**
```json
{
  "city": "london",
  "time": "2025-06-04 04:29:00",
  "timezone": "Europe/London"
}
```

**Error response:**
- If the city is not supported, returns HTTP 404.

## Setup & Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/DszGabriel04/api-practice.git
   cd api-practice
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```sh
   uvicorn main:app --reload
   ```
   By default, the API will be available at `http://127.0.0.1:8000/`.

## Directory Structure

```
.
├── main.py               # Main FastAPI application
├── requirements.txt      # Python dependencies
├── static/               # Static files (HTML, CSS, JS, etc.)
├── .gitignore
└── README.md
```

## Dependencies

Key dependencies from `requirements.txt`:
- `fastapi`
- `uvicorn`
- `pytz`
- Plus various others for data science, notebook, and server utilities.

To see the full list, check `requirements.txt`.

## Contributing

Pull requests and issues are welcome! Please open an issue or PR if you find bugs or want to add features.

## License

This project is provided for educational and demonstration purposes. Please add a license if you intend to use it in production.

---

**Author:** [DszGabriel04](https://github.com/DszGabriel04)
