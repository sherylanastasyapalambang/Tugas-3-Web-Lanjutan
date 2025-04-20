from pydantic import BaseModel

class OrderDetailBase(BaseModel):
    productCode: str    
    quantityOrdered: int
    priceEach: float
    orderLineNumber: int

class OrderDetailCreate(OrderDetailBase):
    orderNumber: int
    productCode: str

class OrderDetailUpdate(OrderDetailBase):
    pass  # Primary key tidak diubah saat update

class OrderDetail(OrderDetailCreate):
    class Config:
        orm_mode = True
