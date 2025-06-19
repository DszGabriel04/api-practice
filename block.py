from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Create a FastAPI app instance
app = FastAPI(
    title="My FastAPI Boilerplate",
    description="A basic boilerplate for creating FastAPI applications.",
    version="0.1.0",
)

# --- Pydantic Models ---
# Pydantic models are used for request and response validation and serialization.

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tags: List[str] = []

# --- API Endpoints ---

@app.get("/")
async def read_root():
    """
    Root GET endpoint.
    Returns a welcome message.
    """
    


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    """
    GET endpoint to retrieve an item by its ID.
    Includes an optional query parameter 'q'.
    """
    return {"item_id": item_id, "q": q, "description": f"Details for item {item_id}"}


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    """
    POST endpoint to create a new item.
    It uses the Pydantic Item model for request body validation.
    """
    # In a real application, you would save the item to a database here.
    print(f"Received item: {item.dict()}")
    return item

# To run this application:
# 1. Save this file as main.py (or any other name).
# 2. Install FastAPI and Uvicorn: pip install fastapi uvicorn
# 3. Run the server: uvicorn main:app --reload
#
# Then, open your browser at http://127.0.0.1:8000/docs to see the interactive API documentation.
