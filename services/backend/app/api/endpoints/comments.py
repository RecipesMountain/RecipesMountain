from typing import Any, List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.api import deps

router = APIRouter()


@router.get("/{recipe_id}", response_model=List[schemas.Comment])
def get_comments_by_recipe_id(
    recipe_id: UUID,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    return crud.comment.get(db, recipe_id=recipe_id, skip=skip, limit=limit)


@router.post("/{recipe_id}", response_model=schemas.Comment)
def create_comment(
    recipe_id: UUID,
    comment_in: schemas.CommentCreate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    return crud.comment.create(db, obj_in=comment_in, recipe_id=recipe_id, owner_id=current_user.id)


@router.put("/{recipe_id}/{comment_id}", response_model=schemas.Comment)
def update_comment(
    recipe_id: UUID,
    comment_id: UUID,
    comment_in: schemas.CommentUpdate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    return crud.comment.update(db, obj_in=comment_in, comment_id=comment_id)


@router.delete("/{recipe_id}/{comment_id}", response_model=bool)
def delete_comment(
    recipe_id: UUID,
    comment_id: UUID,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    return crud.comment.delete(db, comment_id=comment_id)
