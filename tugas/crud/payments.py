from sqlalchemy.orm import Session
from models.payments import Payment
from schemas.payments import PaymentCreate

def get_all(db: Session):
    return db.query(Payment).all()

def get_one(db: Session, customerNumber: int, checkNumber: str):
    return db.query(Payment).filter_by(customerNumber=customerNumber, checkNumber=checkNumber).first()

def create(db: Session, data: PaymentCreate):
    new_payment = Payment(**data.dict())
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment

def update(db: Session, customerNumber: int, checkNumber: str, data: PaymentCreate):
    payment = get_one(db, customerNumber, checkNumber)
    if payment:
        for key, value in data.dict().items():
            setattr(payment, key, value)
        db.commit()
        db.refresh(payment)
        return payment
    return None

def delete(db: Session, customerNumber: int, checkNumber: str):
    payment = get_one(db, customerNumber, checkNumber)
    if payment:
        db.delete(payment)
        db.commit()
        return True
    return False
