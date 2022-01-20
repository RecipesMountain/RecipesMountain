from typing import Any, List, Optional
from uuid import UUID

from fastapi import APIRouter, Query, Depends, HTTPException

from fastapi import File, UploadFile

from sqlalchemy.orm import Session

from app import models, schemas, crud
from app.api import deps

from fastapi.responses import Response


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
            detail='Bad sort, aviable "popular", "views", "best", "nosort"',
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


@router.get("/favorites", response_model=List[schemas.RecipeSearch])
def get_favorites_recipes(
    *,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    favorite_recipies = crud.recipe.get_favorite_recepies(
        db=db, user_id=current_user.id
    )
    return favorite_recipies


@router.put("/like/{recipe_id}", response_model=bool)
def like_or_unlike(
    *,
    recipe_id: UUID,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    return crud.recipe.add_of_delete_from_favorites(
        db=db, user_id=current_user.id, recipe_id=recipe_id
    )


@router.get("/isLiked/{recipe_id}", response_model=bool)
def is_liked_by_user(
    *,
    recipe_id: UUID,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    return crud.recipe.is_liked(db=db, user_id=current_user.id, recipe_id=recipe_id)


@router.get("/{recipe_id}", response_model=schemas.Recipe)
def get_recipe_by_id(
    recipe_id: UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get recipe by id
    """
    recipe = crud.recipe.get_and_incrementViews(db=db, recipe_id=recipe_id)
    if recipe:
        return recipe
    else:
        raise HTTPException(status_code=404, detail="Recipe not exists.")


@router.post("/", response_model=schemas.Recipe)
def create_recipe(
    *,
    db: Session = Depends(deps.get_db),
    recipe_in: schemas.RecipeCreate,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Create recipe
    """
    recipe = crud.recipe.create(db, obj_in=recipe_in, owner_id=current_user.id)
    return recipe


@router.post("/img/{recipe_id}")
def add_image(
    *,
    db: Session = Depends(deps.get_db),
    recipe_id: UUID,
    image: Optional[bytes] = File(None),
    current_user: models.User = Depends(deps.get_current_user),
):

    recipe = crud.recipe.get_by_id(db=db, recipe_id=recipe_id)
    if recipe:
        if recipe.owner_id == current_user.id:
            crud.recipe.add_image(db=db, recipe_id=recipe_id, file=image)
        else:
            raise HTTPException(
                status_code=403,
                detail="You dont have permission to this operation - Update image",
            )
    else:
        raise HTTPException(status_code=404, detail="Recipe not exists.")

    return Response(content=image, media_type="image/png")


@router.get("/img/{recipe_id}")
def get_recipe_img(
    recipe_id: UUID,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get image for recipe
    """
    recipe = crud.recipe.get_by_id(db=db, recipe_id=recipe_id)

    if recipe:
        recipe_img = recipe.image_blob

        return Response(content=recipe_img, media_type="image/png")

    return {"imageStatus": "empty"}


@router.put("/{recipe_id}", response_model=schemas.Recipe)
def update_recipe(
    *,
    recipe_id: UUID,
    db: Session = Depends(deps.get_db),
    recipe_in: schemas.RecipeUpdate,
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    recipe = crud.recipe.get_by_id(db=db, recipe_id=recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found.")
    # TODO: check if this is correct user
    else:
        if recipe.owner_id == current_user.id:
            recipe = crud.recipe.update(db=db, obj_in=recipe_in, recipe_id=recipe_id)
        else:
            raise HTTPException(
                status_code=403,
                detail="You dont have permission to this operation - Update recipe",
            )

    return recipe


@router.delete("/{recipe_id}", response_model=bool)
def delete_recipe(
    recipe_id: UUID,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    return crud.recipe.delete(db, recipe_id=recipe_id)


@router.put("/{recipe_id}/rate", response_model=int)
def rate_recpie(
    recipe_id: UUID,
    newRating: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    if newRating > 50:
        newRating = 50
    if newRating < 0:
        newRating = 0
    return crud.recipe.rate(
        db, recipe_id=recipe_id, newRating=newRating, user_id=current_user.id
    )

