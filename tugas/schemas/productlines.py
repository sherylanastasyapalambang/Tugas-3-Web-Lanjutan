from pydantic import BaseModel
from typing import Optional

# Base schema for ProductLine
class ProductLineBase(BaseModel):
    textDescription: Optional[str] = None
    htmlDescription: Optional[str] = None
    image: Optional[str] = None

# Schema for creating a ProductLine
class ProductLineCreate(ProductLineBase):
    pass

# Schema for ProductLine response
class ProductLine(ProductLineBase):
    productLine: str  # primary key, as productLine is the unique identifier
    
    class Config:
        orm_mode = True  # this helps to serialize SQLAlchemy models into Pydantic models
