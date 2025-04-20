from sqlalchemy.orm import Session
from models.orderdetails import OrderDetail
from schemas.orderdetails import OrderDetailCreate, OrderDetailUpdate

def get_all_orderdetails(db: Session):
    return db.query(OrderDetail).all()

def get_orderdetail(db: Session, orderNumber: int, productCode: str):
    return db.query(OrderDetail).filter(
        OrderDetail.orderNumber == orderNumber,
        OrderDetail.productCode == productCode
    ).first()

def create_orderdetail(db: Session, orderdetail: OrderDetailCreate):
    db_orderdetail = OrderDetail(**orderdetail.dict())
    db.add(db_orderdetail)
    db.commit()
    db.refresh(db_orderdetail)
    return db_orderdetail

def update_orderdetail(db: Session, orderNumber: int, productCode: str, updated: OrderDetailUpdate):
    db_orderdetail = get_orderdetail(db, orderNumber, productCode)
    if db_orderdetail:
        for key, value in updated.dict().items():
            setattr(db_orderdetail, key, value)
        db.commit()
        db.refresh(db_orderdetail)
    return db_orderdetail

def delete_orderdetail(db: Session, orderNumber: int, productCode: str):
    db_orderdetail = get_orderdetail(db, orderNumber, productCode)
    if db_orderdetail:
        db.delete(db_orderdetail)
        db.commit()
    return db_orderdetail
