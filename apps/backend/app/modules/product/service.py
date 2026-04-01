from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.exceptions import NotFoundException, AlreadyExistsException
from app.modules.product.models import Product
from app.modules.product.schemas import ProductCreate, ProductUpdate


class ProductService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100) -> list[Product]:
        query = select(Product).offset(skip).limit(limit)
        return list(self.db.execute(query).scalars().all())

    def get_by_id(self, product_id: int) -> Product:
        product = self.db.execute(
            select(Product).where(Product.id == product_id)
        ).scalars().first()
        if not product:
            raise NotFoundException(f"Product #{product_id} not found")
        return product

    def create(self, data: ProductCreate) -> Product:
        existing = self.db.execute(
            select(Product).where(Product.code == data.code)
        ).scalars().first()
        if existing:
            raise AlreadyExistsException(f"Product code '{data.code}' already exists")

        product = Product(**data.model_dump())
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def update(self, product_id: int, data: ProductUpdate) -> Product:
        product = self.get_by_id(product_id)
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(product, key, value)
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete(self, product_id: int) -> None:
        product = self.get_by_id(product_id)
        self.db.delete(product)
        self.db.commit()
