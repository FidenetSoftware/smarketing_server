from sqlalchemy.orm import Session, joinedload
from . import models
from ..text import model as text_model

#Get the results by id
async def get_results_by_searchId(db: Session, id: int):
 
    query = db.query(models.Search_Results).options(joinedload(models.Search_Results.text))
    result = query.filter(models.Search_Results.search_id == id).first();
    return result;



 



