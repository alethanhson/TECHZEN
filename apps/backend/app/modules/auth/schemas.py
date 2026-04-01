from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional
from app.modules.user.schemas import UserResponse


class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    role_id: int = 2  # Default: User role


class TokenResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: Optional[UserResponse] = None


class TokenRefreshRequest(BaseModel):
    refresh_token: str


class TokenPayload(BaseModel):
    sub: Optional[str] = None
    jti: Optional[str] = None
    typ: Optional[str] = None
