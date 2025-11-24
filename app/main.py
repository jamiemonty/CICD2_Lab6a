from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.database import engine, SessionLocal
from app.models import Base, UserDB
from app.schemas import UserCreate, UserRead

app = FastAPI(title="Service A - Greeting API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name} from Service A!"}