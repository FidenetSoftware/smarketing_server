from sqlalchemy.orm import Session, joinedload
from datetime import datetime, timedelta
from . import models, schemas

from typing import List


#Get de las extracciones en base al search_id
async def get_tweet_by_searchId(db: Session, id: int):
    query = db.query(models.TW_Extraction)
    result = query.filter(models.TW_Extraction.search_id == id).all()
    tweet_texts = [row.tweet_created_at for row in result]
    return tweet_texts


   


#Obtener los resultados en base a la fecha:

#Último día
async def get_tweets_by_day(db:Session, id:int, num_days: int):
    
    # Obtener la fecha y hora actual
    current_date = datetime.now()

    # Calcular la fecha de inicio (hace 24 horas)
    start_date = current_date - timedelta(days=num_days)

    # Definir la fecha de fin como la fecha y hora actual
    end_date = current_date

    query = db.query(models.TW_Extraction.tweet_public_metrics, models.TW_Extraction.tweet_created_at).filter(
        models.TW_Extraction.tweet_created_at.between(start_date, end_date),
        models.TW_Extraction.search_id == id)
    results = query.all()
    return results

    #Última semana

    #Último mes

    #En un periodo de tiempo 

    #Último año


