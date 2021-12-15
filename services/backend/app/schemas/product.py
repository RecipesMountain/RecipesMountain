from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class ProductBase(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None


class ProductCreate(ProductBase):
    name: str
    price: int


class ProductUpdate(ProductBase):
    pass


class ProductInDBBase(ProductBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


class Product(ProductInDBBase):
    pass
