from pydantic import BaseModel
from typing import Optional
from uuid import UUID

#! name optional. content no ?
class StageBase(BaseModel):
    name: Optional[str] 
    content: Optional[str]

class StageCreate(StageBase):
    name: str 
    content: Optional[str]

class StageUpdate(StageBase):
    pass

class StageWithProduct():
    pass

class Stage(StageCreate):
    pass


class StageInDBBase(Stage):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True
