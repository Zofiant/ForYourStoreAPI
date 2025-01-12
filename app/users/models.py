import enum
from sqlalchemy import Column, Integer, String, JSON, Enum

from app.database import Base
    
class User_status(enum.Enum):
    user=1
    seller=2
    admin=3
class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key = True)
    name = Column(String, nullable= False)
    surname = Column(String, nullable= False)
    email = Column(String, nullable= False,unique=True)
    password = Column(String, nullable= False)
    image_id = Column(Integer)
    
