from sqlalchemy import REAL, Column, ForeignKey, DateTime, Integer
from sqlalchemy.orm import relationship

from ...database import Base

class Sentiment(Base):
    __tablename__ = 'sentiment'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text_id = Column(Integer)
    positive_score = Column(REAL)
    neutral_score = Column(REAL)
    negative_score = Column(REAL)
    creation_date = Column(DateTime(timezone=True), unique=True, index=True)
    update_date = Column(DateTime(timezone=True), unique=True, index=True)
