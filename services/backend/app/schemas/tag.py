from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID

class TagBase(BaseModel):
    name: Optional[str] = None


class TagCreate(TagBase):
    name: str


class TagUpdate(TagBase):
    recipes: Optional[List[str]]


class TagInDBBase(TagBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


class Tag(TagInDBBase):
    pass
