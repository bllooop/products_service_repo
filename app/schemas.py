from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: int
    shopid: int

class CreateProduct(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

