from datetime import datetime
from fastapi import Depends, HTTPException
from sqlalchemy import Insert, delete, select, update
from app.cart_item.models import Cart_items
from app.database import async_session_maker

from app.cart.models import Carts
from app.orders.models import Order_status, Orders
from app.orders_item.models import Order_items
from app.products.models import Products
from app.repository.base import BaseRepository
from app.users.dependencies import get_current_user
from app.users.models import Users


class CartRepository(BaseRepository):
    
    

             
    
    @staticmethod
    async def get_user_cart_id(user_id):
        async with async_session_maker() as session: 
            query = select(Carts.cart_id).where(Carts.user_id == user_id)
            result = await session.execute(query)
            cart_id = result.scalar()
            return cart_id
        

    @staticmethod
    async def get_cart(user_id):
        async with async_session_maker() as session:       
            cart_id = await CartRepository.get_user_cart_id(user_id)
            
            query = select(Cart_items).filter_by(cart_id = cart_id)
            result = await session.execute(query)
            return result.scalars().all()
            
    
    @staticmethod 
    async def add(product_id, quantity, user_id):
        async with async_session_maker() as session:
            cart_id = await CartRepository.get_user_cart_id(user_id)
            
            
            query = (
                Insert(Cart_items).values(
                    cart_id=int(cart_id),
                    product_id=int(product_id),
                    quantity=int(quantity)
                )
            )
            await session.execute(query)
            await session.commit()
    
                
    @staticmethod 
    async def create_order(address, delivery_type,user_id):
        async with async_session_maker() as session:
            cart_id = await CartRepository.get_user_cart_id(user_id)
            
            cart_items = await CartRepository.get_cart(user_id)
            if not cart_items:
                raise HTTPException(status_code=400, detail="Cart is empty") 
            new_order = Orders(
                user_id=user_id,
                made_in=datetime.utcnow(),
                status=Order_status.Placed
            )
            new_order_data = {
                "user_id": new_order.user_id,
                "made_in": new_order.made_in,
                "status": new_order.status,
                "order_delivery": delivery_type,
                "address": address
            }
            query_new_order = Insert(Orders).values(new_order_data)
            result = await session.execute(query_new_order)
            new_order_id = result.inserted_primary_key[0]
            
            for item in cart_items:
                new_order_item_data = {
                    "order_id": new_order_id,
                    "product_id": item.product_id,
                    "quantity": item.quantity,
                }
                query_add_order_item = Insert(Order_items).values(new_order_item_data)
                await session.execute(query_add_order_item)
            
            await session.commit()
            
            
           
    @staticmethod 
    async def delete_item_one(cart_item_id, user_id):
        async with async_session_maker() as session:
            cart_id = await CartRepository.get_user_cart_id(user_id)
            subquery = select(Cart_items.quantity).filter_by(cart_item_id = cart_item_id)
            subquery_res = await session.execute(subquery)
            subquery_res = subquery_res.scalars().one()
            if subquery_res == 1:
                return await CartRepository.delete_item_all(cart_item_id,user_id)
                
                   
            query = update(Cart_items).values(quantity = subquery_res - 1).filter_by(
                cart_id = cart_id, 
                cart_item_id = cart_item_id
                )
            await session.execute(query)
            await session.commit()       
           
                
    @staticmethod 
    async def delete_item_all(cart_item_id, user_id):
        async with async_session_maker() as session:
            cart_id = await CartRepository.get_user_cart_id(user_id)
            
            query = delete(Cart_items).filter_by(
                cart_id = cart_id, 
                cart_item_id = cart_item_id
                )
            await session.execute(query)
            await session.commit()

    @staticmethod
    async def clear_cart(user_id):
        async with async_session_maker() as session:
            cart_id = await CartRepository.get_user_cart_id(user_id)

            query = delete(Cart_items).filter_by(cart_id = cart_id)

            await session.execute(query)
            await session.commit()



