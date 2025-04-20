from pydantic import BaseModel

class ProductBase(BaseModel):
    productName: str
    productLine: str
    productScale: str
    productVendor: str
    productDescription: str
    quantityInStock: int
    buyPrice: float
    MSRP: float

class ProductCreate(ProductBase):
    productCode: str  # Required saat create

class ProductUpdate(ProductBase):
    pass  # productCode tidak perlu diupdate

class ProductSimple(ProductCreate):
    class Config:
        orm_mode = True

class Product(ProductSimple):
    class Config:
        orm_mode = True
