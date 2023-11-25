"""
Root Router
"""
from fastapi import APIRouter

router = APIRouter()


# Path: /
@router.get("/")
def root():
    """
    Heartbeat
    :return:
    """
    return {"message": "Hello World"}
