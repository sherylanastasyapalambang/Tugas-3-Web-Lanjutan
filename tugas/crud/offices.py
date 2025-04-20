from sqlalchemy.orm import Session
from models.offices import Office
from schemas.offices import OfficeCreate

def get_all(db: Session):
    return db.query(Office).all()

def get_one(db: Session, office_code: str):
    return db.query(Office).filter(Office.officeCode == office_code).first()

def create(db: Session, data: OfficeCreate):
    new_office = Office(**data.dict())
    db.add(new_office)
    db.commit()
    db.refresh(new_office)
    return new_office

def update(db: Session, officeCode: str, office: OfficeCreate):
    db_office = db.query(Office).filter(Office.officeCode == officeCode).first()
    if db_office:
        for key, value in office.dict().items():
            setattr(db_office, key, value)
        db.commit()
        db.refresh(db_office)
    return db_office

def delete(db: Session, office_code: str):
    office = db.query(Office).filter(Office.officeCode == office_code).first()
    if office:
        db.delete(office)
        db.commit()
        return True
    return False
