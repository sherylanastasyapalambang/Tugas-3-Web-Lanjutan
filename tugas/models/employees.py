from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    employeeNumber = Column(Integer, primary_key=True, index=True)
    lastName = Column(String(50))
    firstName = Column(String(50))
    extension = Column(String(10))
    email = Column(String(100))
    officeCode = Column(String(10), ForeignKey("offices.officeCode"))
    reportsTo = Column(Integer, ForeignKey("employees.employeeNumber"), nullable=True)
    jobTitle = Column(String(50))

    # Relasi ke office
    office = relationship("Office", back_populates="employees")

    # Relasi self-referencing: siapa yang menjadi bos (atasan)
    manager = relationship("Employee", remote_side=[employeeNumber], backref=backref("subordinates", lazy="joined"))
