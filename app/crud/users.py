from sqlalchemy.orm import Session
from app.models.users import Users
from app.schemas.users import UserCreate
from passlib.context import CryptContext

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ✅ Create new user with hashed password
def create_User(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    new_user = Users(username=user.username, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# ✅ Login user by verifying password
def login_User(db: Session, username: str, password: str):
    user = db.query(Users).filter(Users.username == username).first()
    if user and pwd_context.verify(password, user.password):
        return user
    return None
