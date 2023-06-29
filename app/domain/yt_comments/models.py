from sqlalchemy import Text, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ...database import Base

class Yt_Comments(Base):

    __tablename__ = "yt_comments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    kind = Column(Text, unique=True, index=True)
    video_id = Column(String, unique=True, index=True)
    comment_thread_id = Column(Text, unique=True, index=True)
    text = Column(Text, unique=True, index=True)
    author = Column(Text, unique=True, index=True)
    author_channel_url = Column(Text, unique=True, index=True)
    likecount = Column(Integer, index=True)
    publishedat = Column(DateTime(timezone=True), unique=True, index=True)
    updatedat = Column(DateTime(timezone=True), unique=True, index=True)
    replycount = Column(Integer, index=True)
    replies = Column(Text, unique=True, index=True)

    