from pydantic import BaseModel
from typing import Optional

class CustomerBase(BaseModel):
    customerName: str
    contactLastName: str
    contactFirstName: str
    phone: str
    addressLine1: str
    addressLine2: Optional[str] = None
    city: str
    state: Optional[str] = None
    postalCode: Optional[str] = None
    country: str
    salesRepEmployeeNumber: Optional[int] = None
    creditLimit: Optional[float] = None

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    customerNumber: int

    class Config:
        from_attributes = True
