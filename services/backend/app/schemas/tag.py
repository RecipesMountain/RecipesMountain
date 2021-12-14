from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class TagBase(BaseModel):
    name: str


class TagInDBBase(TagBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True

class Tag(TagInDBBase):
    pass
