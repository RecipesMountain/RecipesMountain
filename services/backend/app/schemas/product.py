from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID


class ProductBase(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    name: str
    price: int


class ProductUpdate(ProductBase):
    pass


class ProductWithAmount(ProductCreate):
    product_id: Optional[UUID]
    amount: Optional[float]
    amount_unit: Optional[str]


class ProductInDBBase(ProductBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


class Product(ProductInDBBase):
    pass
