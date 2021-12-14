import uuid

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class Recipe(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    title = Column(String)
    cooking_time = Column(Integer)
    difficulty = Column(String)
    calories = Column(Integer)
    portions = Column(Integer)
    rating = Column(Integer)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))

    owner = relationship("User", back_populates="recipes")
    users_favorite = relationship(
        "User", secondary="favorite_recipes", back_populates="favorites"
    )
    tags = relationship("Tag", secondary="recipe_tags", back_populates="recipes")
    stages = relationship("Stage", back_populates="recipe")
    comments = relationship("Comment", back_populates="recipe")
