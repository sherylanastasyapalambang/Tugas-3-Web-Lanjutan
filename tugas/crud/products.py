from sqlalchemy.orm import Session
from models.products import Product
from schemas.products import ProductCreate, ProductUpdate

def get_all_products(db: Session):
    return db.query(Product).all()

def get_product_by_code(db: Session, productCode: str):
    return db.query(Product).filter(Product.productCode == productCode).first()


def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, productCode: str, product: ProductUpdate):
    db_product = db.query(Product).filter(Product.productCode == productCode).first()
    if db_product:
        for key, value in product.dict().items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, productCode: str):
    db_product = db.query(Product).filter(Product.productCode == productCode).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product
