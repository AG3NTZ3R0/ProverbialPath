"""
Budgets Router
"""
from fastapi import APIRouter
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
    :return:
    """
    collection = get_collection("proverbial-path", "budgets")
    budgets = collection.find({})
    return list(budgets)


# Path: /budgets/{budget_id}
@router.get("/budgets/{budget_id}")
def get_budget(budget_id: str):
    """
    Get a budget by id
    :param budget_id: The id of the budget
    :return:
    """
    collection = get_collection("proverbial-path", "budgets")
    budget = collection.find_one({"_id": budget_id})
    return budget


# Path: /budgets/{budget_id}
@router.put("/budgets/{budget_id}")
def put_budget(budget_id: str):
    """
    Create a budget
    :param budget_id: The id of the budget
    :return:
    """
    collection = get_collection("proverbial-path", "budgets")
    result = collection.insert_one({"_id": budget_id})
    return {"message": "Budget created", "id": result.inserted_id}
