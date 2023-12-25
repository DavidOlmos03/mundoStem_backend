from sqlalchemy import Column, Integer, String, Float
from connection.connection import Base

class product_model(Base):
    __tablename__ = 'producto'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255),nullable = False)
    precio = Column(Float, nullable=False)
    url_de_imagen = Column(String(255), nullable=False)

