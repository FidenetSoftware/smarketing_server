from sqlalchemy.orm import Query
from pydantic import BaseModel, validator
from datetime import datetime

#Importar la clase Search del esquema de search
from ..search import schemas



class OrmBase(BaseModel):
    # Common properties across orm models
    id: int

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

class YtCommentsBase(OrmBase):
    id: int
    kind: str
    video_id: str
    comment_thread_id: str
    text: str
    author: str
    author_channel_url: str
    likecount: int
    published_at: datetime
    updateat: datetime
    replycount: int
    replies: str









    