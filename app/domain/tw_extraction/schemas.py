from sqlalchemy.orm import Query
from pydantic import BaseModel, validator
from datetime import datetime
#Importar la clase Search del esquema de search


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

class TwExtractionBase(OrmBase):
    tweet_id: int
    tweet_text: str
    tweet_created_at: datetime
    tweet_public_metrics: str
    tweet_attachments: str
    tweet_entities: str
    tweet_geo: str
    tweet_lang: str
    tweet_author_id: int
    user_id: int
    user_username: str
    user_created_at: datetime
    user_public_metrics: str
    user_description: str
    user_entities: str
    user_location: str
    user_profile_image_url: str
    user_url: str
    user_verified: str
    # search_id: Search









    