from sqlalchemy import Column, DateTime, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from ...database import Base


class Tokenization(Base):
    __tablename__ = "tokenization"


    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text_id = Column(Integer, index=True, autoincrement=True)
    token = Column(String, unique=True, index=True)
    word = Column(String, unique=True, index=True)
    order_word = Column(Integer, index=True)
    creation_date = Column(DateTime(timezone=True), unique=True, index=True)
    update_date = Column(DateTime(timezone=True), unique=True, index=True)

