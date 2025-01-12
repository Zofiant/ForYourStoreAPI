from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from app.orders.models import Order_status, Orders
from app.orders_item.models import Order_items
from app.users.models import Users
from app.orders.schemas import SOrder
from app.orders_item.schemas import SOrderItem
from datetime import time
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(
    prefix="/order",
    tags=["Заказы"],
)
