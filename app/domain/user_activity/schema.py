from sqlalchemy.orm import Query
from pydantic import BaseModel, Json
from datetime import datetime


class UserResultBase(BaseModel):
    id: int
    user_id: int
    search_id: int
    activity_type: str
    activity_data: Json
    creation_date: datetime
    update_date: datetime


class SaveNewResult(BaseModel):
    user_id: int
    search_id: int
    activity_type: str
    activity_data: Json













    