from fastapi import APIRouter,HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from connection.connection import session
from schema.user_schema import UserSchema
from model.user import user_model
from passlib.hash import bcrypt_sha256 ##de cifrado mas seguro 
#from fastapi.exceptions import HTTPException
from flask import Flask, redirect
import webbrowser
"""
    De prueba para generar los tokens 
"""
from fastapi import FastAPI, Depends, HTTPException, status
from jose import JWTError,jwt



user = APIRouter()

                            ###***CRUD TABLE USUARIOS***###
"""
@user.get("/api/show_table_usuarios",, tags=["CRUD USER"])
def get_users():
    result =  session.query(user_model).all()
    return jsonable_encoder(result)

"""                            


@user.post("/api/Create_user", tags=["CrudUser"])
def create_user(data_user: UserSchema):
    existing_user = session.query(user_model).filter_by(id=data_user.id).first()
    if existing_user:
        session.commit()
        raise HTTPException(status_code=400, detail=f"User {data_user.id} aleready exists")
    new_user = user_model(id = data_user.id, full_name=data_user.full_name, email_address=data_user.email_address, password=data_user.password)
    new_user.password = bcrypt_sha256.hash(new_user.password)
    session.add(new_user)
    session.commit()
    #session.refresh(new_user)   
    return new_user

@user.get("/api/read_user_by_id/{user_id}", tags=["CrudUser"])
def get_users(id: int):
    user = session.query(user_model).get(id)
    if not user:
        raise HTTPException(404,f"User {id} not found")
    return user

@user.put("/api/update_users/{user_id}", tags=["CrudUser"])
def update_user(data_update: UserSchema , user_id: int):
    db_usuario = session.query(user_model).filter(user_model.id == user_id).first()
    if db_usuario:
        # Actualiza los atributos del usuario con los valores proporcionados en usuario_actualizado
        for key, value in data_update.dict().items():
            setattr(db_usuario, key, value)
        session.commit()
        session.refresh(db_usuario)
        return {"message": "User updated successfully"}
    session.commit()
    raise HTTPException(404, f"Id {user_id} not found")


@user.delete("/api/delete_user/{user_id}", tags=["CrudUser"])
def delete_user(user_id: int):
    db_usuario = session.query(user_model).filter(user_model.id == user_id).first()

    if db_usuario:
        session.delete(db_usuario)
        session.commit()
        return {"message": "User deleted successfully"}
    session.commit()
    raise HTTPException(404, f"id {user_id} not found")


"""
@user.get("/api/read_user_by_email/{user_email}", tags=["CrudUser"])
def get_user_by_email(user_email: str, user_password:str):
    user = session.query(user_model).filter_by(email_address = user_email).first()
    
    if not user:
        raise HTTPException(404,f"User with {user_email} not found")
    
    stored_hash = user.password;
    password_matched = bcrypt_sha256.verify(user_password, stored_hash)

    if not password_matched:
        raise HTTPException(401, "Invalid password")
    
    return user
"""
@user.post("/api/read_user_by_email", tags=["CrudUser"])
def get_user_by_email(user_data: dict):
    user_email = user_data.get("email_address", "")
    user_password = user_data.get("password", "")

    user = session.query(user_model).filter_by(email_address=user_email).first()
    
    if not user:    #Si el usuario no es encontrado en la base de datos se envia el error correspondiente
        raise HTTPException(404, f"User with {user_email} not found")
    
    stored_hash = user.password #Se accede al hash que está en la DB
    password_matched = bcrypt_sha256.verify(user_password, stored_hash) #Se verifica el hash

    if not password_matched:
        raise HTTPException(401, "Invalid password")
    #En caso de que los datos se hayan ingresado correctamente se pocede a retornar el user
    #session['acceso'] = True
    
    
    return user


"""
    Prueba para la generación de tokens
"""
# Configuración de seguridad
SECRET_KEY = "mundoSteam"  # Cambiar por una clave secreta segura
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict):
    to_encode = data.copy()   
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Rutas de autenticación
@user.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    #Primero se verifica que el usuario y la contraseña coinsidan con los datos ingresados
    userAutenticated = get_user_by_email({"email_address": form_data.username, "password": form_data.password})
    
    if not userAutenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email address or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    """
        Una vez el usuario es verificado en la base de datos, se procede a generar el token de acceso
    """
    access_token = create_access_token(
        data={"sub": userAutenticated.email_address}
    )
    return {"access_token": access_token, "token_type": "bearer"}


@user.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email_address: str = payload.get("sub")
        if email_address is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return {"email_address": email_address}
