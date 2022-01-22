from pydantic import BaseModel
from typing import Optional
from typing import List
from uuid import UUID

from .product import ProductWithAmount, Product, ProductWithAmountNew


class StageBase(BaseModel):
    name: Optional[str]
    content: Optional[str]

    class Config:
        orm_mode = True


class StageWithIngredients(StageBase):
    products: Optional[List[ProductWithAmountNew]]


class StageCreate(StageWithIngredients):
    name: str
    content: Optional[str]


class StageUpdate(StageBase):
    pass


class Stage(StageCreate):
    pass


class StageInDB(StageWithIngredients):
    name: str
    content: Optional[str]

    class Config:
        orm_mode = True
