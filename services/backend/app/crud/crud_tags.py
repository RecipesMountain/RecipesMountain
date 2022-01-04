from typing import Any, Dict, List, Optional, Union
from uuid import UUID

from sqlalchemy.orm import Session, Query
from sqlalchemy.sql.functions import func

from app.crud.base import CRUDBase
from app.models.tag import Tag
from app.models.recipe import Recipe

from app.schemas.tag import TagCreate, TagUpdate


class CRUDTag(CRUDBase[Tag, TagCreate, TagUpdate]):
    def get_all(self, db: Session) -> List[Tag]:
        return db.query(Tag).all()

    def get_by_name(self, db: Session, name: str) -> Tag:
        return db.query(Tag).filter(Tag.name == name).first()

    def get_by_id(self, db: Session, id: UUID) -> Tag:
        return db.query(Tag).filter(Tag.id == id).first()

    # TODO rename
    def get_page(self, db: Session, *, skip, limit) -> List[Tag]:
        return db.query(Tag).offset(skip).limit(limit)

    def create(self, db: Session, *, obj_in: TagCreate) -> Tag:
        db_obj = Tag(name=obj_in.name)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Tag, obj_in: Union[TagUpdate, Dict[str, Any]]
    ) -> Tag:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def delete(self, db: Session, *, id: UUID) -> bool:
        rows = db.query(Tag).filter(Tag.id == id).delete()
        db.commit()
        return rows != 0


tag = CRUDTag(Tag)
