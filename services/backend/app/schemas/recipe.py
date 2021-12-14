from pydantic import BaseModel
from typing import Optional
from typing import List
from .tag import Tag
from .comment import Comment
from .stage import Stage

# TODO: how picture use in model?
# ? send id or no?
class RecipeBase(BaseModel):
    title: Optional[str]
    cookingTime: Optional[str]
    difficulty: Optional[str]
    calories: Optional[int]
    portion: Optional[int]
    rating: Optional[int]


class RecipeWithTags(RecipeBase):
    tags: List[Tag]


class RecipeWithComments(RecipeBase):
    comments: List[Comment]


class RecipeWithStage(RecipeBase):
    stages: List[Stage]


class RecipeCreate(RecipeWithTags, RecipeWithStage):
    pass


class RecipeUpdate:
    pass


class Recipe(RecipeWithTags, RecipeWithComments, RecipeWithStage):
    title: str
    cookingTime: str
    difficulty: str
    calories: int
    portion: int
    rating: int
