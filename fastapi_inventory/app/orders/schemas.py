# app/orders/schemas.py
from pydantic import BaseModel
from typing import Optional

class OrderBase(BaseModel):
    quantity: int
    is_approved: Optional[bool] = False
    user_id: int
    product_id: int

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    is_approved: bool

class Order(OrderBase):
    id: int
    created_at: str
    updated_at: Optional[str] = None

    class Config:
        orm_mode = True
