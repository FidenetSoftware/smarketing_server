from sqlalchemy.orm import Session, joinedload
from . import models, schemas
from ..search import models, schemas

from . import models, schemas



from typing import List


#Get de las extracciones en base al search_id
async def get_tweet_by_searchId(db: Session, id: int):
    query = db.query(models.TW_Extraction.tweet_text)
    result = query.filter(models.TW_Extraction.search_id == id).all()
    return result;

   


#Obtener los resultados en base a la fecha:

#Último día


    #Última semana

    #Último mes

    #En un periodo de tiempo 

    #Último año


