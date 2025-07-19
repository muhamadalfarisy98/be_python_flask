from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.product import ProductCreate, ProductUpdate, ProductResponse
from services import products as service

router = APIRouter()

@router.get("/products", response_model=list[ProductResponse])
def read_products(db: Session = Depends(get_db)):
    return service.get_all(db)

@router.get("/products/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = service.get_by_id(db, product_id)
    if not product:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product

@router.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return service.create(db, product)

@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    result = service.update(db, product_id, product)
    if not result:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Product not found")
    return result

@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    result = service.delete(db, product_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return result
