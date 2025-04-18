from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = "products"

    productCode = Column(String(15), primary_key=True, index=True)
    productName = Column(String(70))
    productLine = Column(String(50), ForeignKey("productlines.productLine"))  # ForeignKey to ProductLine

    # Use string references for relationships to ensure SQLAlchemy resolves it after class definitions
    productLine_rel = relationship("ProductLines", back_populates="products")
