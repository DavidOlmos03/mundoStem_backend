from pydantic import BaseModel
from typing import Optional

class compraSchema(BaseModel):
    user_id: Optional[int]
    product_id: Optional[int]
    total_products: Optional[int]  