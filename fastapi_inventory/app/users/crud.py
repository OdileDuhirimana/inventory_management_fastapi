# app/users/crud.py
from sqlalchemy.orm import Session
from app.users import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.CustomUser(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password,
        bio=user.bio
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.CustomUser).filter(models.CustomUser.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.CustomUser).filter(models.CustomUser.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CustomUser).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    db_user = db.query(models.CustomUser).filter(models.CustomUser.id == user_id).first()
    if db_user:
        db_user.username = user_update.username or db_user.username
        db_user.email = user_update.email or db_user.email
        db_user.full_name = user_update.full_name or db_user.full_name
        db_user.bio = user_update.bio or db_user.bio
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.CustomUser).filter(models.CustomUser.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
