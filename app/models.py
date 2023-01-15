from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column

from .database import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    shopid = Column(Integer)


