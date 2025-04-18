from pydantic import BaseModel
from typing import Optional, List

class EmployeeBase(BaseModel):
    lastName: str
    firstName: str
    extension: str
    email: str
    officeCode: str
    reportsTo: Optional[int] = None
    jobTitle: str

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    employeeNumber: int

    class Config:
        from_attributes = True
