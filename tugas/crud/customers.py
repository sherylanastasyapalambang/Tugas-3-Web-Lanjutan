from sqlalchemy.orm import Session
from models.customers import Customer
from schemas.customers import CustomerCreate

def get_all(db: Session):
    return db.query(Customer).all()

def get_one(db: Session, customerNumber: int):
    return db.query(Customer).filter(Customer.customerNumber == customerNumber).first()

def create(db: Session, customerNumber: int, data: CustomerCreate):
    new_customer = Customer(customerNumber=customerNumber, **data.dict())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

def delete(db: Session, customerNumber: int):
    customer = get_one(db, customerNumber)
    if customer:
        db.delete(customer)
        db.commit()
        return True
    return False
