from sqlalchemy.orm import Query
from pydantic import BaseModel, validator
from datetime import datetime

class OrmBase(BaseModel):
    # Common properties across orm models

    # Pre-processing validator that evaluates lazy relationships before any other validation
    # NOTE: If high throughput/performance is a concern, you can/should probably apply
    #       this validator in a more targeted fashion instead of a wildcard in a base class.
    #       This approach is by no means slow, but adds a minor amount of overhead for every field
    @validator("*", pre=True)
    def evaluate_lazy_columns(cls, v):
        if isinstance(v, Query):
            return v.all()
        return v

    class Config:
        orm_mode = True

class SentimentBase(OrmBase):
    id: int
    text_id: str
    positive_score: float
    neutral_score: float
    negative_score: float
    mixed_score: float
    creation_date: datetime
    update_date: datetime
   

class GetSentiment(OrmBase):
    id: int
    text_id: str
    positive_score_percentage: str
    neutral_score_percentage: str
    negative_score_percentage: str
    


