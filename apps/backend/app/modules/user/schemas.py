from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional


class RoleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    description: Optional[str] = None


class UserCreate(BaseModel):
    username: Optional[str] = None
    name: Optional[str] = None
    email: EmailStr
    password: Optional[str] = None
    role_id: Optional[int] = None
    role: Optional[str] = None
    isActive: Optional[bool] = None


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    role_id: Optional[int] = None


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    email: EmailStr
    is_active: bool
    is_superuser: bool
    role: RoleResponse
