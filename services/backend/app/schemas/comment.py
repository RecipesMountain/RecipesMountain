from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class CommentBase(BaseModel):
    content: Optional[str] = None


class CommentCreate(CommentBase):
    content: str


class CommentUpdate(CommentBase):
    pass


class CommentInDBBase(CommentBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True


class Comment(CommentInDBBase):
    pass
