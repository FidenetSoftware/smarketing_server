from typing import List

from fastapi import APIRouter, Depends, responses

from sqlalchemy.orm import Session

from ..dependencies import get_db

from ..domain.sentiment_aws import service, schema


#Endpoint 
router = APIRouter(tags=["sentiment"])

@router.get("/sentiment/{text_id}", response_model=schema.GetSentiment)
async def get_sentiments_by_text_id(id: int, db: Session = Depends(get_db)):

    result = await service.get_sentiments_by_text_id(db, id)

    if not result: 
        response = responses.JSONResponse(
            status_code=404,
            content={"message": "Results not found"}
        )
        return response
    
    else:
        return result;