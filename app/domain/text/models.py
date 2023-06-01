from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ...database import Base

class Text(Base):
    __tablename__ = 'text'

    original_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    source = Column(String, unique=True, index=True)
    content = Column(String, unique=True, index=True)
    lang = Column(String, unique=True, index=True)
    content_creation_date = Column(DateTime(timezone=True), unique=True, index=True)
    id = Column(Integer, ForeignKey('text.id'))
    search_results = relationship("Search_Results")