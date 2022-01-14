from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from app.schemas.user import UserComment


class CommentBase(BaseModel):
    content: Optional[str] = None


class CommentCreate(CommentBase):
    content: str


class CommentUpdate(CommentBase):
    pass


class CommentInDBBase(CommentBase):
    id: Optional[UUID] = None
    owner: UserComment

    class Config:
        orm_mode = True


class Comment(CommentInDBBase):
    pass
