from fastapi import HTTPException
from sqlalchemy import select
from app.orders.models import Order_status, Orders
from app.orders.schemas import SOrder
from app.orders_item.models import Order_items
from app.repository.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession


class OrderRepository(BaseRepository):
    model = Orders
    

    