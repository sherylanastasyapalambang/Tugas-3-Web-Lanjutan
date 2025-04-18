from sqlalchemy.orm import Session
from models.employees import Employee
from schemas.employees import EmployeeCreate

def get_all(db: Session):
    return db.query(Employee).all()

def get_one(db: Session, employeeNumber: int):
    return db.query(Employee).filter(Employee.employeeNumber == employeeNumber).first()

def create(db: Session, employeeNumber: int, data: EmployeeCreate):
    new_employee = Employee(employeeNumber=employeeNumber, **data.dict())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def delete(db: Session, employeeNumber: int):
    employee = get_one(db, employeeNumber)
    if employee:
        db.delete(employee)
        db.commit()
        return True
    return False
