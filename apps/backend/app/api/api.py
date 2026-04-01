from fastapi import APIRouter
from app.modules.auth import router as auth_router
from app.modules.user import router as user_router
from app.modules.product import router as product_router

api_router = APIRouter()
api_router.include_router(auth_router.router, prefix="/auth", tags=["Auth"])
api_router.include_router(user_router.router, prefix="/users", tags=["Users"])
api_router.include_router(product_router.router, prefix="/products", tags=["Products"])
