import uuid

from sqlalchemy import Boolean, Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_superuser = Column(Boolean, nullable=False, default=False)

    comments = relationship("Comment", back_populates="owner")
    recipes = relationship("Recipe", back_populates="owner")
    favorites = relationship(
        "Recipe", secondary="favorite_recipes", back_populates="users_favorite"
    )
