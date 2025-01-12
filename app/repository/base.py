from app.database import async_session_maker

from sqlalchemy import select,insert, delete, update

class BaseRepository:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id = model_id)
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



# Might NOT WORK
    # @classmethod
    # async def delete(cls, id: int):
    #     async with async_session_maker() as session:
    #         query = delete(cls.model).where(cls.model.id == id)
    #         await session.execute(query)
    #         await session.commit()
    # @classmethod
    # async def update(cls, id: int, **data):
    #     async with async_session_maker() as session:
    #         query = (
    #             update(cls.model)
    #             .where(cls.model.id == id)
    #             .values(**data)
    #         )
    #         result = await session.execute(query)
    #         await session.commit()
    #         return result.rowcount
    # @classmethod
    # async def partial_update(cls, id: int, **data):
    #     async with async_session_maker() as session:
    #         query = (
    #             update(cls.model)
    #             .where(cls.model.id == id)
    #             .values(**{k: v for k, v in data.items() if hasattr(cls.model, k)})
    #         )
    #         result = await session.execute(query)
    #         await session.commit()
    #         return result.rowcount

            
            
    
    
            
            
            
