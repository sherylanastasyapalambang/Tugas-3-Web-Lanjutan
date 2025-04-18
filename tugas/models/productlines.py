from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from database import Base

class ProductLines(Base):
    __tablename__ = "productlines"
    
    productLine = Column(String(50), primary_key=True, index=True)  # Primary key for product lines
    textDescription = Column(String(4000))
    htmlDescription = Column(String(4000))
    image = Column(String(255))

    # Correct relationship definition, use string reference to avoid circular dependency issues
    products = relationship("Product", back_populates="productLine_rel")
