from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
def read_root():
    return {"Categoria": "Comedia"}


@app.get("/items/{item_id}")
def read_item(item_id: string, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}