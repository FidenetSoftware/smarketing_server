from sqlalchemy import Text, Column, Integer, String, DateTime

from ...database import Base

class Ig_Extraction(Base):
    __tablename__ = "ig_extraction"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    caption_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    caption = Column(Text, unique=True, index=True)
    comments_count = Column(Integer, index=True)
    like_count = Column(Integer, index=True)
    media_product_type = Column(String, unique=True, index=True)
    media_url = Column(Text, unique=True, index=True)
    permalink = Column(Text, unique=True, index=True)
    timestamp = Column(DateTime(timezone=True), unique=True, index=True)
    hashtag = Column(String, unique=True, index=True)


    


