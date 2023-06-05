from typing import List

from fastapi import APIRouter, Depends, responses

from sqlalchemy.orm import Session

from ..dependencies import get_db

from ..domain.users import service, models, schemas



#Endpoint 
router = APIRouter(tags=["users"])


#Obtener todos los usuarios
@router.get("/users", response_model=List[schemas.UserBase])
async def get_all_users(db: Session = Depends(get_db)):

    users = await service.get_users(db);

    if users is None:
        response = responses.JSONResponse(
            status_code=404,
            content={"message": "Results not found"}
        )
        return response;

    return users;


#Obtener los datos de un usuario
@router.get("/users/{user_email}", response_model=schemas.UserBase)
async def get_user_by_email(user_email: str, db: Session = Depends(get_db)):

    user = await service.get_user_by_email(db, user_email);

    if user is None:
        response = responses.JSONResponse(
            status_code=404,
            content={"message": "User not found"}
        )
        return response;

    return user;


#Creación de un nuevo usuario
@router.post("/users/create", response_model=schemas.UserBase)
async def create_user(new_user: schemas.UserCreate, db: Session = Depends(get_db)):

    #Comprobar que el usuario no existe
    user = await service.get_user_by_email(db, new_user.user_email);

    if user:
        response = responses.JSONResponse(
            status_code=404,
            content={"message": "User already exists"}
        )
        return response;

    else:
        create_user = await service.create_user(db, new_user);
        return create_user;


#Inicio de sesión del usuario
@router.post("/users/sign-in", response_model=schemas.UserBase)
async def sign_in_user(user: schemas.SignedUser, db: Session = Depends(get_db)):

    #Combrobar que el usuario existe realmente
    result = await service.get_user_by_email_and_password(db, user);

    if result is None:
        response = responses.JSONResponse(
            status_code=404,
            content={"message": "User not found"}
        )
        return response;

    else:
        return result;
        


#Cerrar la sesión del usario
@router.patch("/users/sign-out", response_model= schemas.UserBase)
async def sign_out_user(user: schemas.UpdatedUser, db: Session = Depends(get_db)):

    #Combrobar que el usuario existe
    result = await service.get_user_by_email(db, user.user_email);

    if result is None:
        response = responses.JSONResponse(
            status_code=404,
            content={"message": "User not found"}
        )
        return response;

    else:
        updated_user = await service.update_user(db, user.user_email);
        return updated_user;

    

#Añadir el registro de la búsqueda que el usuario ha realizado
@router.patch("/users/save-search")
async def save_user_search(user: schemas.SaveSearch, db: Session = Depends(get_db)):

    #Combrobar que el usuario existe
    result = await service.get_user_by_email(db, user.user_email);

    if result is None:
        response = responses.JSONResponse(
            status_code=404,
            content={"message": "User not found"}
        )
        return response;

    else:
        updated_user = await service.save_user_search(db, user.user_email, user.search_id);
        return updated_user;



