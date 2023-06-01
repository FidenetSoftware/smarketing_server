from typing import List

from fastapi import APIRouter, Depends, responses

from sqlalchemy.orm import Session

from ..dependencies import get_db

from ..domain.search import service, schemas



#Endpoint 
router = APIRouter(tags=["search"])

@router.get("/search/{string}", response_model=List[schemas.SearchBase])
async def get_data_by_date(string: str, db: Session = Depends(get_db)):

    #Búsqueda en la tabla search en base al contenido
    result = await service.get_search_by_content(db, string);

    if result == [] or None:
        response = responses.JSONResponse(
            status_code=404,
            content={"message": "Results not found"}
        )
        return response;

    #Búsqueda de los resultados en base a search_id
  
    return result;


