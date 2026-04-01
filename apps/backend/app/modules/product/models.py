from sqlalchemy import Column, Integer, String, Float, Boolean, Text
from app.db.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, default=0)
    quantity = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
