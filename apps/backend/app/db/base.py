from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, declared_attr
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_recycle=3600,
    pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
