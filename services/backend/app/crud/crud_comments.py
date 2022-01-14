from typing import Any, Dict, List, Optional, Union

from sqlalchemy.orm import Session, Query
from sqlalchemy.sql.expression import delete
from sqlalchemy.sql.functions import func

from app.crud.base import CRUDBase
from app.models.recipe import Recipe
from app.models.comment import Comment
from app.models.user import User

from app.schemas.comment import CommentCreate, CommentUpdate

from uuid import UUID


class CRUDRecipe(CRUDBase[Comment, CommentCreate, CommentUpdate]):
    def get(
        self, db: Session, *, recipe_id: UUID, skip: int = 0, limit: int = 100
    ) -> List[Comment]:
        return (
            db.query(Comment)
            .filter(Comment.recipe_id == recipe_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create(
        self, db: Session, *, obj_in: CommentCreate, recipe_id: UUID, owner_id: UUID
    ) -> Comment:
        db_obj = Comment(content=obj_in.content, owner_id=owner_id, recipe_id=recipe_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, comment_id: UUID) -> bool:
        comment = db.query(Comment).filter(Comment.id == comment_id).first()
        r = db.delete(comment)
        db.commit()
        return r != 0


comment = CRUDRecipe(Comment)
