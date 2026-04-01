from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.base import get_db
from app.core.responses import UnifiedAPIRoute
from app.modules.product.service import ProductService
from app.modules.product.schemas import ProductCreate, ProductUpdate, ProductResponse

router = APIRouter(route_class=UnifiedAPIRoute)


def get_service(db: Session = Depends(get_db)) -> ProductService:
    return ProductService(db)


@router.get("/", response_model=list[ProductResponse])
def get_all(skip: int = 0, limit: int = 100, svc: ProductService = Depends(get_service)):
    return svc.get_all(skip, limit)


@router.get("/{product_id}", response_model=ProductResponse)
def get_by_id(product_id: int, svc: ProductService = Depends(get_service)):
    return svc.get_by_id(product_id)


@router.post("/", response_model=ProductResponse, status_code=201)
def create(data: ProductCreate, svc: ProductService = Depends(get_service)):
    return svc.create(data)


@router.put("/{product_id}", response_model=ProductResponse)
def update(product_id: int, data: ProductUpdate, svc: ProductService = Depends(get_service)):
    return svc.update(product_id, data)


@router.delete("/{product_id}")
def delete(product_id: int, svc: ProductService = Depends(get_service)):
    svc.delete(product_id)
    return {"message": "Deleted successfully"}
