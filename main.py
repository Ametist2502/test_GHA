# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Worlddddddddddddd"}


@app.get("/login")
def login():
    return None