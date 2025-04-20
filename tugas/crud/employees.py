from sqlalchemy.orm import Session
from models.employees import Employee
from schemas.employees import EmployeeCreate

def get_all(db: Session):
    return db.query(Employee).all()

def get_one(db: Session, id: int):
    return db.query(Employee).filter(Employee.employeeNumber == id).first()

def create(db: Session, id: int, data: EmployeeCreate):
    new_employee = Employee(**data.dict())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def update(db: Session, employeeNumber: int, employee: EmployeeCreate):
    db_employee = db.query(Employee).filter(employee.employeeNumber == employeeNumber).first()
    if db_employee:
        for key, value in employee.dict().items():
            setattr(db_employee, key, value)
        db.commit()
        db.refresh(db_employee)
    return db_employee

def delete(db: Session, id: int):
    employee = db.query(Employee).filter(Employee.employeeNumber == id).first()
    if employee:
        db.delete(employee)
        db.commit()
        return True
    return False
