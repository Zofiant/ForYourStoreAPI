# from app.repository.base import BaseRepository
# from app.cart.models import Carts
# from sqlalchemy.ext.asyncio import AsyncSession
# from typing import List



# class CartRepository(BaseRepository):
#     model = Carts
#     async def get_by_user(self, user_id: int, session: AsyncSession):
#         return await session.query(self.model).filter(self.model.user_id == user_id).first()