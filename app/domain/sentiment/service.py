from sqlalchemy.orm import Session
from . import model
from ...utils import calculatePercentage

#Get the sentiment table's data by text_id
async def get_sentiments_by_text_id(db: Session, id: int):
    result = db.query(model.Sentiment).filter(model.Sentiment.text_id == id).first();

    #Calculamos los porcentajes de los tres sentimientos
    result.neutral_score_percentage = calculatePercentage(result.neutral_score)
    result.positive_score_percentage = calculatePercentage(result.positive_score)
    result.negative_score_percentage = calculatePercentage(result.negative_score)

    return result;



