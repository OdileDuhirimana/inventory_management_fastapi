# app/products/crud.py
from sqlalchemy.orm import Session
from app.products import models, schemas

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        name=product.name,
        description=product.description,
        sku=product.sku,
        stock_level=product.stock_level,
        reorder_level=product.reorder_level,
        price=product.price
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def update_product(db: Session, product_id: int, product_update: schemas.ProductUpdate):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        db_product.name = product_update.name or db_product.name
        db_product.description = product_update.description or db_product.description
        db_product.sku = product_update.sku or db_product.sku
        db_product.price = product_update.price or db_product.price
        db_product.stock_level = product_update.stock_level or db_product.stock_level
        db_product.reorder_level = product_update.reorder_level or db_product.reorder_level
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product
