import uuid

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class Stage(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    content = Column(String, nullable=False)
    recipe_id = Column(UUID(as_uuid=True), ForeignKey("recipe.id"))

    recipe = relationship("Recipe", back_populates="stages")
    products = relationship(
        "Product", secondary="products_in_stages", back_populates="stages"
    )
