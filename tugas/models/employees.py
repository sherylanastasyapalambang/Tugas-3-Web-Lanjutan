from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Employee(Base):
    __tablename__ = "employees"

    employeeNumber = Column(Integer, primary_key=True, index=True)
    lastName = Column(String(50), nullable=False)
    firstName = Column(String(50), nullable=False)
    extension = Column(String(10), nullable=False)
    email = Column(String(100), nullable=False)
    officeCode = Column(String(10), ForeignKey("offices.officeCode"), nullable=False)
    reportsTo = Column(Integer, ForeignKey("employees.employeeNumber"), nullable=True)
    jobTitle = Column(String(50), nullable=False)

    # Relasi ke atasan (self-reference)
    manager = relationship("Employee", remote_side=[employeeNumber], back_populates="subordinates")
    subordinates = relationship("Employee", back_populates="manager")

    # Relasi ke customers (jika sales rep)
    customers = relationship("Customer", back_populates="salesRep")
