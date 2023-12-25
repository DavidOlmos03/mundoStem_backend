from sqlalchemy import Column, Integer, String
from connection.connection import Base

class user_model(Base):
    __tablename__ = 'user'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True)
    full_name = Column(String(255),nullable = False)
    email_address = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)


"""
def __init__(self,id, nombre, email, contrase):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.contrase = contrase

    def __repr__(self):
        return f'usuarios({self.id}, {self.nombre}, {self.email},{self.contrase})'
    
    def __str__(self):
        return self.nombre

"""



