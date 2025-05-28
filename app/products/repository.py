from sqlalchemy import Null, delete, update
from app.database import async_session_maker

from app.products.models import Products
from app.repository.base import BaseRepository


class ProductRepository(BaseRepository):
    model = Products
    
    @classmethod 
    async def delete_product(cls, product_id):
        async with async_session_maker() as session:
            search = await ProductRepository.find_one_or_none(product_id = product_id)
            if search is None:
                return "Продукт не найден"
                 
                        
            query = delete(cls.model).filter_by(product_id = product_id)
            await session.execute(query)
            await session.commit()
            return f"Продукт {product_id} успешно удален"
    
    @classmethod
    async def update_product(cls,product_id, **data):
        async with async_session_maker() as session:
            search = await ProductRepository.find_one_or_none(product_id = product_id)
            if search is None:
                return "Продукт не найден"
            
            
            query = (
                update(cls.model)
                .values(**data).filter_by(product_id = product_id) # Обновляем все поля из словаря
            )
            result = await session.execute(query)
            
            await session.commit()
            return f"Продукт {product_id} успешно обновлен"