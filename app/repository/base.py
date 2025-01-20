from app.database import async_session_maker

from sqlalchemy import select,insert, delete, update

class BaseRepository:
    model = None

    @classmethod
    async def find_by_id(cls, user_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(user_id = user_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
        
    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls,limit: int = 10, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by).limit(limit)
            result = await session.execute(query)
            return result.mappings().all()
        
    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, **filter_by):
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()


            
            
    
    
            
            
            
