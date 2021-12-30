from pydantic import BaseModel
from typing import Optional
from typing import List
from uuid import UUID

from .product import ProductWithAmount, Product

#! name optional. content no ?
# class StageBase(BaseModel):
#     name: Optional[str]
#     content: Optional[str]

#     class Config:
#         orm_mode = True


# class StageWithIngredients(StageBase):
#     products: List[ProductWithAmount]

# class StageCreate(StageWithIngredients):
#     name: str
#     content: Optional[str]

# class StageUpdate(StageBase):
#     pass


# class StageWithProduct:
#     pass


# class Stage(StageCreate):
#     pass


# class StageInDBBase(Stage):
#     id: Optional[UUID] = None

#     class Config:
#         orm_mode = True

class StageBase(BaseModel):
    name: Optional[str]
    content: Optional[str]

    class Config:
        orm_mode = True
    

class StageWithIngredients(StageBase):
    products: Optional[List[ProductWithAmount]]


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
    



# class StageTest(StageBase):
#     name: str
#     content: Optional[str]



# # class Stage(StageInDB):
# #     pass

# class SBase(BaseModel):
#     name: Optional[str]
#     content: Optional[str]

#     class Config:
#         orm_mode = True

# class CBase(SBase):
#     name: str
#     content: str
#     products: List[ProductWithAmount]



