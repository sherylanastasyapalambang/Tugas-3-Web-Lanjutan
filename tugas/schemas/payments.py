from pydantic import BaseModel
from datetime import date

class PaymentBase(BaseModel):
    paymentDate: date
    amount: float

class PaymentCreate(PaymentBase):
    customerNumber: int
    checkNumber: str

class Payment(PaymentCreate):
    class Config:
        from_attributes = True
