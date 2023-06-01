from sqlalchemy import Boolean, Column, ForeignKey, DateTime, Integer, String
from sqlalchemy.orm import relationship

from ...database import Base


class Text(Base):
    __tablename__ = "text"

    original_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    source = Column(String, unique=True, index=True)
    content = Column(String, unique=True, index=True)
    lang = Column(String, unique=True, index=True)
    content_creation_date = Column(DateTime(timezone=True), unique=True, index=True)
    id = Column(Integer, ForeignKey('search_results.text_id'))
    
    search = relationship("Search_Results")


    


