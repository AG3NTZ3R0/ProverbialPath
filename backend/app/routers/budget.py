"""
Budgets Router
"""
from fastapi import APIRouter, HTTPException
import pymongo

router = APIRouter()


def get_collection(db_name: str, collection_name: str) -> pymongo.collection.Collection:
    """
    Get a collection from the database
    :param db_name: The name of the database
    :param collection_name: The name of the collection
    :return: The collection
    """
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    collection = db[collection_name]
    return collection


# Path: /budgets
@router.get("/budgets")
def get_budgets():
    """
    Get all budgets
    :return: A list of budgets
    """
    collection = get_collection("proverbial-path", "budgets")
    budgets = collection.find({})
    budgets_list = list(budgets)

    if len(budgets_list) == 0:
        raise HTTPException(status_code=404, detail="Budgets not found")
    return budgets_list


# Path: /budgets/{budget_id}
@router.get("/budgets/{budget_id}")
def get_budget(budget_id: str):
    """
    Get a budget by id
    :param budget_id: The id of the budget
    :return: The budget
    """
    collection = get_collection("proverbial-path", "budgets")
    budget = collection.find_one({"_id": budget_id})
    if budget is None:
        raise HTTPException(status_code=404, detail="Budget not found")
    return budget


# Path: /budgets/{budget_id}
@router.put("/budgets/{budget_id}")
def put_budget(budget_id: str):
    """
    Create a budget
    :param budget_id: The id of the budget
    :return: A message and the id of the budget
    """
    collection = get_collection("proverbial-path", "budgets")
    result = collection.insert_one({"_id": budget_id})
    return {"message": "Budget created", "id": result.inserted_id}
