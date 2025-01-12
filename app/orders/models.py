from sqlalchemy import JSON, Column, Integer, String, ForeignKey, Time, Enum
from app.database import Base

import enum


class Order_status(enum.Enum):
    Placed = 1
    Processing = 2
    Shipped = 3
    Delivered = 4 
    Canceled = 5
    

class Orders(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key = True)
    user_id = Column(ForeignKey("users.user_id"))
    made_in = Column(Time,nullable=False)
    status = Column(Enum(Order_status))
    total_price = Column(Integer)

