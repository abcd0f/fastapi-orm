# app/main.py
from fastapi import FastAPI
from app.models.user import SQLModel
from app.db.session import engine
from app.api import user

app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.include_router(user.router, prefix="/users", tags=["Users"])
