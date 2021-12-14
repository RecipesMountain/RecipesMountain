from pydantic import BaseModel
from typing import Optional
from typing import List
from .tag import Tag
from .comment import Comment
from .stage import Stage

#TODO: how picture use in model?
#? send id or no?
class RecpieBase(BaseModel):
    title: Optional[str]
    cookingTime: Optional[str]
    difficulty: Optional[str]
    calories: Optional[int]
    portion: Optional[int]
    rating: Optional[int]

class RecpieWithTags(RecpieBase):
    tags: List[Tag]

class RecpieWithComments(RecpieBase):
    comments: List[Comment]

class RecpieWithStage(RecpieBase):
    stages: List[Stage]

class RecpieCreate(RecpieWithTags, RecpieWithStage):
    pass

class RecpieUpdate():
    pass

class Recpie(RecpieWithTags, RecpieWithComments, RecpieWithStage):
    title: str
    cookingTime: str
    difficulty: str
    calories: int
    portion: int
    rating: int

