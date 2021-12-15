from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class ProductsInStages(Base):
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"), primary_key=True)
    stage_id = Column(UUID(as_uuid=True), ForeignKey("stage.id"), primary_key=True)
    amount = Column(Float, nullable=False)
    amount_unit = Column(String, nullable=False)
