from sqlalchemy import Column, String, Numeric, Date, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Payment(Base):
    __tablename__ = "payments"

    customerNumber = Column(Integer, ForeignKey("customers.customerNumber"), primary_key=True)
    checkNumber = Column(String(50), primary_key=True)
    paymentDate = Column(Date)
    amount = Column(Numeric(10, 2))

    customer = relationship("Customer", back_populates="payments")
