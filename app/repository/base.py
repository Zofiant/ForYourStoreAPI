from app.database import async_session_maker
from sqlalchemy import select, insert, delete, update

class BaseRepository:
    model = None  # Модель, с которой будет работать репозиторий

    @classmethod
    async def find_by_id(cls, user_id: int):
        """Находит запись по идентификатору пользователя."""
        async with async_session_maker() as session:  # Создаем асинхронную сессию
            query = select(cls.model).filter_by(user_id=user_id)  # Формируем запрос для поиска по user_id
            result = await session.execute(query)  # Выполняем запрос
            return result.scalar_one_or_none()  # Возвращаем единственную запись или None, если не найдено
        
    @classmethod
    async def find_one_or_none(cls, **filter_by):
        """Находит одну запись по заданным фильтрам."""
        async with async_session_maker() as session:  # Создаем асинхронную сессию
            query = select(cls.model).filter_by(**filter_by)  # Формируем запрос с фильтрами
            result = await session.execute(query)  # Выполняем запрос
            return result.scalar_one_or_none()  # Возвращаем единственную запись или None, если не найдено

    @classmethod
    async def find_all(cls, limit: int = 10, **filter_by):
        """Находит все записи с заданными фильтрами и ограничением по количеству."""
        async with async_session_maker() as session:  # Создаем асинхронную сессию
            query = select(cls.model).filter_by(**filter_by).limit(limit)  # Формируем запрос с фильтрами и лимитом
            result = await session.execute(query)  # Выполняем запрос
            return result.mappings().all()  # Возвращаем все найденные записи в виде списка
        
    @classmethod
    async def add(cls, **data):
        """Добавляет новую запись в базу данных."""
        async with async_session_maker() as session:  # Создаем асинхронную сессию
            query = insert(cls.model).values(**data)  # Формируем запрос на вставку с данными
            await session.execute(query)  # Выполняем запрос
            await session.commit()  # Подтверждаем изменения в базе данных

    @classmethod
    async def delete(cls, **filter_by):
        """Удаляет записи из базы данных по заданным фильтрам."""
        async with async_session_maker() as session:  # Создаем асинхронную сессию
            query = delete(cls.model).filter_by(**filter_by)  # Формируем запрос на удаление с фильтрами
            await session.execute(query)  # Выполняем запрос
            await session.commit()  # Подтверждаем изменения в базе данных
