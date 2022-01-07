from typing import List, Tuple
from uuid import UUID
from sqlalchemy.orm.session import Session
from app.tests.utils.utils import random_lower_string, random_email
from app import crud
from app.schemas.user import UserCreate
from app.schemas.recipe import RecipeCreate
from app.schemas.tag import TagCreate


def createUser(db: Session) -> UUID:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password)
    return crud.user.create(db, obj_in=user_in).id


def createRecpie(db: Session) -> Tuple[UUID, str]:
    owner_id = createUser(db)
    title = random_lower_string() + " " + random_lower_string()
    recipe_in = RecipeCreate(
        title=title,
        cookingTime=50,
        difficulty="easy",
        calories="4000",
        portion=4,
        stages=[],
        tags=[],
    )
    recipe = crud.recipe.create(db, obj_in=recipe_in, owner_id=owner_id)
    assert recipe.title == title
    return recipe.id, title


def createRecpies(db: Session, title: str, amount: int) -> None:
    owner_id = createUser(db)
    for i in range(amount):
        recipe_in = RecipeCreate(
            title=title,
            cookingTime=50,
            difficulty="easy",
            calories="4000",
            portion=4,
            stages=[],
            tags=[],
        )
        crud.recipe.create(db, obj_in=recipe_in, owner_id=owner_id)


def createRecpiesWithTags(
    db: Session, title: str, amount: int, tagsNames: List[str]
) -> None:
    tags = []
    for name in tagsNames:
        tag_in = TagCreate(name=name)
        tags.append(crud.tag.create(db, obj_in=tag_in))

    owner_id = createUser(db)
    for i in range(amount):
        recipe_in = RecipeCreate(
            title=title,
            cookingTime=50,
            difficulty="easy",
            calories="4000",
            portion=4,
            stages=[],
            tags=tags,
        )
        crud.recipe.create(db, obj_in=recipe_in, owner_id=owner_id)
