from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from .comment import Comment
from .stage import Stage
from .tag import Tag
from .user import User


# TODO: how picture use in model?
# ? send id or no?
class RecipeBase(BaseModel):
    title: Optional[str]
    description: Optional[str]
    rating: Optional[int]
    totalViews: Optional[int]


class RecipeWithInfo(RecipeBase):
    cookingTime: Optional[int]
    difficulty: Optional[str]
    calories: Optional[int]
    portion: Optional[int]


class RecipeWithTags(RecipeWithInfo):
    tags: List[Tag]


class RecipeWithComments(RecipeWithInfo):
    comments: List[Comment]


class RecipeWithStage(RecipeWithInfo):
    stages: List[Stage]


class RecipeWithImage(RecipeBase):
    pass


class RecipeInDB(RecipeWithTags, RecipeWithStage, RecipeWithComments):
    id: Optional[UUID] = None
    owner: Optional[User]

    class Config:
        orm_mode = True


class RecipeSearch(RecipeBase):
    id: Optional[UUID] = None
    owner: Optional[User]

    class Config:
        orm_mode = True


class SearchResult(BaseModel):
    total: int
    recipes: List[RecipeSearch]


class RecipeCreate(RecipeWithTags, RecipeWithStage):
    pass


class RecipeUpdate(RecipeBase):
    tags: Optional[List[Tag]]
    stages: Optional[List[Stage]]


class Recipe(RecipeInDB):
    title: str
    description: str
    cookingTime: int
    difficulty: str
    calories: int
    portion: int
    totalViews: int
