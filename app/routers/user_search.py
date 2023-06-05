from typing import List

from fastapi import APIRouter, Depends, responses

from sqlalchemy.orm import Session

from ..dependencies import get_db

from ..domain.user_search import service, schema
from ..domain.users import service as user_service



#Endpoint 
router = APIRouter(tags=["user_search"])


@router.get("/user_search/{user_id}")
async def get_user_searches_by_id(id: int, db: Session = Depends(get_db)):

    #Combrobar que el usuario existe vía id
    result = await user_service.get_user_by_id(db, id);

    if result is None:
        response = responses.JSONResponse(
            status_code=404,
            content={"message": "User not found"}
        )
        return response;

    else:
        saved_search = await service.get_user_searches_by_id(db, id);
        return saved_search;


@router.post("/user_search/save_search")
async def save_user_search(new_search: schema.SaveNewResult, db: Session = Depends(get_db)):

    #Combrobar que el usuario existe vía id
    result = await user_service.get_user_by_id(db, new_search.user_id);

    if result is None:
        response = responses.JSONResponse(
            status_code=404,
            content={"message": "User not found"}
        )
        return response;

    else:
        saved_search = await service.save_user_new_search(db, new_search);
        return saved_search;