import uuid

from sqlalchemy import Column, ForeignKey, Integer, Index, Date
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base
from app.models.TSVector import TSVector

class Stats(Base):
    date = Column(Date, primary_key=True, index=True)
    viewsTotal = Column(Integer)
    viewsRecpies = Column(Integer)