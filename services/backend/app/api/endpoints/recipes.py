from typing import Any, List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models, schemas
from app.api import deps

router = APIRouter()


@router.get("/search", response_model=List[schemas.Recipe])
def search_recipes(
    db: Session = Depends(deps.get_db),
    keywords: str = "",
    skip: int = 0,
    limit: int = 100,
    sort: str = "relevance",
    tags: str = "",
) -> Any:
    pass


@router.get("/popular", response_model=List[schemas.Recipe])
def get_popular_recipes(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    pass


@router.get("/best", response_model=List[schemas.Recipe])
def get_best_recipes(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    pass


@router.get("/{recipe_id}", response_model=schemas.Recipe)
def get_recipe_by_id(
    recipe_id: UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    pass


@router.post("/", response_model=schemas.Recipe)
def create_recipe(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    pass


@router.put("/{recipe_id}", response_model=schemas.Recipe)
def update_recipe(
    recipe_id: UUID,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    pass


@router.delete("/{recipe_id}", response_model=bool)
def delete_recipe(
    recipe_id: UUID,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    pass
