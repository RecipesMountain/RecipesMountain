from typing import Any, List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models, schemas
from app.api import deps

router = APIRouter()


@router.get("/search", response_model=List[schemas.Product])
def search_products(
    db: Session = Depends(deps.get_db),
    query: str = "",
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    pass


@router.post("/", response_model=schemas.Product)
def create_product(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    pass


@router.put("/{product_id}", response_model=schemas.Product)
def update_product(
    product_id: UUID,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    pass


@router.delete("/{product_id}", response_model=bool)
def delete_product(
    product_id: UUID,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    pass
