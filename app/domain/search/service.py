from sqlalchemy.orm import Session
from . import models, schemas
from typing import List
from ...hashing import Hasher


#Obtener los datos en base a la palabra
async def get_searchs(db: Session, search: str):
    user = db.query(models.Search).filter(models.Search.content == search).first();
    return user;