from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import Integer

from app.db.base_class import Base


class RecipeRatings(Base):
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), primary_key=True)
    recipe_id = Column(UUID(as_uuid=True), ForeignKey("recipe.id"), primary_key=True)
    rating = Column(Integer, default=0)
