from sqlalchemy.orm import Session
from . import models
from ...hashing import Hasher


#Obtener los datos en base a la palabra
async def get_search_by_content(db: Session, string: str):
    result = db.query(models.Search.id).filter(models.Search.content.ilike(f'%{string}%')).all()
    return result;

