from typing import Any, List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Tag])
def get_all_tags(
    db: Session = Depends(deps.get_db),
) -> Any:
    return crud.tag.get_all(db)


@router.post("/", response_model=schemas.Tag)
def create_tag(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    pass


@router.put("/{tag_id}", response_model=schemas.Tag)
def update_tag(
    tag_id: UUID,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    pass


@router.delete("/{tag_id}", response_model=bool)
def delete_tag(
    tag_id: UUID,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    pass
