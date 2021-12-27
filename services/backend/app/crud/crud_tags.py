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


tag = CRUDTag(Tag)
