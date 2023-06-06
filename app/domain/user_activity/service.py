from sqlalchemy.orm import Session
from . import model, schema



#Método GET para obtener los registros de la tabla vía el id del usuario
async def get_user_searches_by_id(db: Session, id: int):
    user_searches = db.query(model.UserActivity).filter(model.UserActivity.user_id == id).all()
    return user_searches;

async def save_user_new_search(db: Session, user: schema.SaveNewResult):

    activity_data_dict = user.activity_data.dict()  # Convertir el objeto ActivityData a un diccionario

    user_activity = model.UserActivity(
        user_id=user.user_id,
        search_id=user.search_id, 
        activity_type=user.activity_type,
        activity_data=activity_data_dict  # Asignar el diccionario de activity_data
    )

    result = db.add(user_activity)
    db.commit()

    return result

