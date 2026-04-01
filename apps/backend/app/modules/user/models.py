from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum
from app.db.base import Base


class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True, nullable=False)
    description = Column(String(255), nullable=True)

    users = relationship("User", back_populates="role")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)

    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    role = relationship("Role", back_populates="users")

    refresh_tokens = relationship(
        "app.modules.auth.models.RefreshToken",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    @property
    def is_superuser(self) -> bool:
        return self.role.name == UserRole.ADMIN if self.role else False
