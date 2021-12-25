from typing_extensions import IntVar
from pydantic import BaseModel
from typing import Optional
from typing import List
from .tag import Tag
from .comment import Comment
from .stage import Stage
from uuid import UUID

# TODO: how picture use in model?
# ? send id or no?
class RecipeBase(BaseModel):
    title: Optional[str]
    cookingTime: Optional[int]
    difficulty: Optional[str]
    calories: Optional[int]
    portion: Optional[int]
    rating: Optional[int]
    totalViews: Optional[int]


class RecipeWithTags(RecipeBase):
    tags: List[Tag]


class RecipeWithComments(RecipeBase):
    comments: List[Comment]


class RecipeWithStage(RecipeBase):
    stages: List[Stage]

class RecpieInDB(RecipeWithTags, RecipeWithStage, RecipeWithComments):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True

class RecpieSearch(RecipeWithTags):
    id: Optional[UUID] = None
    class Config:
        orm_mode = True


class SearchResult(BaseModel):
    total: int
    recpies: List[RecpieSearch]

class RecipeCreate(RecipeWithTags, RecipeWithStage):
    pass


class RecipeUpdate:
    pass


class Recipe(RecpieInDB):
    title: str
    cookingTime: int
    difficulty: str
    calories: int
    portion: int
    totalViews: int
