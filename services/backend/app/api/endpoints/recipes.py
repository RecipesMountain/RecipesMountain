from typing import Any, List
from uuid import UUID

from fastapi import APIRouter, Query, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.api import deps

router = APIRouter()


@router.get("/search", response_model=List[schemas.RecipeSearch])
def search_recipes(
    db: Session = Depends(deps.get_db),
    keywords: str = "",
    skip: int = 0,
    limit: int = 100,
    sort: str = "popular",
    tags: List[str] = Query([]),
    tagsConnect: str = "and",
) -> Any:
    # TODO USE ENUM HERE
    if tagsConnect not in ["or", "and"]:
        raise HTTPException(
            status_code=400,
            detail="Bad tags connect",
        )
    # TODO use enum
    if sort not in ["popular", "views", "best", "nosort"]:
        raise HTTPException(
            status_code=400,
            detail="Bad tags connect",
        )

    keywords = keywords.replace("+", " ")

    query = crud.recipe.start_query(db)

    if keywords != "":
        query = crud.recipe.with_keyword(query, keyword=keywords)

    if tags != []:
        print(tags)
        if tagsConnect == "and":
            query = crud.recipe.with_tags_and(query, tags=tags)
        else:
            raise HTTPException(
                status_code=400,
                detail="Not Implemented",
            )

    if sort == "popular":
        query = crud.recipe.sort_popularity(query)
    elif sort == "views":
        query = crud.recipe.sort_views(query)
    elif sort == "best":
        query = crud.recipe.sort_best(query)

    r = crud.recipe.execQuery(query, skip=skip, limit=limit)
    return r


@router.get("/popular", response_model=List[schemas.RecipeSearch])
def get_popular_recipes(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    query = crud.recipe.start_query(db)
    query = crud.recipe.sort_popularity(query)
    return crud.recipe.execQuery(query, skip=skip, limit=limit)


@router.get("/best", response_model=List[schemas.RecipeSearch])
def get_best_recipes(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    query = crud.recipe.start_query(db)
    query = crud.recipe.sort_best(query)
    return crud.recipe.execQuery(query, skip=skip, limit=limit)


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
