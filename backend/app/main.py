"""
Main Application File
"""
from fastapi import FastAPI
from routers import budget, root

app = FastAPI()

app.include_router(root.router)
app.include_router(budget.router)
