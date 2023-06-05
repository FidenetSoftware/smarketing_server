from sqlalchemy.orm import Session
from . import model, schema



#Método GET para obtener los registros de la tabla vía el id del usuario
async def get_user_searches_by_id(db: Session, id: int):
    user_searches = db.query(model.UserSearch).filter(model.UserSearch.user_id == id).all()
    return user_searches;

#Metodo POST para poder realizar una nueva búsqueda
async def save_user_new_search(db: Session, user: schema.SaveNewResult):

    user_search = model.UserSearch(
        user_id = user.user_id,
        search_id = user.search_id, 
        search_text = user.search_text
    )

    result = db.add(user_search)
    db.commit()
    
    return result;
