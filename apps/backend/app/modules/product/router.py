from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.base import get_db
from app.core.responses import UnifiedAPIRoute
from app.core.auth import get_current_admin
from app.modules.user.models import User
from app.modules.product.service import ProductService
from app.modules.product.schemas import ProductCreate, ProductUpdate, ProductResponse, PaginatedProductResponse
from typing import Optional

router = APIRouter(route_class=UnifiedAPIRoute)


def get_service(db: Session = Depends(get_db)) -> ProductService:
    return ProductService(db)


@router.get("/", response_model=PaginatedProductResponse)
def get_all(
    skip: int = 0, 
    limit: int = 100, 
    q: Optional[str] = None, 
    svc: ProductService = Depends(get_service),
    _: User = Depends(get_current_admin),
):
    items, total = svc.get_all(skip, limit, q)
    return {"items": items, "total": total}


@router.get("/{product_id}", response_model=ProductResponse)
def get_by_id(
    product_id: int, 
    svc: ProductService = Depends(get_service),
    _: User = Depends(get_current_admin),
):
    return svc.get_by_id(product_id)


@router.post("/", response_model=ProductResponse, status_code=201)
def create(
    data: ProductCreate, 
    svc: ProductService = Depends(get_service),
    _: User = Depends(get_current_admin),
):
    return svc.create(data)


@router.put("/{product_id}", response_model=ProductResponse)
def update(
    product_id: int, 
    data: ProductUpdate, 
    svc: ProductService = Depends(get_service),
    _: User = Depends(get_current_admin),
):
    return svc.update(product_id, data)


@router.delete("/{product_id}")
def delete(
    product_id: int, 
    svc: ProductService = Depends(get_service),
    _: User = Depends(get_current_admin),
):
    svc.delete(product_id)
    return {"message": "Deleted successfully"}
