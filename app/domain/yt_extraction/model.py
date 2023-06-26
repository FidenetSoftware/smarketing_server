from sqlalchemy import Text, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ...database import Base

class YT_Extraction(Base):

    __tablename__ = "yt_extraction"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    video_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    kind = Column(String, unique=True, index=True)
    publishedat = Column(DateTime(timezone=True), unique=True, index=True)
    channelid = Column(String, unique=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(Text, unique=True, index=True)
    thumbnails = Column(Text, unique=True, index=True)
    channeltitle = Column(String, unique=True, index=True)
    tags = Column(Text, unique=True, index=True)
    category_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    defaultlanguage = Column(String, unique=True, index=True)
    defaultaudiolanguage = Column(String, unique=True, index=True)
    viewcount = Column(Integer, index=True)
    likecount = Column(Integer, index=True)
    favoritecount = Column(Integer, index=True)
    commentcount = Column(Integer, index=True)
    search_id = Column(ForeignKey('search.id'))

    youtube = relationship("Search", back_populates="youtube_searches")
