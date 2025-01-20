from app.cart.models import Carts
from app.repository.base import BaseRepository
from app.users.models import Users
from sqlalchemy import insert, select
from app.database import async_session_maker

class UserRepository(BaseRepository):
    model = Users
    
        

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            result = await session.execute(query)
            new_user_id = result.inserted_primary_key[0]
            
            # # Получаем созданного пользователя для возврата дополнительных данных
            # stmt = select(cls.model).where(cls.model.id == new_user_id)
            # new_user = await session.execute(stmt)
            # new_user = new_user.scalar_one()
            
            await session.commit()
            return new_user_id
    @staticmethod
    async def add_new_cart(user_id):
        async with async_session_maker() as session:
            query = insert(Carts).values(user_id = user_id)
            await session.execute(query)
            await session.commit()
        
        
