from sqlalchemy import select, or_, func
from sqlalchemy.orm import Session, selectinload

from app.core.exceptions import NotFoundException, AlreadyExistsException
from app.modules.product.models import Product, Tag
from app.modules.product.schemas import ProductCreate, ProductUpdate


class ProductService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100, q: str = None) -> tuple[list[Product], int]:
        query = select(Product).options(selectinload(Product.tags))
        if q:
            query = query.where(
                or_(
                    Product.name.ilike(f"%{q}%"),
                    Product.code.ilike(f"%{q}%")
                )
            )
        
        count_query = select(func.count()).select_from(query.subquery())
        total = self.db.execute(count_query).scalar()
        
        items = self.db.execute(query.offset(skip).limit(limit)).scalars().all()
        return list(items), total or 0

    def get_by_id(self, product_id: int) -> Product:
        product = self.db.execute(
            select(Product)
            .options(selectinload(Product.tags))
            .where(Product.id == product_id)
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

        product_data = data.model_dump(exclude={"tags"})
        product = Product(**product_data)
        
        if data.tags:
            for tag_name in data.tags:
                product.tags.append(Tag(name=tag_name))

        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def update(self, product_id: int, data: ProductUpdate) -> Product:
        product = self.get_by_id(product_id)
        
        update_data = data.model_dump(exclude_unset=True)
        
        if "tags" in update_data:
            new_tags = update_data.pop("tags")
            product.tags.clear() # Nhờ quan hệ Delete-Orphan nên table sẽ xoá luôn tag mồ côi
            for tag_name in new_tags:
                product.tags.append(Tag(name=tag_name))
                
        for key, value in update_data.items():
            setattr(product, key, value)
            
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete(self, product_id: int) -> None:
        product = self.get_by_id(product_id)
        self.db.delete(product)
        self.db.commit()
