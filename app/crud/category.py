
from sqlalchemy.orm import Session
from unicodedata import category

from app.models.category import Category
from app.schemas.category import CategoryCreate

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(**category.dict())  # Create Category instance from Pydantic model
    db.add(db_category)  # Add it to the session
    db.commit()  # Commit to save it in the DB
    db.refresh(db_category)  # Refresh to get the updated info (like generated id)
    return db_category

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Category).offset(skip).limit(limit).all()  # Fetch categories from DB
