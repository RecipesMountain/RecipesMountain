from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class RecipeTags(Base):
    recipe_id = Column(UUID(as_uuid=True), ForeignKey("recipe.id"), primary_key=True)
    tag_id = Column(UUID(as_uuid=True), ForeignKey("tag.id"), primary_key=True)
