from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base

engine = create_engine('sqlite:///database.db' )

session = sessionmaker(bind=engine , autocommit=False, autoflush=False)

Base.metadata.create_all(engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

