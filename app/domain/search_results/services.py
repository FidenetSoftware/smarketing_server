from sqlalchemy.orm import Session
from . import models
from ...hashing import Hasher

#Get the results by id
async def get_results_by_searchId(db: Session, id: int):
    result = db.query(models.Search_Results).filter(models.Search_Results.search_id == id).first();
    return result;
