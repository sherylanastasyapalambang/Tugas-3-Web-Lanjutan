from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    productName: str
    productLine: str
    productScale: str
    productVendor: str
    productDescription: Optional[str]
    quantityInStock: int
    buyPrice: float
    msrp: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    productCode: str
    class Config:
        from_attributes = True
