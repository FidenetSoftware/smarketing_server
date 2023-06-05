from sqlalchemy.orm import Query
from pydantic import BaseModel, validator
from datetime import datetime


class UserResultBase(BaseModel):
    id: int
    user_id: int
    search_id: int
    search_text: str
    created_at: datetime


class SaveNewResult(BaseModel):
    user_id: int
    search_id: int
    search_text: str













    