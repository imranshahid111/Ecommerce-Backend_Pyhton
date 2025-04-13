from fastapi import FastAPI
from sqlalchemy.sql.functions import user

from app.routes import category , product , users  # Import your routers here
from app.database import engine
from app.models import base

# Create all tables in the database
base.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce API",
    description="Backend for E-Commerce App with Admin Panel",
    version="1.0.0"
)

# Include routers
app.include_router(category.router)
app.include_router(users.router)
app.include_router(product.router)

@app.get("/")
def root():
    return {"message": "Ecommerce Backend in Python"}# Optionally: serve static files (e.g. product images)
# from fastapi.staticfiles import StaticFiles
# app.mount("/static", StaticFiles(directory="static"), name="static")
