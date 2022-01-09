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
    def get(self, db: Session, *, recipe_id: UUID, skip: int, limit: int) -> List[Comment]:
        return db.query(Comment).filter(Comment.recipe_id == recipe_id).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: CommentCreate, recipe_id: UUID, owner_id: UUID) -> Comment:
        db_obj = Comment(content=obj_in.content, owner_id=owner_id, recipe_id=recipe_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update(self, db: Session, *, comment_id: UUID, obj_in: Union[CommentUpdate, Dict[str, Any]]) -> Comment:
        db_obj = db.query(Comment).filter(Comment.id == comment_id).first()
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)
    
    def delete(self, db: Session, *, comment_id: UUID) -> bool:
        comment = db.query(Comment).filter(Comment.id == comment_id).first()
        r = db.delete(comment)
        return r != 0

comment = CRUDRecipe(Comment)