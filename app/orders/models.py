from sqlalchemy import Column, Integer, String, ForeignKey, Time, Enum
from app.database import Base

import enum


class Order_status(enum.Enum):
    Placed = "Placed"
    Processing = "Processing"
    Shipped = "Shipped"
    Delivered = "Delivered"
    Canceled = "Canceled"
    
class Order_delivery(enum.Enum):
    Courier = "Courier"
    Self_pickup = "Self_pickup"

class Orders(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key = True)
    user_id = Column(ForeignKey("users.user_id"))
    made_in = Column(Time,nullable=False)
    status = Column(Enum(Order_status))
    order_delivery = Column(Enum(Order_delivery))
    address = Column(String)


