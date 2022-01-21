from typing import Any, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, crud, core
from app.api import deps

import requests

router = APIRouter()


@router.get("/search")
def search_products(
    db: Session = Depends(deps.get_db),
    query: str = "",
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    headers = {"Accept": "application/json"}
    payload = {
        "app_id": core.config.settings.EXTERNAL_API_ID_AUTOCOMPLETE,
        "app_key": core.config.settings.EXTERNAL_API_KEY_AUTOCOMPLETE,
        "q": query,
    }
    request = requests.get(
        core.config.settings.EXTERNAL_API_URL, payload, headers=headers
    )
    return request.json()


@router.get("/", response_model=List[schemas.Product])
def get_all_products(
    db: Session = Depends(deps.get_db),
) -> Any:
    return crud.product.get_all(db)


@router.post("/", response_model=schemas.Product)
def create_product(
    *,
    db: Session = Depends(deps.get_db),
    product_in: schemas.ProductCreate,
    current_user: models.User = Depends(deps.get_current_superuser),
) -> Any:
    product = crud.product.get_by_name(db=db, name=product_in.name)
    if product:
        raise HTTPException(
            status_code=400,
            detail="Product with this name already exists in the system",
        )
    product = crud.product.create(db=db, obj_in=product_in)
    return product


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
