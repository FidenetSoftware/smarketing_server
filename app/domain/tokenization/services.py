from sqlalchemy.orm import Session
from . import models
from ...utils import convert_to_json
import json


#Obtener los resultados de la tabla tokenization en base al text_id
async def get_data_by_textId(db: Session, id: int):

    result = db.query(models.Tokenization).filter(models.Tokenization.text_id == id).all();
    
    # Serialize the results using the custom conversion function
    results_json = json.dumps(result, default=lambda obj: convert_to_json(obj, ['id', 'text_id', 'token', 'word', 'order_word', 'creation_date', 'update_date']))

    # Cargar la cadena JSON en un objeto Python
    parsed_data = json.loads(results_json)

    return parsed_data