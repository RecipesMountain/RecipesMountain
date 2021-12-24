import uuid

from sqlalchemy import Column, Integer, Date
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base

class Stats(Base):
    date = Column(Date, primary_key=True, index=True)
    viewsTotal = Column(Integer)
    viewsRecpies = Column(Integer)