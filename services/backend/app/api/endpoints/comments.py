from typing import Any, List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models, schemas
from app.api import deps

router = APIRouter()


@router.get("/{recipe_id}", response_model=List[schemas.Comment])
def get_comments_by_recipe_id(
    recipe_id: UUID,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    sort: str = "best",
) -> Any:
    pass


@router.post("/{recipe_id}", response_model=schemas.Comment)
def create_comment(
    recipe_id: UUID,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    pass


@router.put("/{recipe_id}/{comment_id}", response_model=schemas.Comment)
def update_comment(
    recipe_id: UUID,
    comment_id: UUID,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    pass


@router.delete("/{recipe_id}/{comment_id}", response_model=bool)
def delete_comment(
    recipe_id: UUID,
    comment_id: UUID,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    pass
