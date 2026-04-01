from datetime import datetime, timezone
from jose import jwt, JWTError
from sqlalchemy import select, update
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.security import verify_password, get_password_hash, create_access_token, create_refresh_token
from app.core.exceptions import UnauthorizedException, AlreadyExistsException
from app.modules.auth.models import RefreshToken
from app.modules.auth.schemas import TokenPayload
from app.modules.user.models import User


class AuthService:

    def __init__(self, db: Session):
        self.db = db

    def register(self, username: str, email: str, password: str, role_id: int = 2) -> User:
        if self.db.execute(select(User).where(User.username == username)).scalars().first():
            raise AlreadyExistsException("Username already registered")
        if self.db.execute(select(User).where(User.email == email)).scalars().first():
            raise AlreadyExistsException("Email already registered")

        user = User(
            username=username,
            email=email,
            hashed_password=get_password_hash(password),
            is_active=True,
            role_id=role_id,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def login(self, username: str, password: str) -> dict:
        user = self.db.execute(select(User).where(User.username == username)).scalars().first()
        if not user or not verify_password(password, user.hashed_password):
            raise UnauthorizedException("Incorrect username or password")

        res_dict = self._generate_tokens(user.id, user.username)
        res_dict["user"] = user
        return res_dict

    def refresh(self, refresh_token_str: str) -> dict:
        payload = self._decode_refresh_token(refresh_token_str)
        db_token = self._validate_db_token(payload)

        db_token.is_revoked = True
        self.db.commit()

        return self._generate_tokens(db_token.user_id, payload.sub)

    def _generate_tokens(self, user_id: int, username: str) -> dict:
        access_token = create_access_token(subject=username)
        refresh_token, jti, expires_at = create_refresh_token(subject=username)

        self.db.add(RefreshToken(user_id=user_id, jti=jti, expires_at=expires_at))
        self.db.commit()

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }

    def _decode_refresh_token(self, token: str) -> TokenPayload:
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            data = TokenPayload(**payload)
            if data.typ != "refresh" or not data.jti:
                raise UnauthorizedException("Invalid token type")
            return data
        except JWTError:
            raise UnauthorizedException("Invalid token")

    def _validate_db_token(self, data: TokenPayload) -> RefreshToken:
        db_token = self.db.execute(
            select(RefreshToken).where(RefreshToken.jti == data.jti)
        ).scalars().first()

        if not db_token:
            raise UnauthorizedException("Token not found")

        if db_token.is_revoked:
            self.db.execute(
                update(RefreshToken)
                .where(RefreshToken.user_id == db_token.user_id, RefreshToken.is_revoked == False)
                .values(is_revoked=True)
            )
            self.db.commit()
            raise UnauthorizedException("Token has been revoked")

        if db_token.expires_at.replace(tzinfo=timezone.utc) < datetime.now(timezone.utc):
            raise UnauthorizedException("Token expired")

        return db_token
