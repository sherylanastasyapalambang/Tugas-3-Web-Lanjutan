from pydantic import BaseModel
from typing import Optional

class EmployeeBase(BaseModel):
    lastName: str
    firstName: str
    extension: str
    email: str
    officeCode: str
    reportsTo: Optional[int]
    jobTitle: str

class EmployeeCreate(EmployeeBase):
    employeeNumber: int

class Employee(EmployeeBase):
    employeeNumber: int

    class Config:
        orm_mode = True
