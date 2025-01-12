from sqlalchemy import JSON, Column, Integer, String, ForeignKey, Time, Enum
from app.database import Base
import enum


class Cart_status(enum.Enum):
    Not_orded = 1
    Checkout = 2
    Completed = 3
    
class Carts(Base):
    __tablename__ = "carts"
    cart_id = Column(Integer, primary_key = True)
    user_id = Column(ForeignKey("carts.cart_id"))
    status = Column(Enum(Cart_status))
    total_price = Column(Integer)
