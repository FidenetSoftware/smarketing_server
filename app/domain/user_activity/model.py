from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func, JSON
from sqlalchemy.orm import relationship

from ...database import Base

class UserActivity(Base):
    __tablename__ = "user_activity"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    search_id = Column(Integer, ForeignKey('search.id'))
    activity_type = Column(String, unique=True, index=True)
    activity_data = Column(JSON, nullable=False)
    creation_date = Column(DateTime, default=func.now(), onupdate=func.now())
    update_date = Column(DateTime, default=func.now(), onupdate=func.now())

    user = relationship("User", foreign_keys=[user_id])
    search = relationship("Search", foreign_keys=[search_id])
