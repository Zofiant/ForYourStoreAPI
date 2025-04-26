from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import DB_HOST, DB_PORT, DB_NAME, DB_PASS, DB_USER

# Формируем строку подключения к базе данных PostgreSQL с использованием асинхронного драйвера asyncpg
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Создаем асинхронный движок SQLAlchemy для работы с базой данных
engine = create_async_engine(DATABASE_URL)

# Создаем фабрику сессий для асинхронного взаимодействия с базой данных
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Определяем базовый класс для декларативного определения моделей
class Base(DeclarativeBase):
    """Базовый класс для декларативного определения моделей SQLAlchemy.

    Все модели базы данных должны наследоваться от этого класса.
    Это позволяет SQLAlchemy автоматически создавать таблицы и управлять ими.
    """
    pass
