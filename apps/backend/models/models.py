from sqlalchemy import Column, Integer, String, Boolean, Text
from .database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(50), unique=True, index=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50), default="User")
    note = Column(Text, nullable=True)
    active = Column(Boolean, default=True)
