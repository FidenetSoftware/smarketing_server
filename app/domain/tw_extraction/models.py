from sqlalchemy import Text, Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship

from ...database import Base


class TW_Extraction(Base):
    __tablename__ = "tw_extraction"

    tweet_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tweet_text = Column(Text, unique=True, index=True)
    tweet_created_at = Column(DateTime(timezone=True), unique=True, index=True)
    tweet_public_metrics = Column(Text, unique=True, index=True)
    tweet_attachments = Column(Text, unique=True, index=True)
    tweet_entities = Column(Text, unique=True, index=True)
    tweet_geo = Column(Text, unique=True, index=True)
    tweet_lang = Column(Text, unique=True, index=True)
    tweet_author_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(Text, unique=True, index=True)
    user_username = Column(Text, unique=True, index=True)
    user_created_at = Column(DateTime(timezone=True), unique=True, index=True)
    user_public_metrics = Column(Text, unique=True, index=True)
    user_description = Column(Text, unique=True, index=True)
    user_entities = Column(Text, unique=True, index=True)
    user_location = Column(Text, unique=True, index=True)
    user_profile_image_url = Column(Text, unique=True, index=True)
    user_url = Column(Text, unique=True, index=True)
    user_verified = Column(Text, unique=True, index=True)
    search_id = Column(ForeignKey('search.id'))
    
    search = relationship("Search", back_populates="tweet_searches")
