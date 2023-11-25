from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()


# Path: /
@app.get("/")
def root():
    return {"message": "Hello World"}
