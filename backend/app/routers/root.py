"""
Root Router
"""
from fastapi import APIRouter

router = APIRouter()


# Path: /
@router.get("/")
def root():
    return {"message": "Hello World"}
