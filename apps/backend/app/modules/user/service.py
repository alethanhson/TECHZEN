from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.core.security import get_password_hash
from app.core.exceptions import NotFoundException
from app.modules.user.models import User
from app.modules.user.schemas import UserUpdate


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100) -> list[User]:
        query = select(User).options(joinedload(User.role)).offset(skip).limit(limit)
        return list(self.db.execute(query).scalars().unique().all())

    def get_by_id(self, user_id: int) -> User:
        user = self.db.execute(
            select(User).options(joinedload(User.role)).where(User.id == user_id)
        ).scalars().first()
        if not user:
            raise NotFoundException(f"User #{user_id} not found")
        return user

    def update(self, user_id: int, data: UserUpdate) -> User:
        user = self.get_by_id(user_id)
        update_data = data.model_dump(exclude_unset=True)

        if "password" in update_data:
            update_data["hashed_password"] = get_password_hash(update_data.pop("password"))

        for key, value in update_data.items():
            setattr(user, key, value)

        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user_id: int) -> None:
        user = self.get_by_id(user_id)
        self.db.delete(user)
        self.db.commit()
