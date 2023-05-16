from typing import List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from ..dependencies import get_db

from ..domain.users import service, models, schemas

from urllib.parse import unquote

#Endpoint 
router = APIRouter(tags=["users"])

#Obtener los datos del usuario
# @router.get("/users/{user_email}", response_model=schemas.User)
# def get_user_by_email(user_email: str, db: Session = Depends(get_db)):
 
#     email= unquote(user_email)
#     db_user = service.get_user_by_email(db, user_email=email)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


#Obtener todos los usuarios
@router.get("/users", response_model=List[schemas.UserBase])
def get_all_users(db: Session = Depends(get_db)):
    users = service.get_users(db)
    return users
