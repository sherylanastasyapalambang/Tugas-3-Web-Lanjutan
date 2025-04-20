from sqlalchemy.orm import Session
from models.orders import Order
from schemas.orders import OrderCreate, OrderUpdate

def get_all_orders(db: Session):
    return db.query(Order).all()

def get_order(db: Session, orderNumber: int):
    return db.query(Order).filter(Order.orderNumber == orderNumber).first()

def create_order(db: Session, order: OrderCreate):
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def update_order(db: Session, orderNumber: int, updated: OrderUpdate):
    db_order = get_order(db, orderNumber)
    if db_order:
        for key, value in updated.dict(exclude_unset=True).items():
            setattr(db_order, key, value)
        db.commit()
        db.refresh(db_order)
    return db_order

def delete_order(db: Session, orderNumber: int):
    db_order = get_order(db, orderNumber)
    if db_order:
        db.delete(db_order)
        db.commit()
    return db_order
