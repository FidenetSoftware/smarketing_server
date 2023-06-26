from sqlalchemy import Text, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ...database import Base

class Twitch_Extraction(Base):

    __tablename__ = "twitch_extraction"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    stream_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_login = Column(String, unique=True, index=True)
    user_name = Column(String, unique=True, index=True)
    title = Column(Text, unique=True, index=True)
    description = Column(Text, unique=True, index=True)
    created_at = Column(DateTime(timezone=True), unique=True, index=True)
    published_at = Column(DateTime(timezone=True), unique=True, index=True)
    url = Column(Text, unique=True, index=True)
    thumbnail_url = Column(Text, unique=True, index=True)
    viewable = Column(String, unique=True, index=True)
    view_count = Column(Integer, index=True)
    language = Column(String, unique=True, index=True)
    type = Column(String, unique=True, index=True)
    duration = Column(String, unique=True, index=True)
    search_id = Column(ForeignKey('search.id'))

    twitch = relationship("Search", back_populates="twitch_searches")