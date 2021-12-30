import uuid

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class Product(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    # stages = relationship(
    #     "Stage", secondary="products_in_stages", back_populates="products"
    # )
    stages = relationship("ProductsInStages", back_populates="product")
