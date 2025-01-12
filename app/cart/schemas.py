

from pydantic import BaseModel

from app.cart.models import Cart_status

class SCart(BaseModel):
    cart_id: int
    user_id:int
    status:Cart_status
    total_price: int | None = None

