from typing import Any, Dict, List, Optional, Union

from sqlalchemy.orm import Session, Query
from sqlalchemy.sql.functions import func

from app.crud.base import CRUDBase
from app.models.tag import Tag

from app.schemas.tag import TagCreate, TagUpdate


class CRUDTag(CRUDBase[Tag, TagCreate, TagUpdate]):
    def get_all(self, db: Session) -> List[Tag]:
        return db.query(Tag).all()

    # TODO rename
    def get_page(self, db: Session, *, skip, limit) -> List[Tag]:
        return db.query(Tag).offset(skip).limit(limit)

    def get_by_name(self, db: Session, *, name: str) -> Optional[Tag]:
        return db.query(Tag).filter(Tag.name == name).first()

    def create(self, db: Session, *, obj_in: TagCreate) -> Tag:
        db_obj = Tag(name=obj_in.name)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    # def update(self, db: Session, *, db_obj: Tag, obj_in: Tag) -> Tag:
    #     db.query(Tag).filter()


tag = CRUDTag(Tag)
