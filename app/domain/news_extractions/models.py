from sqlalchemy import Text, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ...database import Base

class News_Extraction(Base):
    __tablename__ = "news_extractions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    news_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    news_date = Column(DateTime(timezone=True), unique=True, index=True)
    title = Column(String, unique=True, index=True)
    excerpt = Column(Text, unique=True, index=True)
    summary = Column(Text, unique=True, index=True)
    author = Column(String, unique=True, index=True)
    link = Column(String, unique=True, index=True)
    clean_url = Column(String, unique=True, index=True)
    media = Column(Text, unique=True, index=True)
    raw_data = Column(Text, unique=True, index=True)    
    search_id = Column(ForeignKey('search.id'))



    news = relationship("Search", back_populates="news_searches")