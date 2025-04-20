from sqlalchemy import Column, Integer, Float, ForeignKey, PrimaryKeyConstraint, String
from sqlalchemy.orm import relationship
from database import Base

class OrderDetail(Base):
    __tablename__ = "orderdetails"

    orderNumber = Column(Integer, ForeignKey("orders.orderNumber"))
    productCode = Column(String(15), ForeignKey("products.productCode"))
    quantityOrdered = Column(Integer)
    priceEach = Column(Float)
    orderLineNumber = Column(Integer)

    __table_args__ = (
        PrimaryKeyConstraint('orderNumber', 'productCode'),
    )

    product = relationship("Product", back_populates="orderdetails")
    order = relationship("Order", back_populates="orderdetails")
