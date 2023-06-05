from sqlalchemy import Column, ForeignKey, Integer, Text, DateTime, func
from sqlalchemy.orm import relationship

from ...database import Base

class UserSearch(Base):
    __tablename__ = "user_search"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    search_id = Column(Integer, ForeignKey('search.id'))
    search_text = Column(Text, unique=True, index=True)
    created_at = Column(DateTime, default=func.now(), onupdate=func.now())

    user = relationship("User", foreign_keys=[user_id])
    search = relationship("Search", foreign_keys=[search_id])
