from sqlalchemy import JSON, Column, Integer, String, ForeignKey, Time, Enum
from app.database import Base
import enum




class Carts(Base):
    __tablename__ = "carts"
    cart_id = Column(Integer, primary_key = True)
    user_id = Column(ForeignKey("users.user_id"))
