from pydantic import BaseModel
from typing import Optional
from datetime import date

class OrderBase(BaseModel):
    orderDate: date
    requiredDate: date
    shippedDate: Optional[date]
    status: str
    comments: Optional[str] = None
    customerNumber: int

class OrderCreate(OrderBase):
    orderNumber: int

class OrderUpdate(BaseModel):
    orderDate: Optional[date]
    requiredDate: Optional[date]
    shippedDate: Optional[date]
    status: Optional[str]
    comments: Optional[str]

class Order(OrderBase):
    orderNumber: int

    class Config:
        orm_mode = True


