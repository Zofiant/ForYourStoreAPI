from fastapi import HTTPException
from app.cart.schemas import SDelivery
from app.orders.models import Order_delivery


async def validate_delivery(delivery_info: SDelivery) -> SDelivery:
    if delivery_info.order_delivery == Order_delivery.Courier:
        if not delivery_info.address_courier:
            raise HTTPException(status_code=400, detail="Courier delivery requires 'address_courier'.")
    elif delivery_info.order_delivery == Order_delivery.Self_pickup:
        if not delivery_info.address_pickup:
            raise HTTPException(status_code=400, detail="Pickup delivery requires 'address_pickup'.")
    else:
        raise HTTPException(status_code=400, detail="Invalid delivery type.")
    return delivery_info