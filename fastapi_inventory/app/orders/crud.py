# app/orders/crud.py
from sqlalchemy.orm import Session
from app.orders import models, schemas

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(
        quantity=order.quantity,
        user_id=order.user_id,
        product_id=order.product_id,
        is_approved=order.is_approved,
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def get_orders_by_user(db: Session, user_id: int):
    return db.query(models.Order).filter(models.Order.user_id == user_id).all()

def update_order(db: Session, order_id: int, order_update: schemas.OrderUpdate):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if db_order:
        db_order.is_approved = order_update.is_approved
        db.commit()
        db.refresh(db_order)
    return db_order
