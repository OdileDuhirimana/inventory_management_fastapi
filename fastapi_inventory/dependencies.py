from fastapi import Depends
from .database import get_db
from sqlalchemy.orm import Session

def get_database(db: Session = Depends(get_db)):
    return db