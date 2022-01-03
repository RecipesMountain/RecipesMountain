# import uuid

# from sqlalchemy import Column, ForeignKey, String
# from sqlalchemy.orm import relationship
# from sqlalchemy.dialects.postgresql import UUID

# from app.db.base_class import Base

# class Step(Base):
#     id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
#     content = Column(String, nullable=False)
#     stage_id = Column(UUID(as_uuid=True), ForeignKey("stage.id"))

#     stage = relationship("Stage", back_populates="steps")
