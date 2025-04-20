from sqlalchemy.orm import Session
from models.productlines import ProductLines  # Sesuaikan dengan nama kelas yang benar
from schemas.productlines import ProductLineCreate

# Get all ProductLines
def get_all(db: Session):
    return db.query(ProductLines).all()

# Get one ProductLine by productLine (primary key)
def get_one(db: Session, line_id: str):
    return db.query(ProductLines).filter(ProductLines.productLine == line_id).first()

# Create a new ProductLine
def create(db: Session, line_id: str, data: ProductLineCreate):
    db_line = ProductLines(productLine=line_id, **data.dict())
    db.add(db_line)
    db.commit()
    db.refresh(db_line)
    return db_line

# Update an existing ProductLine
def update(db: Session, line_id: str, data: ProductLineCreate):
    db_line = get_one(db, line_id)
    if not db_line:
        return None
    for key, value in data.dict().items():
        setattr(db_line, key, value)
    db.commit()
    db.refresh(db_line)
    return db_line

# Delete a ProductLine
def delete(db: Session, line_id: str):
    obj = get_one(db, line_id)
    if obj:
        db.delete(obj)
        db.commit()
    return obj
