from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ...database import Base

class Search_Results(Base):
    __tablename__ = 'search_results'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    search_id = Column(Integer, ForeignKey('search.id'))
    search = relationship("Search")
    text_id = Column(Integer, ForeignKey('text.id'))
    search = relationship("Text")
