from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.associationproxy import association_proxy

from app.db.base_class import Base

from sqlalchemy.orm import relationship


class ProductsInStages(Base):
    product_id = Column(UUID(as_uuid=True), ForeignKey("product.id"), primary_key=True)
    stage_id = Column(UUID(as_uuid=True), ForeignKey("stage.id"), primary_key=True)
    amount = Column(Float, nullable=False)
    amount_unit = Column(String, nullable=False)

    product = relationship("Product", back_populates="stages")
    stage = relationship("Stage", back_populates="products")

    # proxies
    name = association_proxy(target_collection="product", attr="name")
    price = association_proxy(target_collection="product", attr="price")
