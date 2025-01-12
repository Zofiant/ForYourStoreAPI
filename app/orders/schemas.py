
from datetime import time
from pydantic import BaseModel

from app.orders.models import Order_status

class SOrder(BaseModel):

    order_id : int
    user_id : int 
    made_in : time
    status : Order_status
    total_price : int | None = None
