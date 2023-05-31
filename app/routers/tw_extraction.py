from typing import List

from fastapi import APIRouter, Depends, responses

from sqlalchemy.orm import Session

from ..dependencies import get_db

from ..domain.tw_extraction import service, models, schemas



#Endpoint 
router = APIRouter(tags=["tw_extraction"])

@router.get("/tw_extraction/date", response_model=List[schemas.TwExtractionBase])
async def get_data_by_date(db: Session = Depends(get_db)):

    result = await service.get_results_by_date(db);

    if result is None:
        response = responses.JSONResponse(
            status_code=404,
            content={"message": "Results not found"}
        )
        return response;

    return result;