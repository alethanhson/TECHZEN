from pydantic import BaseModel, ConfigDict
from typing import Optional

class TagResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str


class ProductCreate(BaseModel):
    code: str
    name: str
    description: Optional[str] = None
    price: float = 0
    quantity: int = 0
    is_active: bool = True
    tags: Optional[list[str]] = []


class ProductUpdate(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    is_active: Optional[bool] = None
    tags: Optional[list[str]] = None


class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    code: str
    name: str
    description: Optional[str] = None
    price: float
    quantity: int
    is_active: bool
    tags: list[TagResponse] = []

class PaginatedProductResponse(BaseModel):
    items: list[ProductResponse]
    total: int
