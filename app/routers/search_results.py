from typing import List

from fastapi import APIRouter, Depends, responses

from sqlalchemy.orm import Session

from ..dependencies import get_db

from ..domain.search_results import services, models, schemas



#Endpoint 
router = APIRouter(tags=["search_results"])

@router.get("/search_results/{id}", response_model= schemas.ResultsBase)
async def get_results_by_searchId(id: int, db: Session = Depends(get_db)):

    result = await services.get_results_by_searchId(db, id)

    if result is None:
        response = responses.JSONResponse(
            status_code=404,
            content={"message": "Results not found"}
        )
        return response;
    
    return result;