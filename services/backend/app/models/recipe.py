import uuid

from sqlalchemy import Column, ForeignKey, Integer, String, desc, Index, Computed, LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base
from app.models.TSVector import TSVector


class Recipe(Base):

    # TODO ADD decryption?
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    title = Column(String)
    # description = Column(String)
    cookingTime = Column(Integer)
    difficulty = Column(String)
    calories = Column(Integer)
    portion = Column(Integer)
    rating = Column(Integer)


    totalViews = Column(Integer, default=0)
    viewsLast24 = Column(Integer, default=0)
    popularityScore = Column(Integer, default=0)

    image_blob = Column(LargeBinary, nullable=True)
    
    owner_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))

    owner = relationship("User", back_populates="recipes")
    users_favorite = relationship(
        "User", secondary="favorite_recipes", back_populates="favorites"
    )
    tags = relationship("Tag", secondary="recipe_tags", back_populates="recipes")
    stages = relationship("Stage", back_populates="recipe")
    comments = relationship("Comment", back_populates="recipe")

    __ts_vector__ = Column(
        TSVector(), Computed("to_tsvector('english', title )", persisted=True)
    )
    # "to_tsvector('english', title || ' ' || description)",

    __table_args__ = (
        Index("ix_recpie___ts_vector__", __ts_vector__, postgresql_using="gin"),
    )
