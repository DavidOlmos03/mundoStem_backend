from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[int]
    full_name: str
    email_address: str
    password: str