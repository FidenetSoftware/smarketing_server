from typing import List

from fastapi import APIRouter, Depends, responses

from sqlalchemy.orm import Session

from ..dependencies import get_db

from ..domain.search import service, schemas
from ..domain.search_results import services as results_service, schemas as result_schema




#Endpoint 
router = APIRouter(tags=["search"])

@router.get("/search/{string}")
async def get_search_by_content(string: str, db: Session = Depends(get_db)):
    # Búsqueda en la tabla search en base al contenido
    search_ids = await service.get_search_by_content(db, string)

    if not search_ids:
        response = responses.JSONResponse(
            status_code=404,
            content={"message": "Results not found"}
        )
        return response

    result_list = search_ids
    result_variable = result_list[0][0]

    # Búsqueda de los resultados en base a search_id
    results = await results_service.get_results_by_searchId(db, result_variable)
    return results;



