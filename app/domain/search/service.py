from sqlalchemy.orm import Session
from . import models, schemas
from typing import List
from ...hashing import Hasher


#Obtener los datos en base a la palabra
async def get_search_by_content(db: Session, string: str):
    result = db.query(models.Search).filter(models.Search.content.ilike(f'%{string}%')).all()
    return result;

