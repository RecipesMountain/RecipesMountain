from typing import Any, Dict, List, Optional, Union
from uuid import UUID

from sqlalchemy.orm import Session, Query
from sqlalchemy.sql.functions import func

from app.crud.base import CRUDBase
from app.models.product import Product

from app.schemas.product import ProductCreate, ProductUpdate


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    def get_all(self, db: Session) -> List[Product]:
        return db.query(Product).all()
    
    def get_by_id(self, db: Session, *, product_id: UUID) -> Optional[Product]:
        return db.query(Product).filter(Product.id == product_id).first()

    def get_by_name(self, db: Session, *, name: str) -> Optional[Product]:
        return db.query(Product).filter(Product.name == name).first()

    def create(self, db: Session, *, obj_in: ProductCreate) -> Product:
        db_obj = Product(name=obj_in.name, price=obj_in.price)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


product = CRUDProduct(Product)
