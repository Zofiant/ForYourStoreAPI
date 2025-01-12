from app.repository.base import BaseRepository

from app.cart.models import Carts

class CartService(BaseRepository):
    model = Carts
    