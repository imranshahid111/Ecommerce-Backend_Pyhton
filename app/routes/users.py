from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.users import UserResponse , UserCreate
from app.database import get_db
from app.crud.users import create_User , login_User
from app.models.users import Users
from fastapi.responses import JSONResponse
from app.auth.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Users"])

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(Users).filter(Users.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="UserName already registered")
    return create_User(db, user)



@router.post("/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = login_User(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


