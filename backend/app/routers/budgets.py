"""
Budgets Router
"""
from fastapi import APIRouter
from pymongo import MongoClient

router = APIRouter()


# Path: /budgets
@router.get("/budgets")
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
@router.get("/budgets/{budget_id}")
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
@router.put("/budgets/{budget_id}")
def put_budget(budget_id: str):
    """
    Create a budget
    :param budget_id: The id of the budget
    :return:
    """
    client = MongoClient("mongodb://localhost:27017/")
    db = client["proverbial-path"]
    collection = db["budgets"]
    result = collection.insert_one({"_id": budget_id})
    return {"message": "Budget created", "id": result.inserted_id}
