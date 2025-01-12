from app.database import async_session_maker

from app.products.models import Products
from app.repository.base import BaseRepository


class ProductRepository(BaseRepository):
    model = Products
    
    