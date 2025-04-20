from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from database import Base

class Product(Base):
    __tablename__ = "products"

    productCode = Column(String(15), primary_key=True, index=True)
    productName = Column(String(70))
    productLine = Column(String(50), ForeignKey("productlines.productLine"))
    productScale = Column(String(10))
    productVendor = Column(String(50))
    productDescription = Column(String)
    quantityInStock = Column(Integer)
    buyPrice = Column(Float)
    MSRP = Column(Float)

# ... kolom lainnya
    productLine_rel = relationship("ProductLines", back_populates="products")
