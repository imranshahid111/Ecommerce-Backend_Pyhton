# routes/category.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud
from app.schemas.category import Category, CategoryCreate
from app.database import get_db
from app.routes.protected import get_current_user

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=Category)
def create_category_route(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return crud.create_category(db, category)


@router.get("/", response_model=list[Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_categories(db, skip, limit)  # Call get_categories from crud
