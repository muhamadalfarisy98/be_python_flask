from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)

    model_config = ConfigDict(from_attributes=True, extra="forbid")

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1)
    price: Optional[float] = Field(None, gt=0)
    quantity: Optional[int] = Field(None, ge=0)

    model_config = ConfigDict(from_attributes=True, extra="forbid")

class ProductResponse(ProductCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
