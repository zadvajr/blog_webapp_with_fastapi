"""
Docstring for backend.main
"""
from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

@app.get("/")
def hello():
    """
    Docstring for hello
    """
    return {"msg": "Helllo FastAPI 🚀"}
