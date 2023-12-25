from fastapi import APIRouter
from connection.connection import session
from schema.compra_schema import compraSchema
from model.user import user_model
from model.product import product_model
from model.compra import compra_model
from sqlalchemy.exc import IntegrityError


compra = APIRouter()

##WORKING WHITH COMPRA
@compra.put("/api/update_compra/{id_user}/{id_producto}/{total_productos}")
def update_compra(data_buy: compraSchema):
    # Buscar el usuario y producto por su ID
    user = session.query(user_model).filter(user_model.id == data_buy.user_id).first()
    product = session.query(product_model).filter(product_model.id == data_buy.product_id).first()

    if user is None or product is None:
        return {"message": "Usuario o producto no encontrado"}
    
    try:
    # Crear una nueva instancia de Compra
        new_buy = compra_model(user_id=data_buy.user_id, product_id=data_buy.product_id, total_products = data_buy.total_products)
        # Guardar la compra en la base de datos
        session.add(new_buy)
        session.commit()
        session.refresh(new_buy)

        return {"message": "Buy created successfully"}
    #En caso de tener PK (compuesta) repetida (Error de integridad)
    except IntegrityError:
        session.rollback()
        return {"message": "Llave primaria ya existente. No se puede insertar el registro."}
    
