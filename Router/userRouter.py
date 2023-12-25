from fastapi import APIRouter
from connection.connection import session
from schema.user_schema import UserSchema
from model.user import user_model
from passlib.hash import bcrypt_sha256 ##de cifrado mas seguro 
from fastapi.exceptions import HTTPException


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
    new_user = user_model(id = data_user.id, nombre=data_user.nombre, email=data_user.email, contrase=data_user.contrase)
    new_user.contrase = bcrypt_sha256.hash(new_user.contrase)
    session.add(new_user)
    session.commit()
    #session.refresh(new_user)   
    return new_user

@user.get("/api/read_user/{user_id}", tags=["CrudUser"])
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
