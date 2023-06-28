from sqlalchemy.orm import Session
from . import models, schemas
from typing import List
from ...hashing import Hasher


#Obtener los datos de todos los usuarios
async def get_users(db: Session) -> List[schemas.UserBase]:
    users = db.query(models.User).all()
    return users;


#Obtener los datos del usuario via correo electrónico
async def get_user_by_email(db: Session, email: str):
    user = db.query(models.User).filter(models.User.user_email == email).first();
    return user;


async def get_user_by_id(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first();
    return user;


#Creación de un nuevo usuario
async def create_user(db: Session, user: schemas.UserCreate):

    #Guardamos la contraseña de manera totalmente encriptada
    hashed_password = Hasher.get_password_hash(user.user_password)

    new_user = models.User(
        user_name = 'nombre',
        user_last_name = 'apellidos',
        user_rol = 'usuario',
        user_pricing_plan = 'genérico',
        user_username = 'nombre del usuario',
        user_email= user.user_email,
        user_password= hashed_password,
        user_profile_img_url = 'url',
        user_loged = True,
    );

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user;
  

#Inicio de sesión del usuario
async def get_user_by_email_and_password(db: Session, user: schemas.SignedUser):

    #Buscamos la contraseña del usuario que esta guardada en la base de datos
    hashed_password = db.query(models.User.user_password).filter(models.User.user_email == user.user_email).first()

    #Comprobamos que las dos contraseñas son iguales
    verify_password = Hasher.verify_password(user.user_password, hashed_password[0])

    if verify_password:
    
        signed_user = db.query(models.User).filter(models.User.user_email == user.user_email).first();

        #Cambiamos el estado del usuario a true
        signed_user.user_loged = True

        #Guardamos el cambio en la base de datos
        db.commit()
        db.refresh(signed_user)

        return signed_user;


#Cerrar la sesión del usuario
async def update_user(db: Session, email: str):

    #Buscamos el usuario mediante el email
    user = db.query(models.User).filter(models.User.user_email == email).first()

    #Cambiamos el estado a False
    user.user_loged = False

    #Guardamos el cambio en la base de datos
    db.commit()
    db.refresh(user)
    return user;


#Guardar la búsqueda que el usuario haya realizado
async def save_user_search(db: Session, email: str, search_id: int):

    user = db.query(models.User).filter(models.User.user_email == email).first();

    # Realizar la actualización en la base de datos
    user.search_id = search_id
    db.commit()
    db.refresh(user)

    return user;
