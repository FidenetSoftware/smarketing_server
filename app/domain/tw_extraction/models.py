from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ...database import Base


class  TW_Extraction(Base):
    __tablename__ = "tw_extraction"

    tweet_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tweet_text = Column(String, unique=True, index=True)
    tweet_created_at = Column(DateTime(timezone=True), unique=True, index=True)
    tweet_public_metrics = Column(String, unique=True, index=True)
    tweet_attachments = Column(String, unique=True, index=True)
    tweet_entities = Column(String, unique=True, index=True)
    tweet_geo = Column(String, unique=True, index=True)
    tweet_lang = Column(String, unique=True, index=True)
    tweet_author_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True, index=True)
    user_username = Column(String, unique=True, index=True)
    user_created_at = Column(DateTime(timezone=True), unique=True, index=True)
    user_public_metrics = Column(String, unique=True, index=True)
    user_description = Column(String, unique=True, index=True)
    user_entities = Column(String, unique=True, index=True)
    user_location = Column(String, unique=True, index=True)
    user_profile_image_url = Column(String, unique=True, index=True)
    user_url = Column(String, unique=True, index=True)
    user_verified = Column(String, unique=True, index=True)
    search_id = Column(Integer, ForeignKey('search.id'))
    search = relationship("Search")
