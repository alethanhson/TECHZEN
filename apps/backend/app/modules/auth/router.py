from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.base import get_db
from app.core.responses import UnifiedAPIRoute
from app.modules.auth.service import AuthService
from app.modules.auth.schemas import TokenResponse, TokenRefreshRequest, RegisterRequest
from app.modules.user.schemas import UserResponse

router = APIRouter(route_class=UnifiedAPIRoute)


def get_service(db: Session = Depends(get_db)) -> AuthService:
    return AuthService(db)


@router.post("/register", response_model=UserResponse)
def register(data: RegisterRequest, svc: AuthService = Depends(get_service)):
    return svc.register(data.username, data.email, data.password, data.role_id)


@router.post("/login", response_model=TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    svc: AuthService = Depends(get_service),
):
    return svc.login(form_data.username, form_data.password)


@router.post("/refresh", response_model=TokenResponse)
def refresh(data: TokenRefreshRequest, svc: AuthService = Depends(get_service)):
    return svc.refresh(data.refresh_token)