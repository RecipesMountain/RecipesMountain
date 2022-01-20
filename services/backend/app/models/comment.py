import uuid

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class Comment(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    content = Column(String, nullable=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
    recipe_id = Column(UUID(as_uuid=True), ForeignKey("recipe.id"))

    owner = relationship("User", back_populates="comments")
    recipe = relationship("Recipe", back_populates="comments")
