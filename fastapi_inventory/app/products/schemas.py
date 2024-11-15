# app/products/schemas.py
from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    sku: str
    stock_level: int = 0
    reorder_level: int = 5
    price: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name: Optional[str] = None
    description: Optional[str] = None
    sku: Optional[str] = None
    stock_level: Optional[int] = None
    reorder_level: Optional[int] = None
    price: Optional[float] = None

class Product(ProductBase):
    id: int
    low_stock_alert: bool

    class Config:
        orm_mode = True
