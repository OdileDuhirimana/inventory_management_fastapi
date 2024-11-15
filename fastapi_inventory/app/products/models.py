# models/product.py
from sqlalchemy import Column, Integer, String, Text, Boolean, DECIMAL
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    sku = Column(String(100), unique=True, nullable=False)
    stock_level = Column(Integer, nullable=False)
    reorder_level = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    low_stock_alert = Column(Boolean, default=False)
    
    orders = relationship("Order", back_populates="product")
    
    def __str__(self):
        return self.name
    
    def needs_reorder(self):
        return self.stock_level <= self.reorder_level
    
    def save(self, session):
        self.low_stock_alert = self.needs_reorder()
        session.add(self)
        session.commit()
