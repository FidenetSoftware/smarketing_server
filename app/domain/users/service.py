from sqlalchemy.orm import Session
from . import models, schemas


#Obtener los datos del usuario
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.user_email == email).first()

#Obtener los datos de todos los usuarios
def get_users(db: Session):
    return db.query(models.User).all();

#Creación de un nuevo usuario
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.user_email, password=user.user_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user;


#Inicio de sesión del usuario
def get_user_by_email_and_password(db: Session, user: schemas.User ):
    return db.query(models.User).filter(email=user.user_email, password=user.user_password).first()

#Cerrar la sesión del usuario
def update_user(db: Session, email: str ):
    update_user = db.update().where(models.User.user_email == email).values(user_loged = False);
    db.execute(update_user)
    db.commit();
    return update_user;


#Borrar el usuario
def delete_user_by_email(db: Session, email: str ):
    return db.delete(models.User).where(models.User.user_email == email);
