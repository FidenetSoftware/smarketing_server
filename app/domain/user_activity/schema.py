from sqlalchemy.orm import Query
from pydantic import BaseModel
from typing import Any, Dict
from datetime import datetime

class ActivityData(BaseModel):
    search_text: str


class UserActivitySearchBase(BaseModel):
    id: int
    user_id: int
    search_id: int
    activity_type: str
    activity_data: ActivityData
    creation_date: datetime
    update_date: datetime


class SaveNewResult(BaseModel):
    user_id: int
    search_id: int
    activity_type: str
    activity_data: ActivityData














    