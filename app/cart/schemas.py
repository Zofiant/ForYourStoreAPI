

from typing import Optional
from pydantic import BaseModel, Field

from app.orders.models import Order_delivery

class SCart(BaseModel):
    cart_id: int
    user_id:int
    total_price: int | None = None

class SDelivery(BaseModel):
    order_delivery: Order_delivery
    address_courier: Optional[str] = Field(None, description="Address for courier delivery")
    address_pickup: Optional[str] = Field(None, description="Address for pickup delivery")