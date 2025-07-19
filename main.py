from fastapi import FastAPI
from routes import products
from models.product import Base
from database import engine

app = FastAPI()
app.include_router(products.router)

Base.metadata.create_all(bind=engine)
