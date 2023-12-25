from pydantic import BaseModel
from typing import Optional

class productSchema(BaseModel):
    id: Optional[int]
    nombre: str
    precio: float
    url_de_imagen: str

class productSchemaNoId(BaseModel):
    nombre: str
    precio: float
    url_de_imagen: str