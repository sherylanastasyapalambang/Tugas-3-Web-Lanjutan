from sqlalchemy.orm import Session
from models.customers import Customer
from schemas.customers import CustomerCreate

def get_all(db: Session):
    return db.query(Customer).all()

def get_one(db: Session, customerNumber: int):
    return db.query(Customer).filter(Customer.customerNumber == customerNumber).first()

def create(db: Session, data: CustomerCreate):
    new_customer = Customer(**data.dict())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

def update(db: Session, customerNumber: int, data: CustomerCreate):
    customer = get_one(db, customerNumber)
    if customer:
        for key, value in data.dict().items():
            setattr(customer, key, value)
        db.commit()
        db.refresh(customer)
        return customer
    return None

def delete(db: Session, customerNumber: int):
    customer = get_one(db, customerNumber)
    if customer:
        db.delete(customer)
        db.commit()
        return True
    return False
