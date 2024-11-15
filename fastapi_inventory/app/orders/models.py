# models/order.py
from sqlalchemy import Column, ForeignKey, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.types import String
from database import Base
from ..products.models import Product
from ..users.models import CustomUser

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    is_approved = Column(Boolean, default=False)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    
    user = relationship("CustomUser", back_populates="orders")
    product = relationship("Product", back_populates="orders")
    
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
