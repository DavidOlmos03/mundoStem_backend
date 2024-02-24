from sqlalchemy import Column, Integer, String, inspect, MetaData
from connection.connection import Base, engine




class book_model(Base):
    __tablename__ = 'mechanics_books'  # Nombre de la tabla en la base de datos
    id = Column(Integer, primary_key=True)
    title = Column(String(255),nullable = False)
    authors = Column(String(255), nullable=False)
    language = Column(String(255), nullable=False)
    subject = Column(String(255), nullable=False)
    pages = Column(Integer, nullable=True)
    extension = Column(String(255), nullable=True)
    size = Column(Integer, nullable=True)
    summary = Column(String(255), nullable=True)

    


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



