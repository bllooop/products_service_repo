from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import get_db
from . import crud, models, schemas
from .database import engine


app = FastAPI()

@app.get("/v1/products")
async def read_products():
    return "test"



@app.get("/__health")
async def check_service():
    return



