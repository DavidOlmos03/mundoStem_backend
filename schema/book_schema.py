from pydantic import BaseModel
from typing import Optional

class BookSchema(BaseModel):
    id: Optional[int]
    title: str
    authors: str
    language: str
    subject: str
    pages: int
    extension: str
    size: int
    summary: str