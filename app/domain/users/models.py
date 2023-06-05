from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ...database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_name = Column(String, unique=True, index=True)
    user_last_name = Column(String, unique=True, index=True)
    user_rol = Column(String, unique=True, index=True)
    user_pricing_plan = Column(String, unique=True, index=True)
    user_username = Column(String, unique=True, index=True)
    user_email = Column(String, unique=True, index=True)
    user_password = Column(String, unique=True, index=True)
    user_profile_img_url = Column(String, unique=True, index=True)
    user_loged = Column(Boolean, default=True)
    



    


