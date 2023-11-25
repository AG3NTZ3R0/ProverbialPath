from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()


# Path: /
@app.get("/")
def root():
    return {"message": "Hello World"}


# Path: /budgets
@app.get("/budgets")
def get_budgets():
    """
    Get all budgets
    :return:
    """
    client = MongoClient("mongodb://localhost:27017/")
    db = client["proverbial-path"]
    collection = db["budgets"]
    budgets = collection.find({})
    return list(budgets)


# Path: /budgets/{id}
@app.get("/budgets/{id}")
def get_budget(budget_id: str):
    """
    Get a budget by id
    :param budget_id: The id of the budget
    :return:
    """
    client = MongoClient("mongodb://localhost:27017/")
    db = client["proverbial-path"]
    collection = db["budgets"]
    budget = collection.find_one({"_id": budget_id})
    return budget


# Path: /budgets/{id}
@app.put("/budgets/{id}")
def put_budget(budget_id: str):
    """
    Create a budget
    :param budget_id:
    :return:
    """
    client = MongoClient("mongodb://localhost:27017/")
    db = client["proverbial-path"]
    collection = db["budgets"]
    result = collection.insert_one({"_id": budget_id})
    return {"message": "Budget created", "id": result.inserted_id}
