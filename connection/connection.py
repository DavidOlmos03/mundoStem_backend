from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,MetaData
from sqlalchemy.orm import sessionmaker
from databases import Database


url = "mysql+mysqlconnector://root@localhost/p_trabajoudea"
engine = create_engine(url)
meta_data = MetaData()
Base = declarative_base()
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine) #ESTUDIAR
session = Session()
database = Database(url)

#Esta función permite crear una session en la base de datos para poder hacer querys en ella
"""def get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()

"""


