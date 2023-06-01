from sqlalchemy.orm import Session
from . import models
from ..search import models as search_model

#Get the results by id
async def get_results_by_searchId(db: Session, id: int):
 
    # Realizar la unión entre las tablas
    join = db.query(models.Search_Results).join(search_model.Search);
    result = join.filter(models.Search_Results.search_id == id).all()
    return result;



