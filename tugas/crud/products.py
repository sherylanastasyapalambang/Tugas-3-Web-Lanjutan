from sqlalchemy.orm import Session
from models.productlines import ProductLines
from schemas.productlines import ProductLineCreate

def get_all(db: Session):
    return db.query(ProductLines).all()

def get_one(db: Session, id: int):
    return db.query(ProductLines).filter(ProductLines.id == id).first()

def create(db: Session, id: int, data: ProductLineCreate):
    new_productline = ProductLines(
        id=id,
        productLine=data.productLine,
        textDescription=data.textDescription,
        htmlDescription=None,  # Sesuai permintaan: apapun input akan bernilai NULL
        image=None
    )
    db.add(new_productline)
    db.commit()
    db.refresh(new_productline)
    return new_productline

def delete(db: Session, id: int):
    productline = get_one(db, id)
    if productline:
        db.delete(productline)
        db.commit()
        return True
    return False
