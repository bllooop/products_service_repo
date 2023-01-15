from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import get_db
from . import crud, models, schemas
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/v1/products")
def create(details: schemas.CreateProduct, db: Session = Depends(get_db)):
    to_create = models.Product(
        name = details.name,
        price = details.price,
        shopid = details.shopid
    )
    db.add(to_create)
    db.commit()
    return {
        "success": True,
        "created_id":to_create.id
    }

@app.get("/v1/products")
async def read_products(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@app.get("/v1/products/{id}")
async def read_product_by_id(id: int, db: Session = Depends(get_db)):
    result = crud.get_products_by_id(db, id = id)
    if result is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return result

@app.get("/__health")
async def check_service():
    return



