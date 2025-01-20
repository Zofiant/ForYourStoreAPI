from sqlalchemy import insert, select, text, update
from app.orders.models import Orders
from app.orders_item.models import Order_items
from app.repository.base import BaseRepository
from app.database import async_session_maker

class OrderRepository(BaseRepository):
    model = Orders
    
    @classmethod
    async def update(cls,new_status: str, order_id : int ):
        async with async_session_maker() as session:
            
            # query = text("UPDATE Orders SET status=:status WHERE order_id =: order_id ")
            # query = query.bindparams(status = new_status, order_id = order_id)
            # doesn't work dont know why 
            
            # this one works, life's good
            query = (
                update(cls.model).values(status = new_status)
                .filter_by(order_id = order_id)
            )
             
            await session.execute(query)
            await session.commit()
            
    @staticmethod
    async def get_order( user_id):
        async with async_session_maker() as session:
            query = select(Orders).filter_by(user_id = user_id)
            result = await session.execute(query)
            return result.mappings().all()
        
    @staticmethod
    async def get_order_items(user_id):
        async with async_session_maker() as session:
            subquery = select(Orders.order_id).filter_by(user_id = user_id)
            order_ids = await session.execute(subquery)
            order_ids = [order[0] for order in order_ids.all()]  

           
            query = select(Order_items).filter(Order_items.order_id.in_(order_ids))
            result = await session.execute(query)
            return result.mappings().all()
