from sqlalchemy.orm import Session
from . import models
from ..text import model as text_model

#Get the results by id
async def get_results_by_searchId(db: Session, id: int):
 
    # Realizar la unión entre las tablas
    query = db.query(text_model.Text.content).join(models.Search_Results)
    result = query.filter(models.Search_Results.search_id == id).all();
    return result;

 



