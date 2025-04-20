from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Order(Base):
    __tablename__ = "orders"

    orderNumber = Column(Integer, primary_key=True, index=True, autoincrement=True)
    orderDate = Column(Date)
    requiredDate = Column(Date)
    shippedDate = Column(Date, nullable=True)
    status = Column(String(15))
    comments = Column(String(255), nullable=True)
    customerNumber = Column(Integer, ForeignKey("customers.customerNumber"))

    customer = relationship("Customer", back_populates="orders")
    orderdetails = relationship("OrderDetail", back_populates="order", cascade="all, delete-orphan")
