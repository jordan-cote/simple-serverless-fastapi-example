from typing import Optional
from fastapi import FastAPI
from .database import engine
from mangum import Mangum

from .api.api import router as api_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/heartbeat")
def test_database():
    connection = ""
    try:
        engine.connect()
        connection = "successful connection to database"
    except:
        connection = "failure when trying to connecting to database"
    return {"heartbeat": connection}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


app.include_router(api_router, prefix="/api")
handler = Mangum(app)
