from sqlalchemy.orm import Session
from schemas.product import ProductCreate, ProductUpdate
from repositories import products as repo

def get_all(db: Session):
    return repo.get_all(db)

def get_by_id(db: Session, product_id: int):
    return repo.get_by_id(db, product_id)

def create(db: Session, product: ProductCreate):
    return repo.create(db, product)

def update(db: Session, product_id: int, product: ProductUpdate):
    return repo.update(db, product_id, product)

def delete(db: Session, product_id: int):
    return repo.delete(db, product_id)
