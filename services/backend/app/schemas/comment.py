from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class CommentBase(BaseModel):
    content: str

class CommentInDBBase(CommentBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True

class Comment(CommentInDBBase):
    pass