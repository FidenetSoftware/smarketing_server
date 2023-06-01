from typing import List

from fastapi import APIRouter, Depends, responses

from sqlalchemy.orm import Session

from ..dependencies import get_db

from ..domain.search import service, models, schemas



#Endpoint 
router = APIRouter(tags=["search"])

@router.get("/search/{string}", response_model=List[schemas.SearchBase])
async def get_data_by_date(string: str, db: Session = Depends(get_db)):

    result = await service.get_search_by_content(db, string);

    if result == [] or None:
        response = responses.JSONResponse(
            status_code=404,
            content={"message": "Results not found"}
        )
        return response;

    return result;


