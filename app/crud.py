from sqlalchemy.orm import Session

from . import models, schemas


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_products_by_id(db: Session, id: int, ):
    return db.query(models.Product).filter(models.Product.id == id).first()

