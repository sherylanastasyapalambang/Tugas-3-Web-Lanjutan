from pydantic import BaseModel
from typing import Optional

class OfficeBase(BaseModel):
    city: str
    phone: str
    addressLine1: str
    addressLine2: Optional[str] = None
    state: Optional[str] = None
    country: str
    postalCode: str
    territory: str

class OfficeCreate(OfficeBase):
    officeCode: str

class Office(OfficeBase):
    officeCode: str

    class Config:
        orm_mode = True
