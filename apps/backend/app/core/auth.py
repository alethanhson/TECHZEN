from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from app.core.config import settings
from app.core.exceptions import UnauthorizedException, ForbiddenException
from app.db.base import get_db
from app.modules.user.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_STR}/auth/login")


def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme),
) -> User:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise UnauthorizedException("Invalid token payload")
    except JWTError:
        raise UnauthorizedException("Could not validate credentials")

    user = db.execute(
        select(User).options(joinedload(User.role)).where(User.username == username)
    ).scalars().first()

    if user is None:
        raise UnauthorizedException("User not found")
    return user


def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_active:
        raise ForbiddenException("Inactive user")
    return current_user


def get_current_admin(current_user: User = Depends(get_current_active_user)) -> User:
    if not current_user.is_superuser:
        raise ForbiddenException("Not enough privileges")
    return current_user
