from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.base import get_db
from app.core.auth import get_current_active_user, get_current_admin
from app.core.responses import UnifiedAPIRoute
from app.modules.user.service import UserService
from app.modules.user.schemas import UserResponse, UserUpdate
from app.modules.user.models import User

router = APIRouter(route_class=UnifiedAPIRoute)


def get_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.get("/", response_model=list[UserResponse])
def get_all(
    skip: int = 0,
    limit: int = 100,
    svc: UserService = Depends(get_service),
    _: User = Depends(get_current_admin),
):
    return svc.get_all(skip, limit)


@router.get("/{user_id}", response_model=UserResponse)
def get_by_id(
    user_id: int,
    svc: UserService = Depends(get_service),
    _: User = Depends(get_current_admin),
):
    return svc.get_by_id(user_id)


@router.put("/{user_id}", response_model=UserResponse)
def update(
    user_id: int,
    data: UserUpdate,
    svc: UserService = Depends(get_service),
    _: User = Depends(get_current_admin),
):
    return svc.update(user_id, data)


@router.delete("/{user_id}")
def delete(
    user_id: int,
    svc: UserService = Depends(get_service),
    _: User = Depends(get_current_admin),
):
    svc.delete(user_id)
    return {"message": "Deleted successfully"}
